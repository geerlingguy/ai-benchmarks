# ollama-benchmark

[![.github/workflows/shellcheck.yaml](https://github.com/geerlingguy/ollama-benchmark/actions/workflows/shellcheck.yaml/badge.svg)](https://github.com/geerlingguy/ollama-benchmark/actions/workflows/shellcheck.yaml)

This bash script benchmarks LLMs using [Ollama](https://ollama.com), and also aggregates test data using other LLM tools such as [llama.cpp](https://github.com/ggml-org/llama.cpp).

For a quick installation, try:

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

## CLI Options

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
| [M1 Ultra (48 GPU Core) 64GB](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 35.89 Tokens/s | N/A |
| [Framework Mainboard (128GB)](https://github.com/geerlingguy/ollama-benchmark/issues/21#issuecomment-3164567688) | CPU | 11.37 Tokens/s | 140W |

### DeepSeek R1 671b

| System | CPU/GPU | Eval Rate | Power (Peak) |
| :--- | :--- | :--- | :--- |
| [AmpereOne A192-32X - 512GB](https://github.com/geerlingguy/ollama-benchmark/issues/10) | CPU | 4.18 Tokens/s | 477 W |

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
| [Pi 500+ - 16GB (Intel Arc Pro B50<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/27) | GPU | 29.80 Tokens/s | 78.5 W |
| [Pi 500+ - 16GB (Intel Arc B580<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/26) | GPU | 47.38 Tokens/s | 146 W |
| [Pi 500+ - 16GB (AMD RX 7900 XT<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/23) | GPU | 108.58 Tokens/s | 315 W |
| [Pi 500+ - 16GB (AMD RX 9070 XT<sup>1</sup>)](https://github.com/geerlingguy/ollama-benchmark/issues/25) | GPU | 89.63 Tokens/s | 304 W |
| [M4 Mac mini (10 core - 32GB)](https://github.com/geerlingguy/ollama-benchmark/issues/2) | GPU | 41.31 Tokens/s | 30.1 W |
| M1 Max Mac Studio (10 core - 64GB) | GPU | 59.38 Tokens/s | N/A |
| [M1 Ultra (48 GPU Core) 64GB](https://github.com/geerlingguy/ollama-benchmark/pull/11) | GPU | 108.67 Tokens/s | N/A |
| [HiFive Premier P550 (4-core RISC-V)](https://github.com/geerlingguy/ollama-benchmark/issues/20) | CPU | 0.24 Tokens/s | 13.5 W |
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

This script is just a quick way of comparing _one aspect_ of generative AI performance. There are _many other_ aspects that are as important (or more important) this script does _not_ cover.

See [All about Timing: A quick look at metrics for LLM serving](https://isaac-chung.github.io/blog/llm-serving) for a good overview of other metrics you may want to compare when running Ollama.

## Author

This benchmark is based on the upstream project [tabletuser-blogspot/ollama-benchmark](https://github.com/tabletuser-blogspot/ollama-benchmark), and is maintained by Jeff Geerling.
