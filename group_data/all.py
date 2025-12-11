# Inventory variables applied to all hosts.

# Select from 'llama.cpp' or 'ollama'.
ai_benchmark = 'llama.cpp'

# llama.cpp build options.
# For most GPU-enabled platforms:
llama_cpp_build_opts = '-DGGML_VULKAN=1'
# For Nvidia DGX Spark / GB10 systems:
# llama_cpp_build_opts = '-DGGML_CUDA=1 -DCMAKE_CUDA_COMPILER=/usr/local/cuda/bin/nvcc'
# For Macs with Apple Silicon:
# llama_cpp_build_opts = '-DGGML_METAL=ON -DGGML_ACCELERATE=ON'
# llama_cpp_build_opts = '-DGGML_METAL=ON -DGGML_ACCELERATE=ON -DGGML_RPC=ON'

# https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md
# Consider adding '-fa 1 --mmap 0' on memory-constrained systems
llama_bench_opts = '-n 128 -p 512,4096 -pg 4096,128 -ngl 99 -r 2'

# Select which models to benchmark. Ideally they will run entirely in VRAM.
# The `urls` list can include multiple URLs for larger multi-part models.
llama_cpp_models = {
  'tinyllama-1.1b-1t-openorca.Q4_K_M.gguf': {
    'urls': ['https://huggingface.co/TheBloke/TinyLlama-1.1B-1T-OpenOrca-GGUF/resolve/main/tinyllama-1.1b-1t-openorca.Q4_K_M.gguf'],
    'size_in_gb': 0.7,
  },
  'Llama-3.2-3B-Instruct-Q4_K_M.gguf': {
    'urls': ['https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf'],
    'size_in_gb': 1.9,
  },
  # 'llama-2-7b.Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf'],
  #   'size_in_gb': 4.1,
  # },
  # 'llama-2-13b.Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/TheBloke/Llama-2-13B-GGUF/resolve/main/llama-2-13b.Q4_K_M.gguf'],
  #   'size_in_gb': 7.4,
  # },
  # 'DeepSeek-R1-Distill-Qwen-14B-Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-14B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-14B-Q4_K_M.gguf'],
  #   'size_in_gb': 8.4,
  # },
  # 'gpt-oss-20b-Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/unsloth/gpt-oss-20b-GGUF/resolve/main/gpt-oss-20b-Q4_K_M.gguf'],
  #   'size_in_gb': 11.6,
  # },
  # 'Qwen_Qwen3-30B-A3B-Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/bartowski/Qwen_Qwen3-30B-A3B-GGUF/resolve/main/Qwen_Qwen3-30B-A3B-Q4_K_M.gguf'],
  #   'size_in_gb': 18.6,
  # },
  # 'Meta-Llama-3.1-70B-Instruct-Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/bartowski/Meta-Llama-3.1-70B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-70B-Instruct-Q4_K_M.gguf'],
  #   'size_in_gb': 42.5,
  # },
  # 'gpt-oss-120b-Q4_K_M-00001-of-00002.gguf': {
  #   'urls': [
  #     'https://huggingface.co/unsloth/gpt-oss-120b-GGUF/resolve/main/Q4_K_M/gpt-oss-120b-Q4_K_M-00001-of-00002.gguf',
  #     'https://huggingface.co/unsloth/gpt-oss-120b-GGUF/resolve/main/Q4_K_M/gpt-oss-120b-Q4_K_M-00002-of-00002.gguf',
  #   ],
  #   'size_in_gb': 62.9,
  # },
  # 'Qwen3-235B-A22B-Instruct-2507-Q4_K_M-00001-of-00003.gguf': {
  #   'urls': [
  #     'https://huggingface.co/unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF/resolve/main/Q4_K_M/Qwen3-235B-A22B-Instruct-2507-Q4_K_M-00001-of-00003.gguf',
  #     'https://huggingface.co/unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF/resolve/main/Q4_K_M/Qwen3-235B-A22B-Instruct-2507-Q4_K_M-00002-of-00003.gguf',
  #     'https://huggingface.co/unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF/resolve/main/Q4_K_M/Qwen3-235B-A22B-Instruct-2507-Q4_K_M-00003-of-00003.gguf',
  #   ],
  #   'size_in_gb': 142,
  # },
  # 'Hermes-3-Llama-3.1-405B-Q4_K_M-00001-of-00007.gguf': {
  #   'urls': [
  #     'https://huggingface.co/bartowski/Hermes-3-Llama-3.1-405B-GGUF/resolve/main/Hermes-3-Llama-3.1-405B-Q4_K_M/Hermes-3-Llama-3.1-405B-Q4_K_M-00001-of-00007.gguf',
  #     'https://huggingface.co/bartowski/Hermes-3-Llama-3.1-405B-GGUF/resolve/main/Hermes-3-Llama-3.1-405B-Q4_K_M/Hermes-3-Llama-3.1-405B-Q4_K_M-00002-of-00007.gguf',
  #     'https://huggingface.co/bartowski/Hermes-3-Llama-3.1-405B-GGUF/resolve/main/Hermes-3-Llama-3.1-405B-Q4_K_M/Hermes-3-Llama-3.1-405B-Q4_K_M-00003-of-00007.gguf',
  #     'https://huggingface.co/bartowski/Hermes-3-Llama-3.1-405B-GGUF/resolve/main/Hermes-3-Llama-3.1-405B-Q4_K_M/Hermes-3-Llama-3.1-405B-Q4_K_M-00004-of-00007.gguf',
  #     'https://huggingface.co/bartowski/Hermes-3-Llama-3.1-405B-GGUF/resolve/main/Hermes-3-Llama-3.1-405B-Q4_K_M/Hermes-3-Llama-3.1-405B-Q4_K_M-00005-of-00007.gguf',
  #     'https://huggingface.co/bartowski/Hermes-3-Llama-3.1-405B-GGUF/resolve/main/Hermes-3-Llama-3.1-405B-Q4_K_M/Hermes-3-Llama-3.1-405B-Q4_K_M-00006-of-00007.gguf',
  #     'https://huggingface.co/bartowski/Hermes-3-Llama-3.1-405B-GGUF/resolve/main/Hermes-3-Llama-3.1-405B-Q4_K_M/Hermes-3-Llama-3.1-405B-Q4_K_M-00007-of-00007.gguf',
  #   ],
  #   'size_in_gb': 243,
  # },
  # 'DeepSeek-R1-Q4_K_M-00001-of-00011.gguf': {
  #   'urls': [
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00001-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00002-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00003-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00004-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00005-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00006-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00007-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00008-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00009-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00010-of-00011.gguf',
  #     'https://huggingface.co/bartowski/DeepSeek-R1-GGUF/resolve/main/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00011-of-00011.gguf',
  #   ],
  #   'size_in_gb': 404,
  # },
  # 'Kimi-K2-Thinking-UD-Q4_K_XL-00001-of-00014.gguf': {
  #   'urls': [
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00001-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00002-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00003-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00004-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00005-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00006-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00007-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00008-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00009-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00010-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00011-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00012-of-00013.gguf',
  #     'https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/resolve/main/UD-Q4_K_XL/Kimi-K2-Instruct-UD-Q4_K_XL-00013-of-00013.gguf',
  #   ],
  #   'size_in_gb': 587,
  # },
}
