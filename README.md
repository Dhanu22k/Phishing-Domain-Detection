# Phishing Domain Detection

This project implements a machine learning model to detect phishing domains based on various features extracted from URLs. It uses logistic regression and features such as URL components, domain properties, and network-related information.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Dhanu22k/Phishing-Domain-Detection.git
cd phishing-domain-detection
```
2. Install the required dependencies:
```bash
   pip install -r requirements.txt
```
## Usage
1. Extract Features:
   Run main.py to extract features from a given URL:
```bash
python main.py
```
2. Predict Phishing

## Note
1.Ensure that you have an active internet connection for features extraction.

## Files
<ul>
 <li>main.py: Main script for extracting features, saving to CSV, and predicting phishing status.</li>
<li>url_extraction.py: Module for extracting features from URLs.</li>
<li>prediction.py: Module for making predictions using trained models.</li>
<li>input_data.csv: CSV file containing extracted features from input URLs.</li>
<li>trained_model.pkl: Serialized trained logistic regression model.</li>
<li>scaler.pkl: Serialized scaler object used for feature scaling.</li>
</ul>

## Contributors
<h4>Dhanush K</h4>



