# Dataset Description

This project uses a subset of the UCF-101 action recognition dataset.

UCF-101 is a video action recognition dataset containing 101 action
categories collected from YouTube videos.

Official dataset source:
https://www.crcv.ucf.edu/data/UCF101.php

---

## Selected Classes

For this assignment, the following classes were selected:

- Basketball
- JumpingJack
- WalkingWithDog

---

## Preprocessing

The dataset preparation pipeline includes:

- Extracting UCF101.rar
- Selecting three action classes
- Uniform frame sampling per video
- Frame resizing to 224×224
- Train/validation/test split generation

---

## Dataset Structure

dataset/
├── Basketball
├── JumpingJack
└── WalkingWithDog
