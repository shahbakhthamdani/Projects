# Reducing Crime: A Regression Analysis Study

## Topics Covered

- Regression
- Statistical Inference and Causality Analysis
- Data Cleaning and Transformation
- Exploratory Data Analysis
- Telling stories with data

## 0. Links

[Project Report](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/3.%20Crime%20Rate%20Regression%20Analysis/Crime%20Rate%20in%20North%20Carolina.pdf)

## 1. Overview

Providing a safe environment for American citizens and their families is one of the foremost obligations of any public servant, especially local authorities. With this in mind, it is imperative to have a working understanding of which factors are drivers for crime rates. This particular project is specific to the State of North Carolina, in 1987. Once these determinants of crime are identified, quantified, and ordered in importance via statistic modelling, it will be possible to effect significant changes to improve security by creating policies to address these factors. This project will study a wide variety of economic, judicial, and demographic variables, devoting a special focus on the variables that are most actionable from a public policy perspective.

## 2. Model Interpretation

The final model relfects that the two economic metrics, mainly measured through wages, and law enforcement variables were both significant determinants of crime rate in North Carolina in 1987. Most importantly from a public policy perspective, we see a negative relationship between the crime rate and the probability of arrest and conviction. Namely, an increase of 0.1 in the probability of arrest will lead to a decrease of 18.96% in the crime rate. In addition, an increase of 0.1 in the probability of conviction will reduce the crime rate by 9.95%.

On the other hand, we see that both the tax revenue per capita and the weekly wage for federal employees have a positive relationship with crime rate. More specifically, a 1 dollar increase in tax revenue leads to an expected increase of 0.9% in the crime rate while a 1 dollar increase in the weekly wage for federal workers leads, in average, to a 0.4% increase in crime rate. While this might be counter-intuitive at first, this could be caused by the fact that richer counties have more and better payed federal employees leading to larger inequalties in the population which could be increasing the crime rate (it is important to mention that the weekly wages for federal employees were usually the largest one of all the wages in the dataset). Also, the relationship between the weekly federal wage and the increased crime rate could be caused by a confounding effect where counties with larger crime problems receive more help from federal law-enforcement agencies. Moreover, we note that there is a negative relationship between the weekly wage of the service industry and the crime rate, where a 1 dollar increase in this wage leads to a reduction of 0.2% in the crime rate. Finally, it is important to mention that this model can explain roughly two-thirds of the variance in the log of the crime rate (R2 = 0.641) and has the best fit in terms of AIC and R2 adjusted values with 58.7 and 0.619 respectively.

## 3. Conclusion

The above discussion including EDA, model building and omitted variables show that it is a highly complicated
task predicting crime rate in a certain area, and there are a number of socio-economic and law enforcement
factors involved that influence the predictive power of this variable.

However a general trend is that the most effective and actionable variables at reducing the crime rate are a high probability of arrest and conviction. Therfore in order to prevent future crime, it is recommended to
channel sufficient resources to improve the criminal system to make sure that once a crime is committed the
perpetrator is arrested at high rates and that once they are arrested, they are actually convicted. This
means that work needs to be done to make police enforcement agencies better at capturing criminals and the
prosecution better at convicting guilty criminals. An additional economic variable that can help control the
crime rate are the wages, in particular for the service industry. Therefore, a better criminal system together with economic factors for the population such as better living wages for residents are likely to lead to reduced crime rates.
