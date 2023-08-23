## Description

Here you can find analysis using various regression approaches such as linear and multiple linear models, generalized linear models and linear mixed models.

## Contents

* [GLM & LMM](glm+lmm/): GLMs with the poission and binomial link function, as well one LLM implemented in R.
  - [LMM_politeness.rmd](glm+lmm/LMM_politeness.rmd) analyses what explanatory variables may be used to predict and understand our voice frequency
  - [GLM_poisson_soaysheepfitness.rmd](glm+lmm/GLM_poisson_soaysheepfitness.rmd) using the logit link function in a glm to analyse predictors for the fertility of soay sheep.
  - [GLM_binomial_pesticides.rmd](glm+lmm/GLM_binomial_pesticides.rmd) uses the binmial family link in a glm to find how different pesticides affect an insect.
* [Linear Regression](linear-regression/): Linear and multiple regression implemented in python and R, as well as outlier analysis.
  - [migrating_birds.ipynb](linear-regression/migrating_birds.ipynb) analyses the relationship of bird features with their migrating distance in winter.
  - [LM_dicrete_earthworm.rmd](linear-regression/LM_dicrete_earthworm.rmd) finds different relationships between distinguished earthworm species of weight with gut circumference.
  - [LM_continuous_bodyfat.rmd](linear-regression/LM_continuous_bodyfat.rmd) explores which features of human physique can predict bodyfat.
  - [outlier-leverage.ipynb](liner-regression/outlie-leverage.ipynb) simplistic search for outliers and leverage point and how to handle them accordingly
* [Model Selection](model-selection): Performing model selection of linear model (lm) in R according to AIC.
  - [predicitve_model_of_bodyfat.R](model-selection/predicitve_model_of_bodyfat.R): manual model selection by stepwise dropping of explanatory variables according to AIC to obtain optimal model to predict bodyfat.
  -[model-dredge-echocardiogram.rmd](model-selection/model-dredge-echocardiogram.rmd): automated model selection with the `dredge` function from the "MuMIn" package to predict the probability to survide heart attacks
