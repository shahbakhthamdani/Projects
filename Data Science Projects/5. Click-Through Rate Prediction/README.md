# Click-Through Rate Prediction

## Topics Covered

- Pyspark
- Parallel Computing
- Exploratory Data Analysis
- Classification
- Logistic Regression
  
## 0. Links

[Project Notebook](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/5.%20Click-Through%20Rate%20Prediction/Click-Through%20Rate%20Prediction.ipynb)

## 1. Overview

The goal of our analysis is to predict the Click-Through Rate (CTR) on a large set of Criteo Advertising Data. This is motivated because a lot of commerce is conducted digitally these days, and advertisements play an important part in that landscape. There are two stakeholders when it comes to CTR: the publishers (those that provide a platform where an advertisement appears) and advertisers (those that are looking to place their advertisement on any platform). CTR measures how many users click on a certain advertiser's advertisement that is displayed on a certain publisher's platform. Measuring this on a large scale gives the average click-through rate.

This kind of analysis is done in order to measure the effectiveness of advertisements and its accompanying features (shape, size, placement on page, even content, etc.). It also tells about the demographics and characters of the the sort of users that click on a certain ad, and hence that information is valuable to the advertisers. It also enables publishers to get a firm grip on their strength as a platform and charge appropriate money for their services. Hence, CTR serves a very important role in the current E-commerce landscape, for both stakeholders. It also serves as a bouncing off point for other analyses involving CTR such as Cost-per-Click (CPC) and Cost-per-Conversion (CPA).

## 2. Data

The dataset at our disposal has the following properties: it consists of 13 integer columns and 26 categorical columns, all of which have been masked for anonymity. There is a column for label, 0 or 1, that dictates whether an ad was clicked or not. There are about 45 million rows in the dataset, which cover a period of 7 days on Criteo's platform. Hence, we need our model to be highly parallizeable and scalable if we want any sort of working, effective solution. The inherent limitation of this dataset is that all the features are masked. This leads to a certain loss of interpretability, because even if our model performance is high, we might not be able to talk about what features exactly play a part in achieving that. Also, our labels are unbalanced: one class (ad not clicked) is overrepresented (even though subsampling techniques have been applied when getting the data).

## 3. Conclusion

The implementation of logistic regression with and without regularization revealed the importance of parallelization as well as the value of the application of best practices such as broadcasting variables and cacheing RDDs to solve problems on big data. In particular, the statistical analysis of a dataset with as many rows and columns as this one would be impossible on most single node computers. However, by defining the problem as the embarrassingly parallel task of fitting the logistic model through gradient descent it is possible to use a cluster with commoditized hardware to obtain a solution. Nevertheless, the implementation of the model on Spark provided several challenges.

First, the size of the RDDs made it crucial to be judicious on how and where to cache in order to avoid depleting our resources.

Second, broadcasting variables so that workers had them ready to perform their jobs was paramount for better performance, however, this meant that we sometimes had to depart from functional programming best practices. For example, we created three prediction functions (one for each model: logistic, logistic with ridge regularization, and logistic with lasso regularization) in order to guarantee the broadcasting of the proper weights to each function.

Third, some of the features we commonly use locally on Python are not designed to work on a cluster, therefore, we had to define functions that provided metrics such as the accuracy and f1 scores. Moreover, while we were able to obtain solutions for our models, the jobs took a considerable amount of time to be completed which prevented us from having a more robust size of iterations of the gradient descent algorithm or to fine-tune the regularization hyper-parameter.

Finally, the results highlighted the importance of defining the adequate objective metric in a project. In particular, in the prediction of CTR rates it is much more important to detect those consumers that will actually click-through (true positives) than those who won't (true negatives) given that the former are the ones of who provide the revenue for ad agencies and advertisers. Therefore, while we could have obtained a better accuracy by simply predicting each observation as 0 (no click-through), our model is better suited to detect those consumers that matter the most to Criteo.
