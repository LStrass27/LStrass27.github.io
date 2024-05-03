library(readr)
library(dplyr)

oline_fatigue <- read_csv("bdb-fatigue.csv")

age23bel = subset(oline_fatigue, age <= 23)
age23bel = subset(age23bel, select = -c(name, age, position, height,weight, college, week,`80`))

age24 = subset(oline_fatigue, age == 24)
age24 = subset(age24, select = -c(name, age, position, height,weight, college, week,`80`))

age25 = subset(oline_fatigue, age == 25)
age25 = subset(age25, select = -c(name, age, position, height,weight, college, week,`80`))

age26 = subset(oline_fatigue, age == 26)
age26 = subset(age26, select = -c(name, age, position, height,weight, college, week,`80`))

age27 = subset(oline_fatigue, age == 27)
age27 = subset(age27, select = -c(name, age, position, height,weight, college, week,`80`))

age28 = subset(oline_fatigue, age == 28)
age28 = subset(age28, select = -c(name, age, position, height,weight, college, week,`80`))

age29 = subset(oline_fatigue, age == 29)
age29 = subset(age29, select = -c(name, age, position, height,weight, college, week,`80`))

age30 = subset(oline_fatigue, age == 30)
age30 = subset(age30, select = -c(name, age, position, height,weight, college, week,`80`))

age31up = subset(oline_fatigue, age >= 31)
age31up = subset(age31up, select = -c(name, age, position, height,weight, college, week,`80`))

is.data.frame(age23bel)
is.data.frame(age24)
is.data.frame(age25)
is.data.frame(age26)
is.data.frame(age27)
is.data.frame(age28)
is.data.frame(age29)
is.data.frame(age30)
is.data.frame(age31up)

age23bel_av = colMeans(age23bel, na.rm = TRUE)
age24_av = colMeans(age24, na.rm = TRUE)
age25_av = colMeans(age25, na.rm = TRUE)
age26_av = colMeans(age26, na.rm = TRUE)
age27_av = colMeans(age27, na.rm = TRUE)
age28_av = colMeans(age28, na.rm = TRUE)
age29_av = colMeans(age29, na.rm = TRUE)
age30_av = colMeans(age30, na.rm = TRUE)
age31up_av = colMeans(age31up, na.rm = TRUE)

is.numeric(age23bel_av)
is.vector(age23bel_av)


#Analysis
# Fail rate of age 23 and below at different times

summary(age23bel$"3")
summary(age23bel$"15")
summary(age23bel$"30")
# .1144, .1214, .1382 (Shows slight improvement)


# Fail rate of age 31 and above at different times

summary(age31up$"3")
summary(age31up$"15")
summary(age31up$"30")
# .05747, .1078, .1183 (Shows significant improvement)

# Testing significance of differences in failure among
# different age groups

t.test(age23bel$"3",age23bel$"30")
#CI (95%):(-.099,.052), t=-.618, p=.54
t.test(age24$"3",age24$"30")
#CI:(-.022,.124), t=1.378, p=.17
t.test(age25$"3",age25$"30")
#CI: (-.086,.083), t=-.038, p=.97
t.test(age26$"3",age26$"30")
#CI: (-.082,.100), t=.201, p=.84
t.test(age27$"3",age27$"30")
#CI: (-.093,.085), t=-.085, p=.93
t.test(age28$"3",age28$"30")
#CI: (-.076,.079), t=.042, p=.97
t.test(age29$"3",age29$"30")
#CI: (-.095,.068), t=-.323, p=.75
t.test(age30$"3",age30$"30")
#CI: (-.120,.034), t=-1.10, p=.27
t.test(age31up$"3",age31up$"30")
#CI: (-.136,.014), t=-1.60, p=.11

# Data Frame for Averages

averages_df = data.frame(age23bel_av,age24_av,age25_av,age26_av,age27_av,age28_av,age29_av,age30_av,age31up_av)
(averages_df$age23bel_av)

# Line graph for each age depicting fail rate by play number

plot(age23bel_av,type="p",xlab="Play Number",ylab="Fail Rate",main="Age 23 & Below")
plot(age24_av,type="p",xlab="Play Number",ylab="Fail Rate",main="Age 24")
plot(age25_av,type="p",xlab="Play Number",ylab="Fail Rate",main="Age 25")
plot(age26_av,type="p",xlab="Play Number",ylab="Fail Rate",main="Age 26")
plot(age27_av,type="p",xlab="Play Number",ylab="Fail Rate",main="Age 27")
plot(age28_av,type="p",xlab="Play Number",ylab="Fail Rate",main="Age 28")
plot(age29_av,type="p",xlab="Play Number",ylab="Fail Rate",main="Age 29")
plot(age30_av,type="p",xlab="Play Number",ylab="Fail Rate",main="Age 30")
plot(age31up_av,type="p",xlab="Play Number",ylab="Fail Rate",main="Age 31 & up")

