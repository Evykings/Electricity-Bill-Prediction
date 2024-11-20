# Electricity Bill Prediction ⚡️🏠📉 
Welcome to the **Electricity Bill Prediction** This project leverages machine learning to predict monthly electricity bills based on factors such as energy consumption, previous reading, and historical data. By analyzing user-specific data, it provides actionable insights to help optimize energy usage and reduce costs.


# 📌 Project Overview
The Electricity Bill Prediction project is a data-driven solution designed to estimate monthly electricity bills by analyzing key factors like historical usage, weather conditions, and household attributes. With machine learning at its core, the project provides users with accurate predictions and actionable insights to manage energy consumption effectively.

## 🏆 Goals:
*  **Predict Monthly Bills:** Provide users with an estimated electricity bill based on their consumption patterns.
*  **Understand Usage Trends:** Analyze historical data to identify seasonal or behavioral energy trends.
*  **Optimize Energy Use:** Empower users to make informed decisions to reduce electricity costs and improve efficiency.

## 🛠️ Tools and Resources Used 
**Python Version:** 3.12  

**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, pipeline, SGDRegressor

**For Web Framework Requirements:**  ```pip install -r requirements.txt``` 

## 📊 Key Features

*   **Exploratory Data Analysis (EDA):** Understand patterns and relationships in the dataset.
*   **Feature Engineering:** Extract meaningful features for accurate predictions.
*   **Modeling:** Train and evaluate SGDRegressor machine learning model.
*   **Evaluation Metrics:** Root Mean Square Error (RMSE) to assess model performance.

## 📖 Dataset

*    **Source:**  The dataset for this project was sourced from an Electricity Distribution Company, providing real-world insights into energy usage and billing patterns. It includes detailed records of electricity consumption, billing amounts, customer profiles, and other relevant factors over a specified time period.
*    **Description:** The dataset used in this project is a comprehensive collection of electricity consumption and billing information provided by an Electricity Distribution Company. It contains detailed records essential for predicting electricity bills and analyzing consumption patterns. It has 35189 rows and 12 columns. Below is an overview of the key columns in the dataset:

  ### Dataset Columns:
*  **GlobalAccountNames:** Unique identifiers for customer accounts.
*  **CAP:** The maximum amount that energy suppliers can charge for each unit of energy and standing charge for customers on a standard variable tariff.
*  **Billed Amount:** The total amount billed to the customer during a billing cycle.
*  **Previous Payment:** The last payment made by the customer.
*  **Previous Reading:** The meter reading from the previous billing cycle.
*  **Current Reading:** The meter reading for the current billing cycle.
*  **Energy Charges:** Charges based on the energy consumption.
*  **Updated DSS Names:** Distribution Sub-Station names associated with a customer.
*  **Tariff Classes:** The tariff category (e.g., residential, commercial, industrial) under which the customer is billed.

## 🧹✨ Data Cleaning
The dataset underwent a thorough cleaning process to ensure data quality and prepare it for analysis and model training. Below is a description of the key steps in the cleaning stage:

### 🔑 Key Steps in Data Cleaning:
*  **Handling Missing Values:** Missing values were identified and addressed to maintain dataset integrity. Imputation was used to fill in missing values based on statistical methods, ensuring that no critical data points were lost.
*  **Removing Duplicates:** Duplicate rows were identified and dropped to eliminate redundancy and avoid bias in the analysis.
*  **Feature Engineering:** A new feature was engineered by calculating the median of each column. The calculated medians served as a baseline for comparison, enabling more meaningful analysis and insights. 
*  **Normalization of Numerical columns:** Normalization on the numerical columns to bring the values into a comparable range.
*  **OneHotEncoder:** Encoded the Categorical Columns because the machine learning model only accepts numerical variables. 

## 📊 EDA
  **Data Visualization:**
   * **Histograms and Density Plots:** Analyzed the distribution of numerical features, identifying skewness and outliers.
     ![alt text](https://github.com/Evykings/Electricity-Bill-Prediction/blob/b0b8b9d66027362622fdc2a6cf380f2608dc2573/bedc%20tariff%20class%20dis.png)
   * **Bar Charts:** Explored categorical variables like Tariff Classes, Energy Charges, Previous Payments and Global Accounts to understand their frequency and composition.
     ![alt text](https://github.com/Evykings/Electricity-Bill-Prediction/blob/main/energy%20charge%20vs%20tariff.png)
     ![alt text](https://github.com/Evykings/Electricity-Bill-Prediction/blob/main/previous%20payment%20vs%20billed%20amount.png)
   * **Scatter Plots:** Examined relationships between Energy Charges, Current Reading, and Previous Reading.
     ![alt text](https://github.com/Evykings/Electricity-Bill-Prediction/blob/main/scatter%20plot%20of%20energy%20charge%20vs%20billed%20amount.png)
   * **Correlation Analysis:** Computed a correlation matrix to identify relationships between features, highlighting those most relevant for predicting Billed Amount. Visualized      correlations using a heatmap to detect strong positive or negative associations.
     ![alt text](https://github.com/Evykings/Electricity-Bill-Prediction/blob/main/heatmap.png)


## ⚙️ Model Building 

To predict electricity bills accurately, several machine learning models were developed, trained, and evaluated using the cleaned dataset. The process involved feature selection, hyperparameter tuning, and performance evaluation to identify the best model.

### Steps in Model Building:

**1.**  **Data Splitting:**
The dataset was split into training (80%) and testing (20%) sets to evaluate the model's generalization ability.

**2.**  **Feature Engineering:**
*  Selected key features such as ```Previous Payment``` , ```Previous Reading``` ,```Current Reading``` , ```Tariff Classes``` , and ```Energy Charges```.
*  Normalized numerical features to standardize scales.

**3.**  **Model Selection:**
The SGDRegressor (Stochastic Gradient Descent Regressor) was chosen as the primary model for this project due to its ability to handle large datasets efficiently and its suitability for linear regression tasks with regularization options.

**4.**  **Hyperparameter Tuning:**
Used grid search and cross-validation to optimize parameters for the best-performing models.

  **Objective:** Optimize the performance of the SGDClassifier by tuning key hyperparameters such as:
  *  Learning rate  ```0.000001```, ```0.00001```, ```0.0001```, ```0.0002```, ```0.0005```, ```0.0007```.
    
  **Approach:** Leveraged Grid Search Cross-Validation (GridSearchCV) to perform an exhaustive search over hyperparameter combinations. Used a stratified k-fold cross-validation approach to ensure robust performance evaluation and prevent overfitting.

## 💡Model performance
The model was evaluated using the Root Mean Square Error to predict the Billed Amount:

*  **Root Mean Squared Error (RMSE):** Penalizes large errors more heavily, giving insight into model robustness.

**RMSE:** 8.010851941508868e+26

**Scatter plot of predictions**
![alt text](https://github.com/Evykings/Prediction-of-Elderly-Falls/blob/main/images/fall.png)



