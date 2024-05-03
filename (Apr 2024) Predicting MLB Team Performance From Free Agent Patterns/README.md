# Predicting MLB Team Performance From Free Agent Patterns
MLB teams have become very stingy in giving out free agent contracts in the last 15 years. I sought to see if this concern was validated or whether teams should attempt to sign as many good free agents as possible. I used a team performance formula based on playoff success and regualar season win totals. Ridge/lasso regression models for hitters and pitchers to predict total expected contract value. Some of the predictors used were age, position, and player's counting stats the three seasons prior to their free agency. I then used these predicted salary outputs and compared it to the actual salaries, which gave me a classification of whether a contract was a good or bad deal for a team at a given time. Ultimately I discovered that Small Market teams concern should be justified, but for large market teams it is more about spending as much money as possible. I presented this project at the Ohio State Sports Analytics Conference and I go more in depth in the poster presentation **(OSU Presentation 2024)**

**MLB Free Agent Data:** Free Agent Data ranging from 2010-2023 used in the project. All from ESPN.  
**MLB Team Performance Data:** Team performance data used in the team performance metric. From BaseballReference.  
**Player Performance Data:** Hitter and Pitcher performance data scraped from baseball reference. Split up into chunks for the cumulative stats of a player over the three prior years. This was the range I used in the regression models to predict salary output.  
**Poster Pictures:** Supplemental images used in my poster presentation  
**batter_export.csv:** Modified csv to include all the predictor data used in the batter ridge regression model  
**FangraphsScrapeData.r:** Misleading in the name. Ended up being where I scraped the pitcher data for the project from Baseball Reference.  
**Lasso_Ridge.r:** Full model creation and data analysis of the project.  
**MLB_FA_Evaluation.r:** Test r file where I trained a bunch of different model types to see what the best predictors were for salary output to be used in Lasso_Ridge.r. I would do 100 random train/test draws to see which predictor models worked the best for hitters and pitchers. Hoped to remove some of the variability that could be caused by some of the very large contracts.  
**ModelCreation.r** Where I scraped the hitter data from baseball reference. I originally got the pitcher data the same way but found a better way to do it which is in FrangraphsScrapeData.r.  
**OSU Presentation 2024:** This is a .jpg image of my poster I presented at the 2024 Ohio State Sports Analytics Conference. The output of the project is explained in depth here.  
**pitcher_export.csv:** Modified csv to include all the predictor data used in the pitcher lasso regression model  
**SVR_model.py:** Another model I considered to predict the salary outputs was a Support Vector Regression model created using SciKit-Learn. This model was outperformed by both the ridge and lasso models, so it wasn't included in the final project.

