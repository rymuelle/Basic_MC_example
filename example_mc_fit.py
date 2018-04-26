import numpy as np
import pprint
import pandas as pd
#from sklearn import linear_model
import statsmodels.api as sm

import matplotlib.pyplot as plt

#define my params
slope = []

intercept = []

#start MC loop

for i in range(10000):

	#add noise
	X = np.arange(10) # [0,1,2]
	
	X = X + np.random.rand(10)
	
	Y = np.arange(10)
	
	#model goes here
	
	X = sm.add_constant(X)
	model = sm.OLS(Y,X)
	results = model.fit()
	
	#get params out of model

	slope.append(results.params[1])
	intercept.append(results.params[0])

#plot intercept and slope

plt.scatter(intercept, slope , marker='.' , alpha = '.1', c='r',)

#plt.hist(intercept)

#plt.grid(True)
#plt.semilogy()
plt.title("intercept vs slope")
plt.xlabel("intercept")
plt.ylabel("slope")

plt.show()