library(baseballr)

# Import Batter free agents
fa.data <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_FA_DATA_LARGE.csv")
# Import All Star Data
as.data <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_ALL_STAR_08-19.csv")

# Batter Export Matrix
column_names <- c("Name", "POS", "AGE", "YRS", "DOLLARS", "YEAR", "G", "R", "HR", "RBI", "BB", "SB", "HITS", "AS")
export.batters <- data.frame(matrix(ncol = length(column_names), nrow = 0))
colnames(export.batters) <- column_names

# Pitcher Export Matrix
column_names <- c("NAME", "POS", "AGE", "YRS", "DOLLARS", "YEAR", "G", "GS", "IP", "SV", "WERA", "WWHip", "SO9", "SO","W", "AS")
export.pitchers <- data.frame(matrix(ncol = length(column_names), nrow = 0))
colnames(export.pitchers) <- column_names

# Batter Data Import
b_pd_2010 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_08-10.csv")
b_pd_2011 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_09-11.csv")
b_pd_2012 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_10-12.csv")
b_pd_2013 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_11-13.csv")
b_pd_2014 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_12-14.csv")
b_pd_2015 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_13-15.csv")
b_pd_2016 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_14-16.csv")
b_pd_2017 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_15-17.csv")
b_pd_2018 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_16-18.csv")
b_pd_2019 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_data_17-19.csv")

# Pitcher Data Import
p_pd_2010 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2008-2010.csv")
p_pd_2011 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2009-2011.csv")
p_pd_2012 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2010-2012.csv")
p_pd_2013 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2011-2013.csv")
p_pd_2014 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2012-2014.csv")
p_pd_2015 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2013-2015.csv")
p_pd_2016 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2014-2016.csv")
p_pd_2017 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2015-2017.csv")
p_pd_2018 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2016-2018.csv")
p_pd_2019 <- read.csv("C:/Users/Owner/OneDrive/Documents/individualProjects/OSU/MLB_pitcher_data_2017-2019.csv")

batter.dfs <- list(b_pd_2010, b_pd_2011, b_pd_2012, b_pd_2013, b_pd_2014, b_pd_2015, b_pd_2016, b_pd_2017, b_pd_2018, b_pd_2019)
pitcher.dfs <- list(p_pd_2010, p_pd_2011, p_pd_2012, p_pd_2013, p_pd_2014, p_pd_2015, p_pd_2016, p_pd_2017, p_pd_2018, p_pd_2019)

# Begin Combination
for(i in 1:nrow(fa.data)){
  player <- fa.data[i,]
  name <- player$PLAYER
  position <- player$POS
  year <- player$Year
  
  if((position == "SP") || (position == "RP")){
    year.composed <- year - 2009
    df <- pitcher.dfs[[year.composed]]
    
    found <- TRUE
    for(j in 1:nrow(df)){
      player.df <- df[j,]
      if(player.df$Name == name){
        
        all.star <- 0
        for(k in 1:nrow(as.data)){
          if((as.data[k,]$Name == name) && ((as.data[k,]$Year - year) < 3)){
            all.star = all.star + 1
          }
        }
        
        export.player <- c(name, position, player$AGE, player$YRS, player$DOLLARS, year, player.df$G, player.df$GS, player.df$IP, player.df$SV, player.df$WEra, player.df$WWhip, player.df$SO9, player.df$SO, player.df$W, all.star)
        export.pitchers <- rbind(export.pitchers, export.player)
        found <- FALSE
        break;
      }
    }
  }
  else{
    year.composed <- year - 2009
    df <- batter.dfs[[year.composed]]
    
    found <- TRUE
    for(j in 1:nrow(df)){
      player.df <- df[j,]
      if(player.df$Name == name){
        
        all.star <- 0
        for(k in 1:nrow(as.data)){
          if((as.data[k,]$Name == name) && (abs(as.data[k,]$Year - year) < 3) && ((as.data[k,]$Year - year) < 1)){
            all.star = all.star + 1
          }
        }
        export.player <- c(name, position, player$AGE, player$YRS, player$DOLLARS, year, player.df$G, player.df$R, player.df$HR, player.df$RBI, player.df$BB, player.df$SB, player.df$H, all.star)
        export.batters <- rbind(export.batters, export.player)
        found <- FALSE
        break;
      }
    }
    if(found){
      cat(name, as.integer(year), "\n")
    }
  }
}

column_names <- c("NAME", "POS", "AGE", "YRS", "DOLLARS", "YEAR", "G", "GS", "IP", "SV", "WERA", "WWHip", "SO9", "SO","W", "AS")
colnames(export.pitchers) <- column_names

column_names <- c("Name", "POS", "AGE", "YRS", "DOLLARS", "YEAR", "G", "R", "HR", "RBI", "BB", "SB", "HITS", "AS")
colnames(export.batters) <- column_names

write.csv(export.batters, "batter_export.csv", row.names = FALSE)
write.csv(export.pitchers, "pitcher_export.csv", row.names = FALSE)
