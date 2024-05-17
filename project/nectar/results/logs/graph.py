import matplotlib.pyplot as plt
import pandas as pd
import json
import os

def read_jsonl_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return pd.DataFrame(data)

def plot_loss_curves(directory):
    # List all JSONL files in the directory
    file_paths = [f for f in os.listdir(directory) if f.endswith('.jsonl')]
    plt.figure(figsize=(10, 6))

    for file_path in file_paths:
        # Read data from each file
        df = read_jsonl_file(os.path.join(directory, file_path))
        # Plot the loss curve
        plt.plot(df['current_steps'], df['loss'], label=file_path.replace('.jsonl', ''))

    plt.xlabel('Steps')
    plt.ylabel('Loss')
    plt.title('Loss Curves for Nectar Finetuning')
    plt.legend()
    plt.grid(True)
    # Save the figure
    plt.savefig(os.path.join(directory, 'loss_curves.png'))
    plt.show()

# Example usage
plot_loss_curves('.')
