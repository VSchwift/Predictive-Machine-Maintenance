# Machine Maintenance Prediction

This project aims to predict machine maintenance based on various input features. It utilizes a machine learning model trained on a dataset of machine records and failure information. The model predicts whether a machine is in need of maintenance or not.

## Table of Contents
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)

## Installation

To use this project, you need to have Python and the required dependencies installed. You can install the dependencies by running the following command:


## Usage

To use the machine maintenance prediction model, follow these steps:

1. Clone this repository to your local machine.

2. Install the required dependencies as mentioned in the installation section.

3. Run the `app.py` file to start the prediction application.

4. Follow the instructions in the application to enter the required information and get the prediction results.

## Dataset

The dataset used for training the machine maintenance prediction model contains information about various machine records, including features such as air temperature, process temperature, rotational speed, torque, tool wear, power, and machine type. It also includes labels indicating whether a machine experienced failure or not.

## Model Training

The model was trained using the machine records dataset. The dataset was preprocessed to handle categorical features and scaled to ensure all features are on the same scale. The RandomForestClassifier algorithm was used to train the model, which was then saved for future predictions.

## Results

The machine maintenance prediction model achieved an accuracy of 99.6% on the test dataset. The classification report and confusion matrix provide further evaluation metrics for the model's performance.
The most notable features that contribute to the prediction are Rotational speed [rpm], Torque [Nm], and Total wear [min]. 

![Machine Maintenance](images/machine-maintenance.png)



