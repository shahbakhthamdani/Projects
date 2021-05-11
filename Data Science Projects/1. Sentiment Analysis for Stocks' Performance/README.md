# Causal Analysis between Public and Market Sentiment: a Predictive Model for Individual Stock Performance

## 0. Links

[Project Paper](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/1.%20Sentiment%20Analysis%20for%20Stocks'%20Performance/Twitter%20Sentiment%20and%20Stock%20Market%20Behaviour.pdf)
[Data Profiling Notebook](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/1.%20Sentiment%20Analysis%20for%20Stocks'%20Performance/Data_Profiling.ipynb)
[Predictive Neural Network Model Notebook](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/1.%20Sentiment%20Analysis%20for%20Stocks'%20Performance/Neural_Network_Model.ipynb)
[Sentiment Classifier Notebook](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/1.%20Sentiment%20Analysis%20for%20Stocks'%20Performance/Sentiment_Classifier_Model.ipynb)

## 1. Overview

In this project, we tackle one of the most pursued task by hedge fund and asset managers: predicting stock prices. It’s been long said by economists that markets are efficient and follow a random path, therefore undermining any possibility of prices being predictable. Prices, indeed, discount all the information available for a particular stock, or index in real-time, and after major financial data is available to the public, Stocks and Indices are fed by positive, neutral and negative sentiment creating this ”random” fluctuation in price until a major announcement or, typically, the next earnings report creates a new trend.

Until recent years, this ”sentiment” was un-quantifiable, but with advancements in Natural Language Understanding (NLU), we are able to score statements on a scale of positivity and negativity. Our approach takes on sentiment analysis on Twitter and apply Deep Learning principles to find a correlation with the Top 50 Stocks in Market Cap. We will analyze our results from a Neural Network fed with a lag in prices and a lag of sentiment scores from March 2019. Unlike Bollen et al. (2010)’s paper, our work is applied directly to Stocks instead of Dow Jones Index. Apart from the predictive model, we will establish Granger-Causality and build a multivariate time-series regression equation between stock prices and sentiment scores.

## 2. Data

### Twitter Data

For our analysis, we utilized Twitter’s API to gather historical data. Our analysis was limited from 4th March 2019 to 29th March 2019. Twitter only allows free access to a limited number of days data, and after that period, it charges for each succeeding day. Moreover, our analysis was limited to S&P500 Top 50 companies. The final tally was 2,572,925 tweets over the entire period of interest
(4th March to 29th March).

### Stock Data

For the stock data, we simply gathered stock market, by ticker and aggregate, closing values for S&P500 Top 50 publicly available on the internet.

## 3. Sentiment Analysis

For sentiment analysis of tweets in our dataset, we had several choices of implementations available, such as LIWC (Linguistic Inquiry and Word Count), GI (General Inquirer), Hu-Liu04, ANEW (Affective Norms for English Words), SentiWord- Net and SenticNet. Each of these implementations had their pros and cons. Some provided sentiments divided in binary classes (positive and negative), and some provided intensity scores. However, there was the issue that our dataset consisted of tweets which famously are full of internet slang, abbreviations (due to limited capacity of tweets - 280 characters) and emojis. We were of the opinion that these traditional tools might not serve us well in our sentiment analysis. That led us to VADER (Valence Aware Dictionary and sEntiment Reasoner). VADER performed better than all these traditional tools on social media text, achieving precision and recall of 0.99 and 0.94, respectively. These results are outlined in the paper accompanying the release of VADER, (Hutto and Gilbert, 2015). It is described in its official capacity as:

> “VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.”

The aspect of VADER that was attractive to us was its ability to specifically mine social media for sentiment, and provide a valence score. The scoring consisted of positive, negative and neutral score, which were normalized.

VADER works well with emojis, degree modifiers, contractions, word-shape (ALL CAPS, for example), sentiment-laden slang (e.g. sux) and initialisms and acronyms. All these cases are common occurrences in tweets. Using these metrics, we calculated the absolute and relative sentiment for that day. We decided to go with only positive and negative tweets, and discard neutral tweets, because as extreme cases will carry the most information, and neutral tweets will add noise.

## 4. Causality Analysis

In order to establish the causality between stock price movement and Twitter sentiment analysis, we chose to go with Granger Causality Analysis. It was introduced by C.W. Granger in the 1960s, (Granger, 1969) and it deals with establishing causality between time series. The basic idea is that of cause-effect dependence where the cause not only should occur before the effect but also should contain unique information about the effect. Therefore, we say that X Granger-causes Y if the prediction of Y can be improved using both
information from X and Y as compared to only utilizing Y. Since causality is an inherently difficult thing to prove, the qualifier ”Granger” is used in front of causality to indicate that this method does not ascertain *true* causality, but merely points towards a relationship between the variables.

## 5. Conclusion

In this paper we analyzed the Granger-Causal relationship, a multivariate time series regression and a Sequential Neural Network Model between stock market prices for the top 50 S&P 500 companies, and the sentiment analysis on Twitter for the same set of stocks for the month of March 2019. For the first exercise, the Granger-Causal analysis, we were not able to independently prove causal relationship between public sentiment and stock performance. However, a multivariate time series regression equation for stock price log returns against two days lagged sentiment variables yielded a statistically significant result. In a final effort to obtain better results, we built a Sequential Neural Network Model using 4 day lagged values of stock prices and sentiment scores as inputs. Our main metric for success was the mean absolute error on change in price for the next day. For the behavior we witnessed in this model, we can conclude positive feedback that encourages the team to gather more data for future work.
