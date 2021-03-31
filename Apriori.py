#!/usr/bin/env python
# coding: utf-8

# In[164]:


import pandas as pd
from itertools import combinations 
min_sup = float(input('Enter minimum support value: ')) 
min_con = float(input('Enter minimum confidence value: '))
print('barnesandnoble --> 1')
print('targetmovies --> 2')
print('sephora --> 3')
print('wholefoods --> 4')
print('nbajerseys --> 5')
file_number = input('Enter File Number: ')
print('File Number: ', file_number)
file = '/Users/njeriwhite/Desktop/BarnesAndNoble.csv'
if int (file_number) == 2:
    file = '/Users/njeriwhite/Desktop/TargetMovies.csv'
if int (file_number) == 3:
    file = '/Users/njeriwhite/Desktop/Sephora.csv'
if int (file_number) == 4:
    file = '/Users/njeriwhite/Desktop/WholeFoods.csv'
if int (file_number) == 5:
    file = '/Users/njeriwhite/Desktop/nbajerseys.csv'

dataframe = pd.read_csv(file)

headers = list(dataframe.columns)

items = dataframe[headers[1]]
trans_id = dataframe[headers[0]] 

uni_items = dataframe[headers[1]].unique()
uni_tid = dataframe[headers[0]].unique()

def build_transactions(uni_tid, trans_id, items):
    transactions = []
    for i in uni_tid:
        temp_list = []
        for j in range(0, len(trans_id)):
            if trans_id[j] == i:
                temp_list.append(items[j])            
        transactions.append(temp_list)
    return(transactions)

transactions = build_transactions(uni_tid, trans_id, items)
num_trans = len(transactions)

def check_pattern(compare, compareto):
    i = 0
    if(all(i in compareto for i in compare)):
        i = 1
    return i

def update (a, b):
    
    fre = []
    
    for i in a:
        for j in i:
            fre.append(j)
    
    temp = []
    for i in b:
        if i  in fre:
            temp.append(i)
    
    return temp

pat_size = 1 
fre_pat = [] 
fre_pat_count = [] 
temp_fre_pat = [1] 


fre_items = list(uni_items) 
while (temp_fre_pat):

    
    pats = combinations(fre_items, pat_size)
    temp_fre_pat = [] 
    for f in list(pats):
        
        count = 0
        for t in transactions:
            count = count + check_pattern(f, t)
        if count >= min_sup * num_trans:
            temp_fre_pat.append(f)
            fre_pat_count.append(count)
    
    fre_pat = fre_pat + temp_fre_pat
    pat_size += 1 
    

    
    fre_items = update(temp_fre_pat, fre_items)
    


print('\nFREQUENT ITEMSETS:   \n',fre_pat)

print('\nASSOCIATION RULES: ')

for i in fre_pat:

    if len(i) > 1:
        
        groupings = list(combinations(i, len(i) - 1))
        
        for j in groupings:
            temp = []
            for k in j:
                temp.append(k)
            z = list(set(i).difference(set(temp)))
            confidence = fre_pat_count[fre_pat.index(i)] / fre_pat_count[fre_pat.index(j)]
            if confidence > min_con:
                print(j,' ---> ', z ,'   confidence = ',confidence)


# In[162]:


print(uni_items)


# 

# In[ ]:




