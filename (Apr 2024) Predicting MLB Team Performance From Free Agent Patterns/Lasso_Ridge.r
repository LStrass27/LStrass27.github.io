# Load the necessary library
library(glmnet)

# Import Data
batters <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/batter_export.csv")

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

# Create interaction terms
batters$exp_AS <- exp(batters$AS)
batters$AS_div_AGE <- batters$AS / batters$AGE

# Convert "POS" to a factor (categorical variable)
batters$POS <- as.factor(batters$POS)

# Create dummy variables for "POS"
dummy_POS <- model.matrix(~ POS - 1, data = batters)  # -1 removes intercept term

# Combine dummy variables with other predictors
batters_with_dummies <- cbind(batters, dummy_POS)

# Define a function to compute mean squared error (MSE)
compute_mse <- function(predictions, actual_values) {
  mean((predictions - actual_values)^2)
}

# Initialize variables to store MSE
yrs_mse <- 0
cash_mse <- 0

# Repeat the process for 100 iterations
set.seed(87)
  
# Split the data into training and testing sets
train_index <- sample(1:nrow(batters_with_dummies), 0.8 * nrow(batters_with_dummies))
train_data <- batters_with_dummies[train_index, ]
test_data <- batters_with_dummies[-train_index, ]
  
# Standardize predictors (excluding the response variables and categorical variables)
predictors <- c("G", "R", "HR", "RBI", "BB", "SB", "HITS", "YEAR", "AGE", "R_G", "HR_G", "RBI_G", "BB_G", "SB_G", "HITS_G", "AS", "exp_AS", "AS_div_AGE", "POS1B", "POS2B", "POSSS", "POS3B", "POSC")
train_data_scaled <- train_data
train_data_scaled[, predictors] <- scale(train_data_scaled[, predictors])
  
# Fit Lasso regression models with "POS" included
batter_model_yrs <- glmnet(as.matrix(train_data_scaled[, predictors]), train_data_scaled$YRS, alpha = 1)  # Lasso regression
batter_model_cash <- glmnet(as.matrix(train_data_scaled[, predictors]), train_data_scaled$DOLLARS, alpha = 1)  # Lasso regression
  
# Make predictions on the testing data
test_data_scaled <- test_data
test_data_scaled[, predictors] <- scale(test_data_scaled[, predictors])
  
predictions_yrs <- predict(batter_model_yrs, s = 0, newx = as.matrix(test_data_scaled[, predictors]))
predictions_cash <- predict(batter_model_cash, s = 0, newx = as.matrix(test_data_scaled[, predictors]))
  
# Calculate Mean Squared Error (MSE) for both models
mse_yrs <- compute_mse(predictions_yrs, test_data$YRS)
mse_cash <- compute_mse(predictions_cash, test_data$DOLLARS)
yrs_mse <- mse_yrs + yrs_mse
cash_mse <- mse_cash + cash_mse

# Compute average MSE
print(paste("Mean Squared Error Average (Years):", yrs_mse))
print(paste("Mean Squared Error Average (Dollars):", cash_mse))

#---------------------- START PITCHERS-----------------------------------------
#---------------------- START PITCHERS-----------------------------------------
#---------------------- START PITCHERS-----------------------------------------

pitchers <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/pitcher_export.csv")

# Scale down the "DOLLARS" variable by 1000000
pitchers$DOLLARS <- pitchers$DOLLARS / 1000000

pitchers[is.na(pitchers)] <- 0

# Compute per-game statistics
pitchers$SO_G <- pitchers$SO / pitchers$G
pitchers$IP_G <- pitchers$IP / pitchers$G

# Create interaction terms
pitchers$exp_AS <- exp(pitchers$AS)
pitchers$AS_div_AGE <- pitchers$AS / pitchers$AGE

# Convert "POS" to a factor (categorical variable)
pitchers$POS <- as.factor(pitchers$POS)

# Create dummy variables for "POS"
dummy_POS <- model.matrix(~ POS - 1, data = pitchers)  # -1 removes intercept term

# Combine dummy variables with other predictors
pitchers_with_dummies <- cbind(pitchers, dummy_POS)

# Define a function to compute mean squared error (MSE)
compute_mse <- function(predictions, actual_values) {
  mean((predictions - actual_values)^2)
}

# Initialize variables to store MSE
yrs_mse <- 0
cash_mse <- 0

# Repeat the process for 100 iterations
set.seed(10)
  
# Split the data into training and testing sets
train_index <- sample(1:nrow(pitchers_with_dummies), 0.8 * nrow(pitchers_with_dummies))
train_data <- pitchers_with_dummies[train_index, ]
test_data <- pitchers_with_dummies[-train_index, ]
  
