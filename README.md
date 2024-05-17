# Exploring Supervised Finetuning Methods for Large Language Models
2024 Final project for Deep Learning 

This is the fork of LLamafactory used to perform all finetuning experiments. 

Our custom YAML files used for fine-tuning can be found in project/<DATASET>/train.
Our custom YAML files used for computing ROUGE scores are found in project/<DATASET>/eval.
Our collected results and graphs are found in project/<DATASET>/results.

To run LLamafactory with our custom YAML files first clone this repository and run:
```
cd LLaMA-Factory
pip install -e .[torch,metrics]
```
Then run:
```
nvidia-smi --query-gpu=index,timestamp,utilization.gpu,memory.total,memory.free,memory.used --format=csv, --loop=10 > MEMORY_LOG_FILE_NAME.csv 2>&1 & CUDA_VISIBLE_DEVICES=0 llamafactory-cli train project/<DATASET>/train/llama3_<DATASET>_<SFT_METHOD_NAME>.yaml
```
To evaluate, run:
CUDA_VISIBLE_DEVICES=0 llamafactory-cli train project/<DATASET>/eval/llama3_<DATASET>_<SFT_METHOD_NAME>.yaml

The model and the results should be saved in the saves folder not tracked by this repository.
