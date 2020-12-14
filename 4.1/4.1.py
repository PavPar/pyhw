
# https://github.com/remiomosowon/pyeasyga.git
import numpy as np
import pandas as pd
from pyeasyga import pyeasyga

dataFrame = pd.read_csv('22.txt', sep=" ", header=None , skiprows=1, names=['w','v','p'])
WVVals = pd.read_csv('22.txt', sep=" ", header=None , nrows = 1)

maxWeight = WVVals.iloc[0][0]
maxVolume = WVVals.iloc[0][1]

weightList = dataFrame['w'].values.tolist()
volumeList = dataFrame['v'].values.tolist()
priceList = dataFrame['p'].values.tolist()

ga = pyeasyga.GeneticAlgorithm(dataFrame)        # initialise the GA with data
ga.population_size = 200;


def fitness(currSet, data):

    currWeight = sum([a*b for a,b in zip(weightList,currSet)])
    currVolume= sum([a*b for a,b in zip(volumeList,currSet)])
    currPrice = sum([a*b for a,b in zip(priceList ,currSet)])

    if currVolume > maxVolume or currWeight > maxWeight:
        return 0;

    return currPrice;

ga.fitness_function = fitness               # set the GA's fitness function
ga.run()                                    # run the GA

resSet = ga.best_individual()[1]
totalWeight = sum([a * b for a, b in zip(weightList, resSet)])
totalVolume = sum([a * b for a, b in zip(volumeList, resSet)])
totalPrice = ga.best_individual()[0]

print('Полученный набор: ',resSet)
print('Полученный вес: ',totalWeight)
print('Полученный объем: ',totalVolume)
print('Полученная цена: ',totalPrice)