# Standardize predictors (excluding the response variables and categorical variables)
predictors <- c("G", "GS", "IP", "SV", "WERA", "WWHip", "SO9", "SO", "AGE", "IP_G", "SO_G", "AS", "YEAR", "exp_AS", "AS_div_AGE", "POSRP", "POSSP")
train_data_scaled <- train_data
train_data_scaled[, predictors] <- scale(train_data_scaled[, predictors])
  
# Fit ridge regression models with "POS" included
pitcher_model_yrs <- glmnet(as.matrix(train_data_scaled[, predictors]), train_data_scaled$YRS, alpha = 0)  # Ridge regression
pitcher_model_cash <- glmnet(as.matrix(train_data_scaled[, predictors]), train_data_scaled$DOLLARS, alpha = 0)  # Ridge regression
  
# Make predictions on the testing data
test_data_scaled <- test_data
test_data_scaled[, predictors] <- scale(test_data_scaled[, predictors])
  
predictions_yrs <- predict(pitcher_model_yrs, s = 0, newx = as.matrix(test_data_scaled[, predictors]))
predictions_cash <- predict(pitcher_model_cash, s = 0, newx = as.matrix(test_data_scaled[, predictors]))
  
# Calculate Mean Squared Error (MSE) for both models
mse_yrs <- compute_mse(predictions_yrs, test_data$YRS)
mse_cash <- compute_mse(predictions_cash, test_data$DOLLARS)
yrs_mse <- mse_yrs + yrs_mse
cash_mse <- mse_cash + cash_mse

# Compute average MSE
print(paste("Mean Squared Error Average (Years):", yrs_mse))
print(paste("Mean Squared Error Average (Dollars):", cash_mse))

#---------------------- START Model Evaluation-----------------------------------------
top20 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_FA_T20_2010-2019.csv")
team.performance <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLBTeamPerformance(2010-19).csv")
team.col <- top20$NEW.TEAM

# Poster Data Matrix
poster.data <- matrix(nrow = 0, ncol = 5)

# Assign column names
colnames(poster.data) <- c("Year", "Player", "Team", "Contract", "Net Value")

# Compare players to determine if they under/overpaid
predictors <- c("G", "R", "HR", "RBI", "BB", "SB", "HITS", "YEAR", "AGE", "R_G", "HR_G", "RBI_G", "BB_G", "SB_G", "HITS_G", "AS", "exp_AS", "AS_div_AGE", "POS1B", "POS2B", "POSSS", "POS3B", "POSC")
scaled.hitters <- as.data.frame(scale(batters_with_dummies[, predictors]))
top20$Paid.class <- 0
predictors <- c("G", "GS", "IP", "SV", "WERA", "WWHip", "SO9", "SO", "AGE", "IP_G", "SO_G", "AS", "YEAR", "exp_AS", "AS_div_AGE", "POSRP", "POSSP")
scaled.pitchers <- as.data.frame(scale(pitchers_with_dummies[, predictors]))
over <- 0
under <- 0

for(i in 1:nrow(top20)){
  player <- top20[i,]
  year <- as.numeric(top20$Year[i])
  player.name <- top20$PLAYER[i]
  position <- top20$POS[i]
  cont.value <- as.numeric(top20$DOLLARS[i]) / 1000000
  team.name <- top20$NEW.TEAM[i]

  if((position == "RP") || (position == "SP")){
    predictors <- c("G", "GS", "IP", "SV", "WERA", "WWHip", "SO9", "SO", "AGE", "IP_G", "SO_G", "AS", "YEAR", "exp_AS", "AS_div_AGE", "POSRP", "POSSP")
    for(j in 1:nrow(scaled.pitchers)){
      if((pitchers_with_dummies[j,]$NAME == player.name) && (pitchers_with_dummies[j,]$YEAR == year)){
        predictions.cash <- predict(pitcher_model_cash, s = 0, newx = as.matrix(scaled.pitchers[j,predictors]))
        if(predictions.cash > cont.value / 1.5){
          top20$Paid.class[i] <- 1
          under <- under + 1
        }
        else{
          top20$Paid.class[i] <- 0
          over <- over + 1
        }
        row <- c(year, player.name, team.name, cont.value, as.numeric(predictions.cash * 1.5 - cont.value))
        poster.data <- rbind(poster.data, row)
        break;
      }
    }
  }
  else{
    predictors <- c("G", "R", "HR", "RBI", "BB", "SB", "HITS", "YEAR", "AGE", "R_G", "HR_G", "RBI_G", "BB_G", "SB_G", "HITS_G", "AS", "exp_AS", "AS_div_AGE", "POS1B", "POS2B", "POSSS", "POS3B", "POSC")
    for(j in 1:nrow(scaled.hitters)){
      if((batters_with_dummies[j,]$Name == player.name) && (batters_with_dummies[j,]$YEAR == year)){
        predictions.cash <- predict(batter_model_cash, s = 0, newx = as.matrix(scaled.hitters[j,predictors]))
        if(predictions.cash > cont.value / 1.5){
          top20$Paid.class[i] <- 1
          under <- under + 1
        }
        else{
          top20$Paid.class[i] <- 0
          over <- over + 1
        }
        poster.data <- rbind(poster.data, c(year, player.name, team.name, cont.value, as.numeric(predictions.cash * 1.5 - cont.value)))
        break;
      }
    }
  }
}

