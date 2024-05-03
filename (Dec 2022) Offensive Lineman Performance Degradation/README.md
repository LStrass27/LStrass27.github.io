# Tracking Offensive Lineman Performance Degradation (Big Data Bowl)

For the 2022 Big Data Bowl I sought to see if there existed a pattern between Offensive Lineman performance throughout the game based upon their age. For instance, does a older veteran player perform well at the start of games but struggle as games go along due to fatigue. Or does a younger player perform poorly at the beginning of games but perform better once they get used to coverages. This was my hypothesis going in that age would have a direct relationship with younger players getting better as a game went along and older players struggling more. Ultimately, I found that younger lineman play at the same level throughout a game, but older lineman struggle more as the game gets longer. 

Note: This was my first major programming project. I had about 2 months of coding experience which explains why some of the code is messy in some areas.

**bdb.py:** The main function that does the analysis for the project. This program reads in all the provided big data bowl files, and stores the data in class objects for Players and Plays. Also classifies player performance and outputs the results in bdb-fatigue.csv.  
**bdb-fatigue.csv:** Output file of bdb.py. Shows each offensive linemans play by play success throughout a specific week. Used as input in final_bdbr.r.  
**final_bdbr.r:** File that completes the Performance Degradation analysis of an Offensive Lineman throughout the game. Creates plots and uses t-tests.  
**games.csv:** Data with individual game data. Provided by Big Data Bowl  
**pffScoutingData:** Data with Pro Football Focus (PFF) advanced data for each play. Provided by Big Data Bowl.  
**players.csv:** Data with player personal information. Used to initialize Player class objects. Provided by Big Data Bowl.  
**plays.csv:** Data with individual play outcomes and player responses. Provided by Big Data Bowl.