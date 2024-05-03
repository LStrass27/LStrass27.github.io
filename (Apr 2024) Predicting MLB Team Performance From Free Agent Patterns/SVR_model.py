# Import necessary libraries
import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error


# Load data
batters = pd.read_csv("batter_export.csv")

# Convert categorical variable "POS" to dummy variables
batters_with_dummies = pd.get_dummies(batters, columns=["POS"], drop_first=True)

# Divide "DOLLARS" category by 1,000,000
batters_with_dummies["DOLLARS"] /= 1000000  # Divide by 1,000,000 to scale down

# Include "/G" stats as additional predictors
batters_with_dummies["R_PER_GAME"] = batters_with_dummies["R"] / batters_with_dummies["G"]
batters_with_dummies["HR_PER_GAME"] = batters_with_dummies["HR"] / batters_with_dummies["G"]
batters_with_dummies["RBI_PER_GAME"] = batters_with_dummies["RBI"] / batters_with_dummies["G"]
batters_with_dummies["SB_PER_GAME"] = batters_with_dummies["SB"] / batters_with_dummies["G"]
batters_with_dummies["HITS_PER_GAME"] = batters_with_dummies["HITS"] / batters_with_dummies["G"]
batters_with_dummies["BB_PER_GAME"] = batters_with_dummies["BB"] / batters_with_dummies["G"]

# Create interaction terms
batters_with_dummies['AS_AGE_interaction'] = batters_with_dummies['AS'] / batters_with_dummies['AGE']

# Define predictor variables (X) and target variables (y) for both YRS and DOLLARS
X = batters_with_dummies.drop(columns=["YRS", "DOLLARS", "Name"])
y_years = batters_with_dummies["YRS"]
y_dollars = batters_with_dummies["DOLLARS"]

# Standardize predictor variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

yr_mse = 0
dollar_mse = 0
for i in range(100):

    # Split data into training and testing sets
    X_train, X_test, y_train_years, y_test_years = train_test_split(X_scaled, y_years, test_size=0.2, random_state=i)
    X_train, X_test, y_train_dollars, y_test_dollars = train_test_split(X_scaled, y_dollars, test_size=0.2, random_state=i)

    # Define SVR models for predicting years and dollars
    svr_years = SVR(kernel='rbf')  # Radial Basis Function (RBF) kernel
    svr_dollars = SVR(kernel='poly')  # Radial Basis Function (RBF) kernel

    # Fit SVR models
    svr_years.fit(X_train, y_train_years)
    svr_dollars.fit(X_train, y_train_dollars)

    # Predictions
    y_pred_years = svr_years.predict(X_test)
    y_pred_dollars = svr_dollars.predict(X_test)

    # Evaluate model performance (MSE)
    mse_years = mean_squared_error(y_test_years, y_pred_years)
    mse_dollars = mean_squared_error(y_test_dollars, y_pred_dollars)

    print("Mean Squared Error (Years):", mse_years)
    print("Mean Squared Error (Dollars):", mse_dollars)

    yr_mse += mse_years
    dollar_mse += mse_dollars

print("Mean Squared Error Average(Years):", yr_mse/100)
print("Mean Squared Error Average(Dollars):", dollar_mse/100)
