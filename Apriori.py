import pandas as pd
import itertools
import csv

def sublist(lst1, lst2):
    if(all(x in lst2 for x in lst1)):
        return True
    return False
    
def check_subset_frequency(itemset, l, n):
    if n>1:    
        subsets = list(itertools.combinations(itemset, n))
    else:
        subsets = itemset
    for iter1 in subsets:
        if not iter1 in l:
            return False
    return True

def stage_1(items, minimum_support_count):
    c1 = {i:items.count(i) for i in items}
    l1 = {}
    for key, value in c1.items():
        if value >= minimum_support_count:
           l1[key] = value 
    
    return c1, l1
    
def stage_2(l1, records, minimum_support_count):
    l1 = sorted(list(l1.keys()))
    L1 = list(itertools.combinations(l1, 2))
    c2 = {}
    l2 = {}
    for iter1 in L1:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c2[iter1] = count
    for key, value in c2.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l1, 1):
                l2[key] = value 
    
    return c2, l2
    
def stage_3(l2, records, minimum_support_count):
    l2 = list(l2.keys())
    L2 = sorted(list(set([item for t in l2 for item in t])))
    L2 = list(itertools.combinations(L2, 3))
    c3 = {}
    l3 = {}
    for iter1 in L2:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c3[iter1] = count
    for key, value in c3.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l2, 2):
                l3[key] = value 
        
    return c3, l3
    
def stage_4(l3, records, minimum_support_count):
    l3 = list(l3.keys())
    L3 = sorted(list(set([item for t in l3 for item in t])))
    L3 = list(itertools.combinations(L3, 4))
    c4 = {}
    l4 = {}
    for iter1 in L3:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c4[iter1] = count
    for key, value in c4.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l3, 3):
                l4[key] = value 
        
    return c4, l4

def stages():

def support_count(itemset, itemlist):
    return itemlist[itemset]
    
def main(min_support, min_confidence):
    # data = pd.read_csv('Complete_File_Location')
    minimum_support_count = 2
    records = []
    for i in range(0, 20):
        records.append([str(data.values[i,j]) for j in range(0, 4)])

    items = sorted([item for sublist in records for item in sublist if item != 'nan'])

    c1, l1 = stage_1(items, minimum_support_count)
    c2, l2 = stage_2(l1, records, minimum_support_count)
    c3, l3 = stage_3(l2, records, minimum_support_count)
    c4, l4 = stage_4(l3, records, minimum_support_count)
    """
    print(*records, sep = ", ")
    print(len(data))
    print(len(records))
    print(len(l1))
    print(len(l2))
    print(len(c1))
    print(len(c2))
    """
    sets = []
    for iter1 in list(l3.keys()):
        subsets = list(itertools.combinations(iter1, 2))
        sets.append(subsets)

    list_l3 = list(l3.keys())
    for i in range(0, len(list_l3)):
        for iter1 in sets[i]:
            a = iter1
            b = set(list_l3[i]) - set(iter1)
            confidence = (support_count(list_l3[i], l3)/support_count(iter1, l2))*100
            print("Confidence{}->{} = ".format(a,b), confidence)
    
main(0.01, 0.7)
