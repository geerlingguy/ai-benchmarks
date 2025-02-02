# PowerShell script to benchmark Ollama token generation rate
# Inspired by https://taoofmac.com/space/blog/2024/01/20/1800

param (
    [switch]$Help,
    [switch]$Default,
    [string]$Model,
    [int]$Count,
    [string]$OllamaBin = "ollama",
    [switch]$Markdown
)

function Show-Usage {
    Write-Output "Usage: obench.ps1 [OPTIONS]"
    Write-Output "Options:"
    Write-Output " -Help      Display this help message"
    Write-Output " -Default   Run a benchmark using some default small models"
    Write-Output " -Model     Specify a model to use"
    Write-Output " -Count     Number of times to run the benchmark"
    Write-Output " -Ollama-bin    Point to ollama executable or command (e.g if using Docker)"
    Write-Output " -Markdown      Format output as markdown"
    exit 0
}

# Parse command-line arguments

if ($Help) { 
    Show-Usage
    exit 0 
}

# Default values
if ($Default) {
    $Count = 3
    $Model = "llama3.2:3b"
}

# Ensure Ollama is available
$baseCmd = ($OllamaBin -split " ")[0]
if (-not (Get-Command $baseCmd -ErrorAction SilentlyContinue)) {
    Write-Error "Error: $baseCmd could not be found. Please check the path or install it."
    exit 1
}

# Prompt for benchmark count if not provided
if (-not $Count) {
    $Count = Read-Host "How many times to run the benchmark?"
}

# Prompt for model if not provided
if (-not $Model) {
    Write-Output "Current models available locally:"
    & $OllamaBin list
    $Model = Read-Host "Enter model you'd like to run (e.g. llama3.2)"
}

Write-Output "Running benchmark $Count times using model: $Model"
Write-Output ""
if ($Markdown) {
    Write-Output "| Run | Eval Rate (Tokens/Second) |"
    Write-Output "|-----|---------------------------|"
}

$totalEvalRate = 0
for ($run = 1; $run -le $Count; $run++) {
    $result = echo "Why is the blue sky blue?" | & $OllamaBin run $Model --verbose 2>&1 | Select-String "^eval rate:"
    
    if ($result) {
        $evalRate = ($result -split "            ")[1]
        $tokenValue = ($evalRate -split " ")[0]
        $totalEvalRate += [double]$tokenValue
        if ($Markdown) {
            Write-Output "| $run | $evalRate tokens/s |"
        } else {
            Write-Output $result
        }
    }
}

$averageEvalRate = [math]::Round($totalEvalRate / $Count, 2)
if ($Markdown) {
    Write-Output "|**Average Eval Rate**| $averageEvalRate tokens/second |"
} else {
    Write-Output "Average Eval Rate: $averageEvalRate tokens/second"
}
