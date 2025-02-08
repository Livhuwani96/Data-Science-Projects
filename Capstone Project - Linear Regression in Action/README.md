# Ames Housing Price Prediction - Linear Regression

# Project Overview  
This project explores **housing prices in Ames, Iowa**, using a **multiple linear regression model**.  
The model predicts housing prices based on **above-grade living area** and **garage size**.  

---

# Dataset  
The dataset used is **Ames Housing Dataset** (`ames.csv`), which contains detailed housing characteristics.  

# Features Used in Model  
| Feature | Description |
|---------|------------|
| `Gr_Liv_Area` | Size of above-grade (ground living) area in square feet |
| `Garage_Area` | Size of the garage in square feet |
| `SalePrice` | Dependent variable - House sale price |

---

# Exploratory Data Analysis (EDA)

✔ Visualized **distributions** of independent and dependent variables  
✔ Identified **patterns and relationships** using scatter plots  
✔ Checked for **outliers and missing values**  

---

# Model Development 

1️ **Data Preprocessing**  
   - Handled missing values and ensured clean data  
   - Split data into **training (75%)** and **test (25%)** sets  

2️ **Linear Regression Model**  
   - Trained a **multiple linear regression model**  
   - Extracted model **intercept** and **coefficients**  

3️ **Model Evaluation**  
   - Predicted house prices on the **test set**  
   - Calculated **Mean Squared Error (MSE)** and **Root Mean Squared Error (RMSE)**  
   - Plotted **prediction vs. actual values**  

---

# Results & Key Findings

1 **Impact of Living Area (Gr_Liv_Area) on House Prices**
-There is a strong positive correlation between the size of the above-grade living area and the sale price of a house.
-Houses with larger living areas tend to have significantly higher prices, making this feature the most influential variable in the model.
-The linear relationship is evident from scatter plots, where price increases almost proportionally with square footage.

2 **Influence of Garage Size (Garage_Area)**
-While garage size has a positive relationship with house price, its impact is less significant compared to living area.
-The regression coefficient suggests that an increase in garage size leads to a smaller price increase compared to living space.
-Some outliers in the data indicate that other factors, such as location or house quality, might influence price more than garage size.

3 **Model Performance & Accuracy**
-The model performed reasonably well in predicting house prices, with an acceptable RMSE indicating a moderate level of error.
-MSE and RMSE values suggest that while the model captures major trends, it struggles with extreme values and high-end properties.
-The residual error plot shows some heteroscedasticity, implying that price variability increases for more expensive homes.

4 **Potential Improvements**
-Including more features such as lot size, number of bedrooms, and neighborhood quality could improve predictive accuracy.
-Applying polynomial regression or regularization techniques (Ridge/Lasso Regression) could help refine predictions.
-Addressing outliers and conducting feature engineering (e.g., creating interaction terms) may further enhance model performance.

---
