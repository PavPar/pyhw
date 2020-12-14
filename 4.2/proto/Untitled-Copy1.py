#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import random


# In[2]:


dataFrame = pd.read_csv('../22.txt', sep=" ", header=None, skiprows=1, names=['w', 'v', 'p'])
WVVals = pd.read_csv('../22.txt', sep=" ", header=None, nrows=1)

maxWeight = WVVals.iloc[0][0]
maxVolume = WVVals.iloc[0][1]

weightList = dataFrame['w'].values.tolist()
volumeList = dataFrame['v'].values.tolist()
priceList = dataFrame['p'].values.tolist()


# In[3]:


def fitness(currSet):
    currWeight = sum([a * b for a, b in zip(weightList, currSet)])
    currVolume = sum([a * b for a, b in zip(volumeList, currSet)])
    currPrice = sum([a * b for a, b in zip(priceList, currSet)])

    if currVolume > maxVolume or currWeight > maxWeight:
        return 0;

    return currPrice;


# In[4]:


# Шаг 1 . Случайная генерация
def generateEntity(length):
    return [random.randint(0, 1) for i in range(length)]

def generation(length, entities):
    sets = []
    setID=0;
    for i in range(entities):
        newSet = generateEntity(length)
        sets.append([setID, newSet, fitness(newSet)])
        setID=setID+1
    return pd.DataFrame(sets,columns=['id', 'set', 'fitness'])



# In[5]:


# Шаг 2. Массовая игра в русскую рулетку
def rouleteSelection(setsDF):
    setsData = setsDF[['id','set','fitness']]
    setsData = setsData[setsData['fitness'] != 0]
    totalFitness = sum(setsData['fitness'].values.tolist())
    maxSectVal = 1;

    setsData['section'] = setsData.apply(lambda row: row['fitness']/totalFitness, axis=1)
    setsData = setsData.sort_values(by=['fitness'],ascending=False)

    sectionsFixed = setsData['section'].values.tolist()
    newSections = []
    for fit in sectionsFixed:
        maxSectVal = maxSectVal-fit
        if(maxSectVal<0):
            maxSectVal = 0
        fit = maxSectVal
        newSections.append(maxSectVal)
    setsData['section'] = newSections
    return setsData[setsData['section']>random.random()][['id','set','fitness']]


# In[6]:


#Создание пар
def createPairs(selectedSets):
    totalPairsCount = len(selectedSets[set].values.tolist())
    selectedSets['pair'] = [0 for i in range(totalPairsCount)]
    currPairNum = 0

    while True:
        pairless = selectedSets[selectedSets['pair']==0]
        pairlessCount = len(pairless.values.tolist())
    
        if(pairlessCount < 2):
            break
        
        while True:
            firstParentIdx = random.randint(0,pairlessCount-1)
            secondParentIdx = random.randint(0,pairlessCount-1)
            if(firstParentIdx != secondParentIdx):
                break
        selectedSets.iloc[[firstParentIdx,secondParentIdx],3] = currPairNum
        selectedSets = selectedSets.sort_values(by=['pair'])
        currPairNum=currPairNum+1
    return selectedSets

#Шаг 5. Формирование новой популяции (замена своих родителей)

#Шаг 6. Оценка


# In[7]:


#Шаг 3. Кроссинговер (однородный (каждый бит от случайно выбранного родителя))
def breed(setPair):
    return [setPair[random.randint(0,1)][i] for i in range(0,len(setPair[0]))]


# In[8]:


#Шаг 4. Мутация (инвертирование всех битов у 1 особи )
def mutation(setPair):
    randnum = random.randint(0,1)
    return [(~np.array(setPair[randnum]).astype('bool')).astype('int').tolist(),setPair[1-randnum]]


# In[9]:


def newPop(setsPairs):
    columnNames = ['id', 'set', 'fitness']
    pairsCount = setsPairs["pair"].max()
    newDF = pd.DataFrame(columns=columnNames)
    for pairIDX in range(1,pairsCount+1):
        setPair = setsPairs[setsPairs['pair'] == pairIDX]['set'].values.tolist()
        children = [breed(setPair),breed(setPair)]
        children = mutation(children)
        childIDS = setsPairs[setsPairs['pair'] == pairIDX]['id'].values.tolist()
        childID = 0
        for child in children:
            childDF = pd.DataFrame([[childIDS[childID],child,fitness(child)]],columns=columnNames)
            childID = childID+1
            newDF = newDF.append(childDF)
    return newDF


# In[17]:


iterationCount=0
setsDF = generation(len(priceList), 200)
while(iterationCount<500):
    prevmaxfit=setsDF['fitness'].max()    
    selectedSets = rouleteSelection(setsDF)
    setsPairs = createPairs(selectedSets)
    if (len(setsPairs[setsPairs['pair']!=0].values.tolist()) == 0):
        iterationCount = iterationCount + 1
        print('empty')
        continue
    newSets = newPop(setsPairs[setsPairs['pair']!=0])
    newIDS = newSets['id'].values.tolist()
    setsDF = setsDF[~setsDF['id'].isin(newIDS)].append(newSets)
    iterationCount= iterationCount+1
    if(abs(setsDF['fitness'].max()-prevmaxfit)<=min(priceList)):
        print('no changes')
        break
print(setsDF['fitness'].max())

# Шаг 2. Массовая игра в русскую рулетку
def sectioning(setsDF):
    setsData = setsDF[['id','set','fitness']]
    setsData = setsData[setsData['fitness'] != 0]
    totalFitness = sum(setsData['fitness'].values.tolist())
    maxSectVal = 1;

    setsData['section'] = setsData.apply(lambda row: row['fitness']/totalFitness, axis=1)
    setsData = setsData.sort_values(by=['fitness'],ascending=False)

    sectionsFixed = setsData['section'].values.tolist()
    newSections = []
    for fit in sectionsFixed:
        maxSectVal = maxSectVal-fit
        if(maxSectVal<0):
            maxSectVal = 0
        fit = maxSectVal
        newSections.append(maxSectVal)
    setsData['section'] = newSections
    return setsData

def roulette(sectDF):
    while True:
        rand = random.random()
        chosen = sectDF[sectDF['section']>rand][['id','set','fitness','section']];
        if(len(chosen.values.tolist())>0):break
    return chosen.iloc[-1]
# In[11]:
def createPairs2(setsDF):
    setsDF = sectioning(setsDF)
    setsDF['pair'] = [0 for i in range(len(setsDF['set'].values.tolist()))]
    currPairNum = 0
    while True:
        pairless = setsDF[setsDF['pair'] == 0]
        pairlessCount = len(pairless.values.tolist())

        if (pairlessCount < 2):
            break

        while True:
            firstParentID = roulette(pairless)['id']
            pairless.drop(pairless['id'] == firstParentID)
            secondParentID = roulette(pairless)['id']
            print('gen')
            if (firstParentID != secondParentID):
                print('gen-exit')
                break
        setsDF.loc[setsDF['id'].isin([firstParentID, secondParentID]), 'pair'] = currPairNum
        currPairNum = currPairNum + 1
    return setsDF

createPairs2(generation(5, 200))
setsDF

