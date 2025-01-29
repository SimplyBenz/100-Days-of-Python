"""
This script calculates the value of a European call option using the Monte Carlo simulation method.

Parameters:
S0 (float): Initial index level.
K (float): Strike price.
T (float): Time-to-maturity.
r (float): Riskless short rate.
sigma (float): Volatility.
I (int): Number of simulations.

Variables:
z (ndarray): Pseudo-random numbers generated from a standard normal distribution.
ST (ndarray): Index values at maturity.
hT (ndarray): Payoff at maturity.
CB (float): Monte Carlo estimator for the value of the European call option.

Output:
Prints the value of the European call option formatted to three decimal places.
"""

import math
import numpy as np

S0 = 100 #initial index level
K = 105 #strike price
T = 1.0 #time-to-maturity
r = 0.05 #riskless short rate
sigma = 0.2 #volatility

I = 10000 #number of simulations

#Valuation Algorithm
z = np.random.standard_normal(I) #pseudo-random numbers
#index values at maturity
ST = S0 * np.exp((r-0.5*sigma**2)*T+sigma*math.sqrt(T)*z)
hT = np.maximum(ST-K,0) #payoff and maturity
CB = math.exp(-r*T)*np.mean(hT) #Monte Carlo setimator

#Result output
print("Value of the European call option %5.3f." % CB)