#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python src/evaluate.py \
    --model_name_or_path meta-llama/Meta-Llama-3-8B \
    --adapter_name_or_path saves/llama3-8b/lora/wiki_qa \
    --template fewshot \
    --finetuning_type lora \
    --save_dir saves/llama3-8b/lora/wiki_qa-eval\
    --task mmlu \
    --split test \
    --lang en \
    --n_shot 5 \
    --batch_size 4