#loads the packages we will be using to do a PCF and ACF function 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.api as sm 

#loads the data into a dataframe defined as df
df = pd.read_csv('tovar_moving.csv')

#because the data is separated by periods, we need to turn it into a date/time function. this piece of code does that 
df['new_date'] = pd.to_datetime(df['date'])

#the way to index the df is to set the new column we created as the date
new_date_index = df.set_index('new_date')

#we will now take the date and tuncating the date... we can cumulate all the september, october, and november etc.
year_month_summary = new_date_index.groupby(lambda x: x.year * 100 + x.month).count()

#here we investigate the new variable and extract qty and get the counts by obversation
qty_count_summary = year_month_summary['qty']

#plotting the ACF function
sm.graphics.tsa.plot_acf(qty_count_summary)
plt.show()

#plotting the pcf function
sm.graphics.tsa.plot_pacf(qty_count_summary)
plt.show()