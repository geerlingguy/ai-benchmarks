# AI/LLM Benchmarks (Ollama and llama.cpp)

[![.github/workflows/shellcheck.yaml](https://github.com/geerlingguy/ai-benchmarks/actions/workflows/shellcheck.yaml/badge.svg)](https://github.com/geerlingguy/ai-benchmarks/actions/workflows/shellcheck.yaml)

This repository contains AI/LLM benchmarks and benchmarking data compiled by Jeff Geerling, using a combination of [Ollama](https://ollama.com) and [llama.cpp](https://github.com/ggml-org/llama.cpp).

Benchmarking AI models can be a bit daunting, because you have to deal with hardware issues, OS issues, driver issues, stability issues... and that's all before deciding on:

  1. What _models_ to benchmark (which quantization, what particular gguf, etc.?)
  2. _How_ to benchmark the models (what context size, with or without features like flash attention, etc.?).
  3. What _results_ to worry about (prompt processing speed, generated tokens per second, etc.?)

## Llama.cpp Benchmark

_Most_ of the time I rely on llama.cpp, as it is more broadly compatible, works with more models on more systems, and incorporates features that are useful for hardware acceleration more quickly than Ollama. For example, [Vulkan was supported for years in llama.cpp prior to Ollama supporting it](https://github.com/ollama/ollama/issues/2033). Vulkan enables many AMD and Intel GPUs (as well as other Vulkan-compatible iGPUs) to work for LLM inference.

Right now I don't have a particular _script_ to assist with my llama.cpp benchmarks, I just pull a model manually, then use llama.cpp's built-in `llama-bench` utility:

```
# Download a model (gguf)
cd models && wget https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf && cd ..

# Run a benchmark
./build/bin/llama-bench -m models/Llama-3.2-3B-Instruct-Q4_K_M.gguf -n 128 -p 512,4096 -pg 4096,128 -ngl 99 -r 2
```

You can change various `llama-bench` options to test different prompt and context sizes, enable or disable features like MMIO and Flash Attention, etc.

I generally start with Llama 3.2:3B Q4_K_M because it's a small model (only 2GB), and it doesn't crash even with smaller systems like SBCs.

## Ollama Benchmark

The first and simplest benchmarks I often run—at least on systems where Ollama is supported and runs well—is my `obench.sh` script. It can run a predefined benchmark on Ollama one to many times, and generate an average score.

For a quick installation of Ollama, try:

```
curl -fsSL https://ollama.com/install.sh | sh
```

> If you're not running Linux, [download Ollama](https://ollama.com/download/mac) from the official site.

Verify you can run `ollama` with a given model:

```
ollama run llama3.2:3b
```

Then run this benchmark script:

```
./obench.sh
```

Uninstall Ollama following the [official uninstall instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md#uninstall).

For the benchmarks I save in this project, I usually run the following benchmark command, which generates an average from three runs and prints it in markdown:

```
./obench.sh -m llama3.2:3b -c 3 --markdown
```

### Ollama benchmark CLI Options

```
Usage: ./obench.sh [OPTIONS]
Options:
 -h, --help      Display this help message
 -d, --default   Run a benchmark using some default small models
 -m, --model     Specify a model to use
 -c, --count     Number of times to run the benchmark
 --ollama-bin    Point to ollama executable or command (e.g if using Docker)
 --markdown      Format output as markdown
```

## Findings

### DeepSeek R1 14b

| System | CPU/GPU | Eval Rate | Power (Peak) |
| :--- | :--- | :--- | :--- |
| [Pi 5 - 16GB](https://github.com/geerlingguy/ollama-benchmark/issues/7) | CPU | 1.20 Tokens/s | 13.0 W |
| [Pi 5 - 16GB (AMD Pro W7700<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/9) | GPU | 19.90 Tokens/s | 164 W |
| [GMKtek G3 Plus (Intel N150) - 16GB](https://github.com/geerlingguy/ollama-benchmark/issues/12) | CPU | 2.13 Tokens/s | 30.3 W |
| [Radxa Orion O6 - 16GB](https://github.com/geerlingguy/ollama-benchmark/issues/13) | CPU | 4.33 Tokens/s | 34.7 W |
| [Radxa Orion O6 - 16GB (Nvidia RTX 3080 Ti)](https://github.com/geerlingguy/ollama-benchmark/issues/13) | GPU | 64.58 Tokens/s | 465 W |
| [Minisforum MS-R1](https://github.com/geerlingguy/ai-benchmarks/issues/32) | CPU | 3.39 Tokens/s | 38.4 W |
| [M1 Ultra (48 GPU Core) 64GB](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 35.89 Tokens/s | N/A |
| [Framework Mainboard (128GB)](https://github.com/geerlingguy/ollama-benchmark/issues/21#issuecomment-3164567688) | CPU | 11.37 Tokens/s | 140W |

### DeepSeek R1 671b

| System | CPU/GPU | Eval Rate | Power (Peak) |
| :--- | :--- | :--- | :--- |
| [AmpereOne A192-32X - 512GB](https://github.com/geerlingguy/ollama-benchmark/issues/10) | CPU | 4.18 Tokens/s | 477 W |

### Llama 3.1:70b

| System | CPU/GPU | Eval Rate | Power (Peak) |
| :--- | :--- | :--- | :--- |
| [Framework Desktop Mainboard 395+](https://github.com/geerlingguy/ai-benchmarks/issues/21) | CPU | 4.97 Tokens/s | 133 W |
| [Minisforum MS-R1](https://github.com/geerlingguy/ai-benchmarks/issues/32) | CPU | 0.77 Tokens/s | 38.2 W |

### Llama 3.2:3b

| System | CPU/GPU | Eval Rate | Power (Peak) |
| :--- | :--- | :--- | :--- |
| [Pi 400 - 4GB](https://github.com/geerlingguy/ollama-benchmark/commit/96bab78f2a8e6c996c6810c5e2119274e3eb401a) | CPU | 1.60 Tokens/s | 6 W |
| [Pi 5 - 8GB](https://github.com/geerlingguy/ollama-benchmark/issues/1) | CPU | 4.61 Tokens/s | 13.9 W |
| [Pi 5 - 16GB](https://github.com/geerlingguy/ollama-benchmark/issues/70) | CPU | 4.88 Tokens/s | 11.9 W |
| [Pi 500+ - 16GB](https://github.com/geerlingguy/ollama-benchmark/issues/24) | CPU | 5.55 Tokens/s | 13 W |
| [GMKtec G3 Plus (Intel N150) - 16GB](https://github.com/geerlingguy/ollama-benchmark/issues/12) | CPU | 9.06 Tokens/s | 26.4 W |
| [Pi 5 - 8GB (AMD RX 6500 XT<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/1) | GPU | 39.82 Tokens/s | 88 W |
| [Pi 5 - 8GB (AMD RX 6700 XT<sup>1</sup>) 12GB](https://github.com/geerlingguy/ollama-benchmark/issues/1) | GPU | 49.01 Tokens/s | 94 W |
| [Pi 5 - 8GB (AMD RX 7600<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/1) | GPU | 48.47 Tokens/s | 156 W |
| [Pi 5 - 8GB (AMD Pro W7700<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/9) | GPU | 56.14 Tokens/s | 145 W |
| [Pi 500+ - 16GB (Intel Arc A310 ECO<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/29) | GPU | 13.36 Tokens/s | 50 W |
| [Pi 500+ - 16GB (Intel Arc Pro B50<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/27) | GPU | 29.80 Tokens/s | 78.5 W |
| [Pi 500+ - 16GB (Intel Arc B580<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/26) | GPU | 47.38 Tokens/s | 146 W |
| [Pi 500+ - 16GB (AMD RX 7900 XT<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/23) | GPU | 108.58 Tokens/s | 315 W |
| [Pi 500+ - 16GB (AMD RX 9070 XT<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/25) | GPU | 89.63 Tokens/s | 304 W |
| [Minisforum MS-R1](https://github.com/geerlingguy/ai-benchmarks/issues/32) | CPU | 12.12 Tokens/s | 35 W |
| [Minisforum MS-R1](https://github.com/geerlingguy/ai-benchmarks/issues/32) (Nvidia RTX A2000) | GPU | 71.36 Tokens/s | 94.3 W |
| [HiFive Premier P550 (AMD RX 580)](https://github.com/geerlingguy/ollama-benchmark/issues/20) | GPU | 36.23 Tokens/s | 150 W |
| [HiFive Premier P550 (4-core RISC-V)](https://github.com/geerlingguy/ollama-benchmark/issues/17) | CPU | 0.24 Tokens/s | 13.5 W |
| [DC-ROMA Mainboard II (8-core RISC-V)](https://github.com/geerlingguy/ollama-benchmark/issues/28) | CPU | 0.31 Tokens/s | 30.6 W |
| [M4 Mac mini (10 core - 32GB)](https://github.com/geerlingguy/ollama-benchmark/issues/2) | GPU | 41.31 Tokens/s | 30.1 W |
| M1 Max Mac Studio (10 core - 64GB) | GPU | 59.38 Tokens/s | N/A |
| [M1 Ultra (48 GPU Core) 64GB](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 108.67 Tokens/s | N/A |
| [Dell Optiplex 780 (C2Q Q8400)](https://github.com/geerlingguy/ai-benchmarks/issues/31) | CPU | 1.09 Tokens/s | 146 W |
| [Ryzen 9 7900X (Nvidia 4090)](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 237.05 Tokens/s | N/A |
| [Intel 13900K (Nvidia 5090)](https://github.com/geerlingguy/ollama-benchmark/pull/18) | GPU | 271.40 Tokens/s | N/A |
| [Intel 13900K (Nvidia 4090)](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 216.48 Tokens/s | N/A |
| [Ryzen 9 9950X (AMD 7900 XT)](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 131.2 Tokens/s | N/A |
| [Ryzen 9 7950X (Nvidia 4080)](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 204.45 Tokens/s | N/A |
| [Ryzen 9 7950X (Nvidia 4070 Ti Super)](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 198.95 Tokens/s | N/A |
| [Ryzen 9 5950X (Nvidia 4070)](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 160.72 Tokens/s | N/A |
| [System76 Thelio Astra (Nvidia A400)](https://github.com/geerlingguy/ollama-benchmark/issues/5) | GPU | 35.51 Tokens/s | 167 W |
| [System76 Thelio Astra (Nvidia A4000)](https://github.com/geerlingguy/ollama-benchmark/issues/5) | GPU | 90.92 Tokens/s | 244 W |
| [System76 Thelio Astra (AMD Pro W7700<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/5) | GPU | 89.31 Tokens/s | 261 W |
| [AmpereOne A192-32X (512GB)](https://github.com/geerlingguy/ollama-benchmark/issues/10) | CPU | 23.52 Tokens/s | N/A |
| [Framework Mainboard (128GB)](https://github.com/geerlingguy/ollama-benchmark/issues/21#issuecomment-3164568218) | GPU | 88.14 Tokens/s | 133W |

### Llama 3.1:70b

| System | CPU/GPU | Eval Rate | Power (Peak) |
| :--- | :--- | :--- | :--- |
| M1 Max Mac Studio (10 core - 64GB) | GPU | 7.25 Tokens/s | N/A |
| [Ryzen 9 7900X (Nvidia 4090)](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU/CPU | 3.10 Tokens/s | N/A |
| [AmpereOne A192-32X (512GB)](https://github.com/geerlingguy/ollama-benchmark/issues/10) | CPU | 3.86 Tokens/s | N/A |
| [Framework Mainboard (128GB)](https://github.com/geerlingguy/ollama-benchmark/issues/21#issuecomment-3164570464) | GPU | 4.47 Tokens/s | 139W |
| [Raspberry Pi CM5 Cluster (10x 16GB)](https://github.com/geerlingguy/beowulf-ai-cluster/issues/6#issuecomment-3238338502) | CPU | 0.85 Tokens/s | 70W |

<sup>1</sup> These GPUs were tested using `llama.cpp` with Vulkan support.

### Llama 3.1:405b

| System | CPU/GPU | Eval Rate | Power (Peak) |
| :--- | :--- | :--- | :--- |
| [AmpereOne A192-32X (512GB)](https://github.com/geerlingguy/ollama-benchmark/issues/10) | CPU | 0.90 Tokens/s | N/A |
| [Framework Mainboard Cluster (512GB)](https://github.com/geerlingguy/ollama-benchmark/issues/21#issuecomment-3164569199) | GPU | 0.71 Tokens/s | N/A |

## Further Reading

These benchmarks are in no way comprehensive, and I normally only compare _one aspect_ of generative AI performance—inference tokens per second. There are _many other_ aspects that are as important (or more important) my benchmarking does _not_ cover, though sometimes I get deeper into the weeds in individual issues.

See [All about Timing: A quick look at metrics for LLM serving](https://isaac-chung.github.io/blog/llm-serving) for a good overview of other metrics you may want to compare.

## Author

This benchmark was originally based on the upstream project [tabletuser-blogspot/ollama-benchmark](https://github.com/tabletuser-blogspot/ollama-benchmark), and is maintained by Jeff Geerling.
