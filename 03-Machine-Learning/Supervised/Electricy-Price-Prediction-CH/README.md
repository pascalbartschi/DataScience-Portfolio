# Project Description

This project focuses on predicting electricity prices in Switzerland using machine learning models. The dataset includes price information from various countries and features related to seasonality. The key challenges addressed in this project include handling missing data and optimizing model performance in the face of low predictive power.

The machine learning pipeline involves data preprocessing, kernel selection, and model tuning. Data preprocessing techniques such as KNN Imputation, One-Hot Encoding, and Standardization are employed to ensure the model receives quality input data. Kernelized regression models, particularly Gaussian processes, are used to capture the complex relationships within the data. The model selection process includes cross-validation and hyperparameter tuning to find the optimal kernel and parameters for accurate predictions.

# Code Description

In this notebook, the `scikit-learn` library is used to preprocess the provided data and find an optimal kernel for modeling its characteristics using machine learning. The workflow includes the following steps:

1. **Data Preprocessing**:
   - **KNN Imputation**: Missing values are imputed using K-Nearest Neighbors.
   - **One-Hot Encoding**: Categorical variables are converted to a numeric format.
   - **Standardization**: The features are standardized to have a mean of zero and a standard deviation of one.
   
   This preprocessing pipeline was determined through exploratory data analysis (EDA) and identified as the optimal approach.

2. **Kernel Selection**:
   - The model employs kernelized regression techniques.
   - **Cross-validation with 10 folds** is used to select the optimal kernel. The **Matern kernel** shows the smallest RMSE.

3. **Model Tuning & Final Prediction**:
   - The selected Matern kernel is fine-tuned using **Randomized Search** to optimize model parameters.
   - The tuned model is then used to make the final predictions.

This structured approach provides a robust and accurate model for predicting electricity prices in Switzerland. The project reached an accuracy of 97.1% on the unseen, public dataset.