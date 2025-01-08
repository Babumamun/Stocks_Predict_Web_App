# Stocks_Predict_Web_App
This project is a culmination of both Streamlit, a Python Framework, along with Matplotlib, Sklearn, and Yahoo Finance. In this project, i decided to utilize a Linear Regression Model from sklearn in order to predict future trends. i specifically chose the Linear Regression Model so that i could efficiently predict the future stock prices of given stocks. Combining this with a dataset taken from Yahoo Finance, we were able to create a better dataset and model. Yahoo Finance gave us an up-to-date dataset, which we were able to implement as the training set and test set data for our Linear Regression model. This dataset is comprised of features such as “Close Price,” “Open Price,” “Volume,” “High,” and “Low,” however, we did need to add on another feature called “Date” so that we could keep track of the days. Here’s a look into a little bit of the raw data from one of the companies, Alibaba.

i used the datetime module in Python in order to make the time period for the stock more flexible for users.Additionally, i added two extra features: the Exponential Moving Average for 50 days and 200 days. Through doing this, i was able to predict whether the stock market was tending to be Bearish or Bullish during a certain period of time and show users more trends about their stock.
Before making the Regression Model, we wanted to first visualize some of this data. We plotted the High vs Low prices along with a graph of the daily closing price with the Exponential Moving Average for 50 and 200 days.

After getting a feel for the dataset, it was time to dive into the Linear Regression Model. The end goal for this project was to predict the Closing Price for a given stock, so i made it the X component. That left us with all the other features as Y components.
Next, Scikit-learn’s train_test_split function allowed me to separate the data into 80% for training and the rest 20% for testing.

Now it was time to fit the Linear Regression Model and predict what the future prices would be.
Once this was done, i wanted to visualize how accurate our model was, so i created a graph of the Model’s values vs the actual values.

Furthermore, i printed out the Real vs Predicted prices for the stock during random days. This allowed us to explicitly see how close or far apart these numbers were and make it more clear whether our model had worked as intended.

After finishing the Model, all that was left was to try to predict the closing price based on the different features. The one that stuck out to us the most was Volume vs Closing Price. i feel that this model worked really well and was able to mostly predict the values with little to no error.




Now time for some statistics. In order to fully see how well our model had performed, i had to look at the r² score, the mean absolute error, and the mean squared score.

Our project didn’t stop here, however. Previously i had already learned Flask, one of Python’s frameworks, so we went on to implement this as an app using that.
