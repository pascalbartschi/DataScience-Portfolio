# clear brain

rm(list= ls())

# import of libraries
library("ggplot2")
library("dplyr")
library("ggfortify")
library('tidyverse')
library('GGally')
library('MASS')
library('readr')
library('MuMIn')

# load data

setwd("~/BSc_UZH/UZH_22FS/BIO144/all_datasets_144")
# setwd("~/BSc_UZH/UZH_22FS/BIO144/datasets-master")
data <- read.csv('abalone_age.csv', stringsAsFactors = T)
# dd <- read_delim('bodyfat.clean.txt')

glimpse(data)

# distribution of response v Rings

ggplot(data = data, mapping = aes(x=Rings)) +
  geom_histogram()

options(na.action = 'na.fail')

fullm <- glm(Rings ~ ., data = data, family = poisson(link = log))
autoplot(fullm)
AICc(fullm)

# removing always one variable at a time to see which one have which influence

dropterm(fullm, sorted = T) # none states AIC when nothing is removed

# increase in RSS from none to removal of lenth in mm

dropterm(fullm, sorted = T)[1,3] - dropterm(fullm, sorted = T)[3,3]

# change in adjusted r-squared value

r2fullm <- as.numeric(summary(fullm)[9]) # index 9 is adjusted R squared
AICc(fullm)

m_len <- update(fullm, . ~ . - Length_mm)

r2m_len <- as.numeric(summary(m_len)[9])
AICc(m_len)

round(r2fullm - r2m_len, 2)

######################################################################################
# removal of variables, one by one until there is to big AIC chamnge(> 4 untits)

m_shellw <- update(m_len,  .~. -Shell_weight_g)
AICc(m_shellw)

dropterm(m_shellw, sorted = T)

m_height <- update(m_shellw, .~. -Height_mm)
AICc(m_height)

dropterm(m_height, sorted = T)

m_Viscera <- update(m_height, .~. -Sex -Viscera_weight_g)
AICc(m_Sex)

bestmanual <- m_Viscera

dropterm(bestmanual, sorted = T)

# what is the dispersion ratio of residuals of the bestmanual model

anova(bestmanual)
round((summary(bestmanual)$deviance / summary(bestmanual)$df.residual), 2)

# --> model is under dispersed, lets the try the quasipoisson family
################################################

quasim <- glm(Rings ~ Diameter_mm + Whole_weight_g + Shuck_weight_g, data = data, family = quasipoisson)

round((summary(quasim)$deviance / summary(quasim)$df.residual), 2)

# doesn't make any difference at all :(
