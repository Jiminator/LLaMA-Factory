#!/bin/bash

python scripts/llama_pro.py \
    --model_name_or_path meta-llama/Meta-Llama-3-8B \
    --output_dir models/llama3-8b-pro \
    --num_expand 8
