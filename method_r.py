#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:39:50 2019

@author: mjzhang
"""
import statistics


def WZ_stdDev(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot/len(X))**0.5  # Square root of mean difference


print('Calculate the variance for Method R MOT Edition 3 \
       Sample Sets on page 8')
list_A = [0.924, 0.928, 0.954, 0.957, 0.961, 0.965, 0.972, 0.979, 0.987, 1.373]


print('WZ stddev of list_A is {:15.9f}'.format(WZ_stdDev(list_A)))
print('WZ variance of list_A is {:15.9f}'.format(WZ_stdDev(list_A) ** 2))
print('Statistic stddev list_A is {:15.9f}'.format(statistics.stdev(list_A)))
print('Population Statistic stddev list_A \
        is {:15.9f}'.format(statistics.pstdev(list_A)))
print("Statistic Variance of list_A is \
        {:15.9f}".format(statistics.variance(list_A)))
print("Population Statistic Variance of list_A is \
       {:15.9f}".format(statistics.pvariance(list_A)))


print('...........................................................')
list_C = [0.091, 0.109, 0.134, 0.136, 0.159, 0.172, 0.185, 0.191, 0.207, 8.616]

print('WZ stddev of list_C is', WZ_stdDev(list_C))
print('WZ variance of list_C is', WZ_stdDev(list_C) ** 2)
print('Statistic stddev list_C is', statistics.stdev(list_C))
print('Population Statistic stddev list_C is \
       {:15.9f}'.format(statistics.pstdev(list_C)))
print("Statistic Variance of list_C is \
         {:15.9f}".format(statistics.variance(list_C)))
print("Population Statistic Variance of \
       list_C is {:15.9f}".format(statistics.pvariance(list_C)))
