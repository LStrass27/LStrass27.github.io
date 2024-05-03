# Import Data
batters <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/batter_export.csv")
pitchers <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/pitcher_export.csv")

# Scale down the "DOLLARS" variable by 1000000
batters$DOLLARS <- batters$DOLLARS / 1000000

# Compute per-game statistics
batters$G_G <- batters$G / batters$G
batters$R_G <- batters$R / batters$G
batters$HR_G <- batters$HR / batters$G
batters$RBI_G <- batters$RBI / batters$G
batters$BB_G <- batters$BB / batters$G
batters$SB_G <- batters$SB / batters$G
batters$HITS_G <- batters$HITS / batters$G

# Convert "POS" to a factor (categorical variable)
batters$POS <- as.factor(batters$POS)

# Create dummy variables for "POS"
dummy_POS <- model.matrix(~ POS - 1, data = batters)  # -1 removes intercept term

# Combine dummy variables with other predictors
batters_with_dummies <- cbind(batters, dummy_POS)

yrs_mse = 0
cash_mse = 0


for(m in 1:100){
  set.seed(m)
  # Split the data into training and testing sets
  train_index <- sample(1:nrow(batters_with_dummies), 0.8 * nrow(batters_with_dummies))
  train_data <- batters_with_dummies[train_index, ]
  test_data <- batters_with_dummies[-train_index, ]
  
  # Standardize predictors (excluding the response variables and categorical variables)
  predictors <- c("G", "R", "HR", "RBI", "BB", "SB", "HITS", "YEAR", "AGE", "R_G", "HR_G", "RBI_G", "BB_G", "SB_G", "HITS_G", "AS")
  train_data_scaled <- train_data
  train_data_scaled[, predictors] <- scale(train_data_scaled[, predictors])
  
  # Fit linear regression models with "POS" included
  bat.model.yrs <- lm(YRS ~ G + R + HR + RBI + BB + SB + HITS + YEAR + AGE 
                      + POS1B + POS2B + POSSS + POS3B + POSC 
                      + R_G + HR_G + RBI_G + BB_G + SB_G + HITS_G 
                      + AS + exp(AS) + AS/AGE,
                      data = train_data_scaled)
  summary(bat.model.yrs)
  
  bat.model.cash <- lm(DOLLARS ~ G + R + HR + RBI + BB + SB + HITS + YEAR + AGE
                       +POS1B + POS2B + POSSS + POS3B + POSC +
                         R_G + HR_G + RBI_G + BB_G + SB_G + HITS_G 
                       + AS + exp(AS) + AS/AGE, 
                       data = train_data_scaled)
  summary(bat.model.cash)
  
  # Make predictions on the testing data
  test_data_scaled <- test_data
  test_data_scaled[, predictors] <- scale(test_data_scaled[, predictors])
  
  predictions_yrs <- predict(bat.model.yrs, newdata = test_data_scaled)
  predictions_cash <- predict(bat.model.cash, newdata = test_data_scaled)
  
  # Calculate Mean Squared Error (MSE) for both models
  mse_yrs <- mean((predictions_yrs - test_data$YRS)^2)
  mse_cash <- mean((predictions_cash - test_data$DOLLARS)^2)
  
  for(i in 1:nrow(test_data)){
    cat(test_data[i,]$Name, predictions_yrs[i] - test_data[i,]$YRS, predictions_cash[i] - test_data[i,]$DOLLARS, "\n")
  }
  #print(paste("Mean Squared Error (Years):", mse_yrs))
  #print(paste("Mean Squared Error (Dollars):", mse_cash))
  
  yrs_mse = mse_yrs + yrs_mse
  cash_mse = mse_cash + cash_mse
}
print(paste("Mean Squared Error Average (Years):", yrs_mse/ 100))
print(paste("Mean Squared Error Average (Dollars):", cash_mse/ 100))
