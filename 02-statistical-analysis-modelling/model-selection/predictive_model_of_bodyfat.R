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
setwd("~/BSc_UZH/UZH_22FS/BIO144/datasets-master")

dd <- read.csv('bodyfat.csv', stringsAsFactors = T)
dd <- read_delim('bodyfat.clean.txt')


# a posteriori variable selection is after collecting data
# select a set of variables that gives us the best predictive power
# attention overfitting if choosing to many variables, shitty if to few
# AIC to find out what predicts best

# set na action to fail, protecting us from bad things happening

options(na.action='na.fail')
# prevents fitting models with different number of values

dd <- dplyr::select(dd, bodyfat, age, weight, height, bmi, neck, chest,
             abdomen, hip, thigh, knee, ankle, biceps)

## start with the full model

m1 <- lm(bodyfat ~ ., data = dd) # dot means everthing else than response v
AICc(m1) # AIC corrected, goal is now to trim down the model

dropterm(m1, sorted = T) # takes m1 and fits a new model, with 1 term removed and saves result, each model will have one variable missing, saves each model
# doesn't gives AICc we have to square  AIC to get AICc

dt1 <- update(m1, . ~ . - knee)

AICc(dt1) # removing knee lowered AIC by 2 units
dropterm(dt1, sorted = T)

# remove age

dt2 <- update(dt1, . ~ . - age)
AICc(dt2)
dropterm(dt2, sorted = T)

# remove biceps

dt3 <- update(dt2, . ~ . - biceps)
AICc(dt3)
dropterm(dt3, sorted = T)

# remove chest

dt4 <- update(dt3, . ~ . - chest)
AICc(dt4)
dropterm(dt4, sorted = T)

# remove ankle

dt5 <- update(dt4, . ~ . - ankle) # dont remove intercepts
AICc(dt5)
dropterm(dt5, sorted = T)

# remove height

dt6 <- update(dt5, . ~ . - height)
AICc(dt6)
dropterm(dt6, sorted = T)

# remove bmi

dt7 <- update(dt6, . ~ . - bmi)
AICc(dt7)
dropterm(dt7, sorted = T)

# remove hip

dt8 <- update(dt7, . ~ . - hip)
AICc(dt8)
dropterm(dt8, sorted = T)

# remove thight

dt9 <- update(dt8, . ~ . - thigh)
AICc(dt9)
dropterm(dt9, sorted = T)

# remove neck

dt10 <- update(dt9, . ~ . - neck)
AICc(dt10)
dropterm(dt10, sorted = T)

# remove weight

dt11 <- update(dt10, . ~ . - weight)
AICc(dt11)
dropterm(dt11, sorted = T) # big decrease, see that in high sum of squares above

# remove abdomen

dt12 <- update(dt11, . ~ . - abdomen)
AICc(dt12)
dropterm(dt12, sorted = T)

# compare the different models we created

models <- list(m1=m1,df1=dt1,dt2=dt2,dt3=dt3,dt4=dt4,dt5=dt5,
               dt6=dt6,dt7=dt7,dt8=dt8,dt9=dt9,dt10=dt10,dt11=dt11,dt12=dt12)

model.sel(models)
# each row is a model, delta shows difference in AIC to best model(delta = 0)

## the computer can do the steps above for us

fit1 <- m1 # full model
fit2 <- lm(bodyfat ~ 1, dd) # only intercept

step.forward <- stepAIC(fit2, direction = 'forward',
                        scope = list(upper = fit1, lower = fit2))

# forward from simplest to full model


step.backward <- stepAIC(m1, direction = 'backward',
                        scope = list(upper = fit1, lower = fit2))

# backwards from full to simlest

step.both <- stepAIC(m1, direction = 'both',
                        scope = list(upper = fit1, lower = fit2))

# dropping and putting back in
## each of them return according optimal model

## compare the models again

models1 <- list(step.forward = step.forward, step.backward = step.backward,
            step.both = step.both)

model.sel(models1) # compares

# model forward has gives best AIC

## every possible combination of variables predicting bodyfat

s1 <- dredge(m1) # should be used with great care, creates lots of model

model.sel(get.models(s1, subset = delta < 1))# search for models under criteria

model.sel(get.models(s1, subset = delta < 2))

best_dredge <- get.models(s1, subset = delta == 0) # return best dredge model

best_models <- list(m1=m1, dt10=dt10, sforth = step.forward,
                    sback = step.backward, sboth = step.both,
                    best_dredge = best_dredge[[1]]) # attention we need to use index

model.sel(best_models)

# look at how good the model predictions are

p1 <- data.frame(dt10=predict(dt10),
                 dt11=predict(dt11)) # dataframe for plotting

dd1 <- cbind(dd, p1)  # facilitates the plotting

ggplot(data = dd1, mapping = aes(x=dt10, y=bodyfat)) +
  geom_point() # compares prediction with actual values

# compare to worse model

ggplot(data = dd1, mapping = aes(x=dt11, y= bodyfat)) +
  geom_point()

# bigger spread when look at eg the 20% bodyfast xaxis, prediction is worse
# scatter like this is very useful to get grounded again in data
# and understanding the variation


       