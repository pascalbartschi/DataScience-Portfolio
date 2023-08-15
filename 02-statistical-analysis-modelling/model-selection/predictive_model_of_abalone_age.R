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
#dd <- read_delim('bodyfat.clean.txt')

glimpse(data)

# distribution of response v Rings

ggplot(data = data, mapping = aes(x=Rings)) +
  geom_histogram()

options(na.action = 'na.fail')

fullm <- lm(Rings ~ ., data = data)
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

r2fullm - r2m_len


######################################################################################
# removal of variables, one by one until there is to big AIC chamnge(> 4 untits)

m_shellw <- update(m_len,  .~. -Shell_weight_g)
AICc(m_shellw)

dropterm(m_shellw, sorted = T)

m_height <- update(m_shellw, .~. -Height_mm)
AICc(m_height)

dropterm(m_height, sorted = T)

bestmanual <- m_height

################################################
# step models

m0 <- lm(Rings ~ 1, data)

step.forward <- stepAIC(m0, direction = 'forward',
                        scope = list(upper = fullm, lower = m0))

# forward from simplest to full model


step.backward <- stepAIC(fullm, direction = 'backward',
                         scope = list(upper = fullm, lower = m0))

# backwards from full to simlest

step.both <- stepAIC(fullm, direction = 'both',
                     scope = list(upper = fullm, lower = m0))

models <- list(fwd = step.forward, bwd = step.backward, both = step.both)

model.sel(models)

# use dredge

s1 <- dredge(fullm)

best_dredge <- get.models(s1, subset = delta < 5)

sum(!is.na(model.sel(best_dredge)[,2]))

View(model.sel(best_dredge))

          