poster.data <- as.data.frame(poster.data)
poster.data[c("Contract", "Net Value")] <- lapply(poster.data[c("Contract", "Net Value")], as.numeric)

#---------------------- START DATA ANALYSIS-----------------------------------------
#---------------------- START DATA ANALYSIS-----------------------------------------
#---------------------- START DATA ANALYSIS-----------------------------------------

# Create a table with unique values and their counts
unique.counts <- table(team.col)

# Convert the table to a data frame for better readability
unique.counts.df <- as.data.frame(unique.counts)
names(unique.counts.df) <- c('Team_name', 'Count')

merged.count.performance <- merge(unique.counts.df, team.performance, by = "Team_name", all = FALSE)

plot(merged.count.performance$Count, merged.count.performance$PerfPts, main = "Free Agent Count versus Team Performance", xlab = "Top Free Agent Count", ylab = "Team Performance Points")

# Fit Regression to Scatter plot
fit <- lm(merged.count.performance$PerfPts ~ merged.count.performance$Count)

# Add regression line to plot
abline(fit, col = "red")

# Calculate correlation coefficient
correlation <- cor(merged.count.performance$Count,merged.count.performance$PerfPts )
print(paste("Correlation coefficient:", correlation))

# Evaluate percentages
library(dplyr)

# Percent Accuracy table
accuracy.table <- top20 %>%
  group_by(NEW.TEAM) %>%
  summarize(accuracy = mean(Paid.class))

names(accuracy.table) <- c('Team_name', 'Accuracy')

merged.accuracy <- merge(accuracy.table, team.performance, by = "Team_name", all = FALSE)

plot(merged.accuracy$Accuracy, merged.accuracy$PerfPts, main = "Free Agent Accuracy versus Team Performance", xlab = "Top Free Agent Accuracy", ylab = "Team Performance Points")

# Fit Regression to Scatter plot
fit <- lm(merged.accuracy$PerfPts ~ merged.accuracy$Accuracy)

# Add regression line to plot
abline(fit, col = "red")

# Calculate correlation coefficient
correlation <- cor(merged.accuracy$Accuracy,merged.accuracy$PerfPts )
print(paste("Correlation coefficient:", correlation))

# Split by market
large.markets <- c("Yankees", "Mets", "Angels", "Dodgers", "Cubs", "White Sox", "Blue Jays",
                   "Giants", "Nationals", "Phillies", "Red Sox", "Rangers", "Braves", "Astros", "Mariners", "Cardinals")
small.markets <- c("Twins", "Diamondbacks", "Rays", "Tigers", "Rockies", "Marlins", "Orioles", "Padres", "Guardians", "Pirates", 
                   "Royals", "Reds", "Brewers", "Athletics")
small.markets.o <- c("Twins", "Diamondbacks", "Rays", "Tigers", "Rockies", "Marlins", "Orioles", "Padres", "Guardians", "Pirates", 
                   "Royals", "Reds", "Brewers", "Athletics")

# Filter accuracy data for large markets
large.market.accuracy <- accuracy.table %>%
  filter(Team_name %in% large.markets)

# Filter accuracy data for small markets
small.market.accuracy <- accuracy.table %>%
  filter(Team_name %in% small.markets)

# Filter accuracy data for small markets without the Cardinals
small.market.o.accuracy <- accuracy.table %>%
  filter(Team_name %in% small.markets.o)

# Merge accuracy data with team performance data for large markets
merged.large.accuracy <- merge(large.market.accuracy, team.performance, by = "Team_name", all = FALSE)

# Plot large market accuracy
plot(merged.large.accuracy$Accuracy, merged.large.accuracy$PerfPts, 
     main = "Large Market Accuracy", 
     xlab = "Top Free Agent Accuracy", ylab = "Team Performance Points")

# Fit Regression to Scatter plot
fit <- lm(merged.large.accuracy$PerfPts ~ merged.large.accuracy$Accuracy)

# Add regression line to plot
abline(fit, col = "red")

