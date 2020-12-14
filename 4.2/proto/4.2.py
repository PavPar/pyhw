# https://github.com/remiomosowon/pyeasyga.git
import numpy as np
import pandas as pd
import random

dataFrame = pd.read_csv('../22.txt', sep=" ", header=None, skiprows=1, names=['w', 'v', 'p'])
WVVals = pd.read_csv('../22.txt', sep=" ", header=None, nrows=1)

maxWeight = WVVals.iloc[0][0]
maxVolume = WVVals.iloc[0][1]

weightList = dataFrame['w'].values.tolist()
volumeList = dataFrame['v'].values.tolist()
priceList = dataFrame['p'].values.tolist()


def fitness(currSet):
    currWeight = sum([a * b for a, b in zip(weightList, currSet)])
    currVolume = sum([a * b for a, b in zip(volumeList, currSet)])
    currPrice = sum([a * b for a, b in zip(priceList, currSet)])

    if currVolume > maxVolume or currWeight > maxWeight:
        return 0;

    return currPrice;


# Шаг 1 . Случайная генерация
def generateEntity(length):
    return [random.randint(0, 1) for i in range(length)]


def generation(length, entities):
    sets = []
    for i in range(entities):
        newSet = generateEntity(length)
        sets.append([0, newSet, fitness(newSet)])
    return pd.DataFrame(sets,columns=['age', 'set', 'fitness'])


res = generation(5, 10)
print(res)

# Шаг 2. Массовая игра в русскую рулетку
def rouleteSelection(setsDF):
    setsData = setsDF['set','fitness']
    totalFitness = sum(setsData['fitness'].values.list())
    setsData

# totalWeight = sum([a * b for a, b in zip(weightList, resSet)])
# totalVolume = sum([a * b for a, b in zip(volumeList, resSet)])
# totalPrice =

# print('Полученный набор: ',resSet)
# print('Полученный вес: ',totalWeight)
# print('Полученный объем: ',totalVolume)
# print('Полученная цена: ',totalPrice)
random.random(0,1)

random.ra