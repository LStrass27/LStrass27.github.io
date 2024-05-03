library(baseballr)

data <- read.csv("C:/Users/Owner/OneDrive/Documents/GitHub/big_data_bowl/DynastySimulator/MLB_FA_DATA_BATTERS.csv")

column_names <- c("First_name", "Last_name", "POS", "AGE", "YRS", "DOLLARS", "YEAR", "G", "R", "HR", "RBI", "BB", "SB", "HITS")

export <- data.frame(matrix(ncol = length(column_names), nrow = 0))
colnames(export) <- column_names

pd_2009 <- bref_daily_pitcher(t1 = "2007-01-01", t2 = "2009-12-31")
pd_2010 <- bref_daily_pitcher(t1 = "2008-01-01", t2 = "2010-12-31")
pd_2011 <- bref_daily_pitcher(t1 = "2009-01-01", t2 = "2011-12-31")
pd_2012 <- bref_daily_pitcher(t1 = "2010-01-01", t2 = "2012-12-31")
pd_2013 <- bref_daily_pitcher(t1 = "2011-01-01", t2 = "2013-12-31")
pd_2014 <- bref_daily_pitcher(t1 = "2012-01-01", t2 = "2014-12-31")
pd_2015 <- bref_daily_pitcher(t1 = "2013-01-01", t2 = "2015-12-31")
pd_2016 <- bref_daily_pitcher(t1 = "2014-01-01", t2 = "2016-12-31")
pd_2017 <- bref_daily_pitcher(t1 = "2015-01-01", t2 = "2017-12-31")
pd_2018 <- bref_daily_pitcher(t1 = "2016-01-01", t2 = "2018-12-31")
pd_2019 <- bref_daily_pitcher(t1 = "2017-01-01", t2 = "2019-12-31")

tables <- list(pd_2009, pd_2010, pd_2011, pd_2012, pd_2013, pd_2014, pd_2015, pd_2016, pd_2017, pd_2018, pd_2019)

for(i in 1:length(tables)){
  size <- nrow(tables[[i]])  # Accessing the data frame from the list using double square brackets
  WEra <- rep(0, size)
  WWhip <- rep(0, size)
  for(j in 1:size){
    ind.WEra <- tables[[i]][j, "ERA"] / (tables[[i]][j, "IP"] / 500)  # Accessing columns by name
    ind.WWhip <- ((tables[[i]][j, "H"] + tables[[i]][j, "BB"]) / tables[[i]][j, "IP"]) / (tables[[i]][j, "IP"] / 500)  # Accessing columns by name
    WEra[j] <- ind.WEra
    WWhip[j] <- ind.WWhip
  }
  WEra <- unlist(WEra)
  WWhip <- unlist(WWhip)
  
  tables[[i]]$WEra <- WEra
  tables[[i]]$WWhip <- WWhip
}

print(tables[[i]])

start_year <- 2007
end_year <- 2009

for (i in 1:length(tables)) {
  if (!is.data.frame(tables[[i]])) {
    warning(paste("Element", i, "is not a data frame and will be skipped."))
    next  # Skip to the next iteration if the element is not a data frame
  }
  
  table <- as.data.frame(tables[i])
  year_start <- start_year + i - 1
  year_end <- end_year + i - 1
  file_name <- sprintf("MLB_pitcher_data_%02d-%02d.csv", year_start, year_end)
  write.csv(table, file_name, row.names = FALSE)
}
