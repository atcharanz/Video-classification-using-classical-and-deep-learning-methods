"""
DATASET PREPARATION SCRIPT

Steps for the user:
1. Download UCF-101 dataset archive:
   https://www.crcv.ucf.edu/data/UCF101/UCF101.rar
2. Place UCF101.rar in the CURRENT PROJECT DIRECTORY.
3. Run this script.

This script will:
- Extract UCF101.rar
- Detect dataset folder structure automatically
- Create ./dataset subset
- Generate ./splits files
"""

import os
import shutil
import random

# -------------------------
# STEP 1 — Extract dataset
# -------------------------

if not os.path.exists("UCF101"):
    if not os.path.exists("UCF101.rar"):
        raise FileNotFoundError("UCF101.rar not found in project directory.")

    print("Extracting UCF101.rar...")

    # Try Mac-friendly extraction first
    if os.system("unar UCF101.rar") != 0:
        os.system("unrar x UCF101.rar")

else:
    print("UCF101 already extracted.")

# -------------------------
# STEP 2 — Detect source root
# -------------------------

root_contents = os.listdir("UCF-101")

if len(root_contents) == 1 and os.path.isdir(os.path.join("UCF-101", root_contents[0])):
    source_root = os.path.join("UCF-101", root_contents[0])
else:
    source_root = "UCF-101"



print("Detected dataset root:", source_root)

# -------------------------
# STEP 3 — Create dataset subset
# -------------------------

dataset_root = "./dataset"

selected_classes = [
    "Basketball",
    "JumpingJack",
    "WalkingWithDog"
]

os.makedirs(dataset_root, exist_ok=True)

for cls in selected_classes:
    src = os.path.join(source_root, cls)
    dst = os.path.join(dataset_root, cls)

    if not os.path.exists(src):
        raise FileNotFoundError(f"Missing class folder: {src}")

    if not os.path.exists(dst):
        shutil.copytree(src, dst)

print("Dataset subset created.")

# -------------------------
# STEP 4 — Create splits
# -------------------------

split_dir = "./splits"
os.makedirs(split_dir, exist_ok=True)

random.seed(42)

train_f = open(os.path.join(split_dir, "train.txt"), "w")
val_f   = open(os.path.join(split_dir, "val.txt"), "w")
test_f  = open(os.path.join(split_dir, "test.txt"), "w")

for cls in os.listdir(dataset_root):
    cls_path = os.path.join(dataset_root, cls)

    if not os.path.isdir(cls_path):
        continue

    videos = sorted(os.listdir(cls_path))
    random.shuffle(videos)

    n = len(videos)
    train = videos[:int(0.8*n)]
    val   = videos[int(0.8*n):int(0.9*n)]
    test  = videos[int(0.9*n):]

    for v in train:
        train_f.write(f"{cls}/{v}\n")
    for v in val:
        val_f.write(f"{cls}/{v}\n")
    for v in test:
        test_f.write(f"{cls}/{v}\n")

train_f.close()
val_f.close()
test_f.close()

print("Train/Val/Test splits created successfully.")
