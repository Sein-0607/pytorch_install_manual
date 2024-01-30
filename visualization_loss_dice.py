import os
import re
import numpy as np
import matplotlib.pyplot as plt

def extract_epoch_loss_dice(filename):
    pattern = re.compile(r"epoch_(\d+)_loss_([\d\.]+)_dice_([\d\.]+)")
    match = pattern.search(filename)
    if match:
        # 마침표가 있을 경우 제거합니다
        loss_str = match.group(2).rstrip('.')
        dice_str = match.group(3).rstrip('.')
        return int(match.group(1)), float(loss_str), float(dice_str)
    return None, None, None

def read_dice_scores_from_txt(filename):
    with open(filename, 'r') as f:
        scores = [float(line.split(': ')[1]) for line in f]
        return np.mean(scores)

# Assuming all files are in the same directory
directory_path = 'PATH/TO/TRAINING/OUTPUT'
file_names = sorted([f for f in os.listdir(directory_path) if f.endswith('.pth')])

epochs = []
losses = []
dice_scores = []
for file_name in file_names:
    epoch, loss, dice = extract_epoch_loss_dice(file_name)
    if epoch is not None:
        txt_filename = file_name.replace('.pth', '_dice.txt')
        txt_path = os.path.join(directory_path, txt_filename)
        
        # 파일이 존재하는지 확인하고, 존재하지 않으면 pass합니다.
        if not os.path.exists(txt_path):
            print(f"Warning: The file {txt_path} does not exist. Skipping.")
            continue
        
        avg_dice_score = read_dice_scores_from_txt(txt_path)
        
        epochs.append(epoch)
        losses.append(loss)
        dice_scores.append(avg_dice_score)


# Plotting
plt.figure(figsize=(15, 5))

# Loss Plot
plt.subplot(1, 2, 1)
plt.plot(epochs, losses, 'r-', label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss Over Epochs')
plt.legend()

# Dice Score Plot
plt.subplot(1, 2, 2)
plt.plot(epochs, dice_scores, 'b-', label='Average Dice Score')
plt.xlabel('Epoch')
plt.ylabel('Average Dice Score')
plt.title('Dice Score Over Epochs')
plt.legend()

plt.tight_layout()
plt.show()
