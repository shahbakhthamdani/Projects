# Bot or Not: Bot Detection Classifier

## Topics Covered

- Exploratory Data Analysis (EDA)
- Data Preprocessing and Feature Engineering
- Classification Methods
  - Logistic Regression
  - Support Vector Machines
  - Random Forest

## 0. Links

[Project Notebook](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/6.%20Bot%20Detection%20Classifier/Bot%20Detection.ipynb)

## 1. Overview

The present work is based on a Kaggle competition (<https://www.kaggle.com/c/facebook-recruiting-iv-human-or-bot/>) whose goal is to identify which users on an auction website are humans and which are bots based on their bidding history and other user features. The issue of bot detection is extremely relevant to auction websites, given that bots have become one of the main factors that have stifled the growth of auction sites over the past years by generating an unfair marketplace and damaging the consumer's trust on the site.

There are two main types of auction bots:

- Snipers: Bots specialized in bidding at the last possible instant of an auction to guarantee that their owner can't be outbid and securing the auction.
- Shills: Bots that engage in shill bidding which is the process of bidding continuously on the owner's own auction to inflate the price and make it seem more popular than it is.

While initially auction sites relied on user reports to manually verify if a user was a bot or not, this system wasn't scaleable, therefore, as these sites gained popularity worldwide it became important to automatize this process to make bot detection more affordable, proactive, and accurate. Nowadays most auction sites use a combination of humans and Machine Learning through a process in which algorithms detect possible bot activity which is confirmed by the site's employees.

Our goal in this project is to use a combination of feature engineering and Machine Learning methods to effectively predict bot activity in order to flag suspicious user activity for further review.

## 2. Data

The data is split into three files:

**bids.csv** contains information about more than 7,650,000 bids including:

- bid_id: Unique id for the bid
- bidder_id – Unique identifier of a bidder (same as the bidder_id used in train.csv and test.csv)
auction – Unique identifier of an auction
- merchandise – The category of the auction site campaign, which means the bidder might come to this site by way of searching for "home goods" but ended up bidding for "sporting goods" - and that leads to this field being "home goods". This categorical field could be a search term, or online advertisement.
- device – Phone model of a visitor
- time - Time that the bid is made (transformed to protect privacy).
- country - The country that the IP belongs to
- ip – IP address of a bidder (obfuscated to protect privacy).
- url - url where the bidder was referred from (obfuscated to protect privacy).
- payment_account – Payment account associated with a bidder. These are obfuscated to protect privacy.
- address – Mailing address of a bidder. These are obfuscated to protect privacy.

**train.csv** contains user-level information that links the bidder_id, payment account, address, and outcome (0 for human and 1 for bots). There are a total of 2013 users in the training set.

**test.csv** contains user-level information about the bidder_id, payment account, and address. There are a total of 4700 users in the test set which doesn't have the outcome variable as final accuracy is checked through kaggle.

Therefore, to predict whether a user is a bot or not it is necessary to match the bidder id in the test or training data set to the bids made by the same bidder id on the bids data set, aggregating all the user activity in the process.

## 3. Conclusion

The main takeaway from the project is the immense importance of feature selection on applied Machine Learning projects. While the model selection and parameter tuning can improve accuracy, generating and selecting the right features are essential for a successful predictive model. Furthermore, we learned that one of the main challenges of successful feature engineering is that a large amount of knowledge about the phenomenon under study is needed in order to generate the relevant features. In particular, we noticed that most contestants on the Kaggle competition used the same models (Random Forests were the most popular ones by far) but the difference in their rates of success came from the features they used.

Another important insight was how to deal with imbalanced data which increases the complexity of the models especially if one of the outcomes is much more important to predict than the other (in our case predicting robots). Specifically, unpenalized models tended to predict that all cases were human which lead to high accuracy rates (since 1910 cases of our training set were human out of 2013, predicting that all were human lead to an accuracy of 1910/2013 = 94.5%) but zero ability to predict bots. Therefore, through the use of penalized and balanced weighted models we were able to increase our model's ability to predict bot activity.

The relatively small size of the training set compared to the test set also helped us understand the value of cross validation and related procedures such as K Fold Cross Validation which can also help with the issues of imbalance (the folds are made to preserve the percentage of samples for each class for the cross validation). Nevertheless, the trade-off between additional training cases and a more robust test set with outcomes is something that needs to be evaluated on a case-to-case basis depending on the characteristics and objectives of the project.

Finally, the scale of the project made it clear to us the importance of parallel computing on practical applications of Machine Learning and the limitations that the processing power of consumer-grade computers at attempting large tasks. Reductions in the processing time obtained through parallel computing would have allowed us to experiment more with the features and models and could have helped us obtain better results.
