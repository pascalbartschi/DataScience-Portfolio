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
library('boot')

# load data

setwd("~/BSc_UZH/UZH_22FS/BIO144/all_datasets_144")
# setwd("~/BSc_UZH/UZH_22FS/BIO144/datasets-master")
data <- read.csv('echocardiogram.csv', na.strings = c('?'))
#dd <- read_delim('bodyfat.clean.txt')

# glimpse

glimpse(data)
#glimpse(dd)

# omit na values

data <- na.omit(data)

names(data) <- c("survival", "still_alive", "age_at_heart_attack", "pericardial_effusion",
                      "fractional_shortening", "epss",
                      "lvdd", "wall_motion_score", 
                      "wall_motion_index", "mult",
                      "name",
                      "group",
                      "alive_at_1")

glimpse(data)

data <- dplyr::select(data, -name)

glm1 <- glm(alive_at_1 ~ fractional_shortening+
              epss+
              lvdd+
              wall_motion_index+
              pericardial_effusion, data= data, family = binomial, na.action = 'na.fail')

model_dredge <- dredge(glm1)
best_dredge <- get.models(model_dredge, subset = delta == 0)[[1]] # indexing gives only model, double indexing to index inside of list

# perform a chisq

anova(best_dredge, test = 'LRT')
summary(best_dredge) # 59.63 deviance left

# show predcitions

ggplot(data, aes( x = wall_motion_index, y = alive_at_1)) +
  geom_point(position=position_jitter(height=0.1, width=0), alpha=0.5)+ # jitter creates distance inbetween points
  stat_smooth(method="glm", method.args=list(family="binomial")) + # fitted binom line of glm1
  theme_bw()

anova(glm1, test = 'Chisq')

