#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import random
pd.options.mode.chained_assignment = None


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



# In[17]:


# Шаг 2. Массовая игра в русскую рулетку
def sectioning(setsDF):
    setsData = setsDF
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
        chosen = sectDF[sectDF['section']>rand]
        if(len(chosen.values.tolist())>0):break
        if (len(sectDF.values.tolist()) == 1):return sectDF.iloc[0]   
    return chosen.iloc[-1]


# In[27]:


#Создание пар
def createPairs(setsDF):
    setsDF = sectioning(setsDF)
    setsDF['pair'] = [0 for i in range(len(setsDF['set'].values.tolist()))]
    currPairNum = 0
    while True:
        pairless = setsDF[setsDF['pair']==0]
        pairlessCount = len(pairless.values.tolist())
    
        if(pairlessCount < 2):
            break
        
        firstParentID = roulette(pairless)['id']
        secondParentID = roulette(pairless[pairless['id'] != firstParentID])['id']
        setsDF.loc[setsDF['id'].isin([firstParentID,secondParentID]),'pair'] = currPairNum
        currPairNum=currPairNum+1
    return setsDF

#Шаг 5. Формирование новой популяции (замена своих родителей)

#Шаг 6. Оценка


# In[7]:


gen = generation(5,200)


# In[28]:


sectioning(gen)


# In[49]:


sectDF = createPairs(gen)
sectDF


# In[10]:


#Шаг 3. Кроссинговер (однородный (каждый бит от случайно выбранного родителя))
def breed(setPair):
    return [setPair[random.randint(0,1)][i] for i in range(0,len(setPair[0]))]


# In[11]:


#Шаг 4. Мутация (инвертирование всех битов у 1 особи )
def mutation(setPair):
    randnum = random.randint(0,1)
    return [(~np.array(setPair[randnum]).astype('bool')).astype('int').tolist(),setPair[1-randnum]]


# In[12]:


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


# In[54]:


iterationCount=0
setsDF = generation(len(priceList), 200)
while(iterationCount<500):
    prevmaxfit=setsDF['fitness'].max()    
    setsPairs = createPairs(setsDF)
    if (len(setsPairs[setsPairs['pair']!=0].values.tolist()) == 0):
        continue
    newSets = newPop(setsPairs[setsPairs['pair']!=0])
    newIDS = newSets['id'].values.tolist()
    setsDF = setsDF[~setsDF['id'].isin(newIDS)].append(newSets)
    iterationCount= iterationCount+1
    print(iterationCount)
    if(abs(setsDF['fitness'].max()-prevmaxfit)<min(priceList)):
        break
setsDF['fitness'].max()


# In[ ]:


setsDF


# In[ ]:


setsData = setsDF
setsData = setsData[setsData['fitness'] != 0]
totalFitness = sum(setsData['fitness'].values.tolist())
maxSectVal = 1

setsData.loc[:,'ab'] = 0
setsData