# Calculate correlation coefficient
correlation <- cor(merged.large.accuracy$Accuracy, merged.large.accuracy$PerfPts)
print(paste("LMA Correlation coefficient:", correlation))

# Merge accuracy data with team performance data for small markets
merged.small.accuracy <- merge(small.market.accuracy, team.performance, by = "Team_name", all = FALSE)

# Plot small market accuracy
plot(merged.small.accuracy$Accuracy, merged.small.accuracy$PerfPts, 
     main = "Small Market Accuracy", 
     xlab = "Top Free Agent Accuracy", ylab = "Team Performance Points")

# Fit Regression to Scatter plot
fit <- lm(merged.small.accuracy$PerfPts ~ merged.small.accuracy$Accuracy)

# Add regression line to plot
abline(fit, col = "red")

# Calculate correlation coefficient
correlation <- cor(merged.small.accuracy$Accuracy, merged.small.accuracy$PerfPts)
print(paste("SMA Correlation coefficient:", correlation))

# Merge accuracy data with team performance data for small markets without the Cardinals
merged.small.o.accuracy <- merge(small.market.o.accuracy, team.performance, by = "Team_name", all = FALSE)

# Plot small market accuracy without the Cardinals
plot(merged.small.o.accuracy$Accuracy, merged.small.o.accuracy$PerfPts, 
     main = "Small Market Accuracy W/O STL", 
     xlab = "Top Free Agent Accuracy", ylab = "Team Performance Points")

# Fit Regression to Scatter plot
fit <- lm(merged.small.o.accuracy$PerfPts ~ merged.small.o.accuracy$Accuracy)

# Add regression line to plot
abline(fit, col = "red")

# Calculate correlation coefficient
correlation <- cor(merged.small.o.accuracy$Accuracy, merged.small.o.accuracy$PerfPts)
print(paste("SMA W/o STL Correlation coefficient:", correlation))

# Filter count data based on market size
large.market.counts <- merged.count.performance %>%
  filter(Team_name %in% large.markets)
small.market.counts <- merged.count.performance %>%
  filter(Team_name %in% small.markets)
small.market.o.counts <- merged.count.performance %>%
  filter(Team_name %in% small.markets.o)

# Plot for large markets
plot(large.market.counts$Count, large.market.counts$PerfPts, 
     main = "Free Agent Count (Large Markets)", 
     xlab = "Top Free Agent Count", ylab = "Team Performance Points")
fit_large <- lm(large.market.counts$PerfPts ~ large.market.counts$Count)
abline(fit_large, col = "red")
correlation_large <- cor(large.market.counts$Count, large.market.counts$PerfPts)
print(paste("Correlation coefficient (Large Markets):", correlation_large))

# Plot for small markets
plot(small.market.counts$Count, small.market.counts$PerfPts, 
     main = "Free Agent Count (Small Markets)", 
     xlab = "Top Free Agent Count", ylab = "Team Performance Points")
fit_small <- lm(small.market.counts$PerfPts ~ small.market.counts$Count)
abline(fit_small, col = "red")
correlation_small <- cor(small.market.counts$Count, small.market.counts$PerfPts)
print(paste("Correlation coefficient (Small Markets):", correlation_small))

# Plot for small markets without Cardinals
plot(small.market.o.counts$Count, small.market.o.counts$PerfPts, 
     main = "Free Agent Count versus Team Performance (Small W/O STL)", 
     xlab = "Top Free Agent Count", ylab = "Team Performance Points")
fit_small <- lm(small.market.o.counts$PerfPts ~ small.market.o.counts$Count)
abline(fit_small, col = "red")
correlation_small <- cor(small.market.o.counts$Count, small.market.o.counts$PerfPts)
print(paste("Correlation coefficient (Small W/O STL):", correlation_small))

library(gt)
library(magrittr)

poster.data$Contract <- round(poster.data$Contract, digits = 0)
poster.data$`Net Value`<- round(poster.data$`Net Value`, digits = 0)

# Sort dataframe by Score column
poster.data <- poster.data[order(-poster.data$`Net Value`), ]

# Keep top 5 and bottom 5 rows based on Score
poster.data1 <- rbind(poster.data[1:8, ])
poster.data2 <- rbind(poster.data[(nrow(poster.data)-7):nrow(poster.data), ])

best.values = gt(data = poster.data1) %>%
  tab_header(
    title = "Best Free Agent Values 2010-2019",
  )

worst.values = gt(data = poster.data2) %>%
  tab_header(
    title = "Worst Free Agent Values 2010-2019",
  )

# Export the gt table to a PDF file
gtsave(best.values, "best_values.png")
gtsave(worst.values, "worst_values.png")
