# pcf_acf_analysis
sample dataset that i used to explore the pcf and acf functions in statsmodels 


For this particular dataset, we use the ACF/PCF functions to perform an ARIMA analysis on some sample data. This included a slight bit of cleaning up, but the statistical model is more rigorous. 

For the ACF (autocorrelation function) the result is that the data is not stationary. The ACF measures the impact that seasonality makes on the dataset. 
Particularly, the data set has random noise (we see a lag of roughly 10 periods, where the data cuts off to 0, then continues to go down until it goes up). The data ends up being linear. 

The PCF function is a measurement as to how much seasonality impacts the data. We see here after two periods (which, if building a model, we would need to use a lag of 2). 

