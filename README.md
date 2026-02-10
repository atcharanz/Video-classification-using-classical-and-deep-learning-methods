# Video Classification — Comparative Study

**Student Name:** Charan C  
**Student ID:** 2024AC05015  
**Course:** Video Analytics (AIMLCZG531)

---

## Project Overview

This project implements and compares **classical machine learning** and **deep learning approaches** for video classification.  
The goal is to evaluate performance, computational cost, and representation learning capability across different methods.

The workflow includes:
- Video preprocessing
- Feature extraction
- Classical ML classification
- Deep learning–based classification
- Comparative evaluation

---

## Project Structure

Student_2024AC05015_Video_Classification/
│
├── code/
│ ├── part_a_classical.ipynb
│ ├── part_b_deep_learning.ipynb
│ ├── comparative_analysis.ipynb
│ ├── datasetprepare.py
│ └── requirements.txt
│
├── report/
│ └── charan_c_2024ac05015_Comparative_Report.pdf
│
├── dataset_info/
│ ├── dataset_url.txt
│ ├── dataset_description.md
│ └── data_statistics.txt
│
├── results/
│ ├── confusion_matrices/
│ ├── performance_plots/
│ └── feature_visualizations/
│
└── README.md



---

## Methods Implemented

### Classical Machine Learning
- Feature extraction from video frames
- Traditional classifiers (e.g., Logistic Regression / SVM / Random Forest)

### Deep Learning
- CNN-based feature extraction
- Temporal pooling–based video classification

---

## How to Run

Install dependencies:

pip install -r code/requirements.txt



## Run notebooks in order:

part_a_classical.ipynb

part_b_deep_learning.ipynb

comparative_analysis.ipynb

Results

The project compares models using:

Accuracy

Confusion matrices

Validation curves

Model comparison plots

Results are stored in the results/ directory.

Note: Dataset is not included due to size. 
Please download it using the link provided in dataset_info/dataset_url.txt.



Conclusion

Classical methods are computationally efficient and interpretable, while deep learning models provide stronger representation learning and scalability.
CNN with temporal pooling offers a good balance between performance and computational cost.