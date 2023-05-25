# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:31:09 2021

@author: Siria
Write a function to partition a given list based on the last item of the list,
so that the original list gets modified
"""

def partition(l, start, end):
# =============================================================================
#     #partition of a list
#     l_lower = list()
#     l_higher = list()
#     for item in l[:-1]:
#         if item < l[-1]:
#             l_lower.append(item)
#         else:
#             l_higher.append(item)
#     l2 = l_lower + [l[-1]] + l_higher
#     for i in range(len(l)):
#         l[i] = l2[i]
#     return l
# =============================================================================
    j = 0
    #for each index i in 0, len-1
    for i in range(len(l)-1):
    #if the item in position i is < pivot
        if l[i] < l[-1]:
    #exchange i with j and increment j
            l[i], l[j] = l[j], l[i]
            j += 1
    #after the loop, exchange pivot with j
    l[-1], l[j] = l[j], l[-1]
    
def QuickSort(l, start, end):
    if (end - start) <= 1:
        return
    pivot_pos = partition(l, start, end)
    QuickSort(l, start, pivot_pos -1)
    QuickSort(l, start, pivot_pos -1)
    