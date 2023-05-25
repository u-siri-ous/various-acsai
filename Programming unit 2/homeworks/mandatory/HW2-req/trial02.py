# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:38:07 2021

@author: Siria

"""
# =============================================================================
# def ex(match,k):
#     #part 1: remove spaces, compare string elements
#     matches = match.copy()
#     matches = [i.replace(' ','').replace('\t','') for i in matches]
#     points = [0] * len(matches)
#     rank = []
#     for i in range(len(matches)-1):
#         for j in range(i+1,len(matches)):#this kinda works but not well
#         #part 1.5: assign points like said in the .py
#             if (ord(matches[i][j]) - ord(matches[j][i])) <= k:
#                 if (ord(matches[i][j]) > ord(matches[j][i])):
#                     points[i] += 1
#                 elif (ord(matches[i][j]) < ord(matches[j][i])):
#                     points[j] +=1
#             elif (ord(matches[i][j]) - ord(matches[j][i])) >= k:
#                 if (ord(matches[i][j]) > ord(matches[j][i])):
#                     points[j] += 1
#                 elif (ord(matches[i][j]) < ord(matches[j][i])):
#                     points[i] += 1
#                 if points[i] == points[j]:
#                     if ord(matches[i][j]) < ord(matches[j][i]):
#                         points[i] += 1
#                 else:
#                     points[j] += 1
#     rank = sorted(range(len(points)), key=lambda k: points[k], reverse=True)
#     return rank
# =============================================================================

def assign_points(game, pl1, pl2, k):
    score1 = 0
    score2 = 0
    wins1 = 0
    wins2 = 0
    playersum = []
    
    for p1,p2 in zip(pl1,pl2):
        p1 = ord(p1)
        p2 = ord(p2)
        if abs(p1-p2) <= k:
            score1 += 1
        else:
            score2 += 1
    if score1 > score2:
        wins1 += 1
    elif score1 < score2:
        wins2 += 1
        
    return[wins1, wins2]

def removespaces(lst):
    lstcopy = lst.copy()
    lstcopy = [x.replace(' ', '').replace('\t', '') for x in lstcopy]
    return lstcopy    

def ex(matches, k):
    removespaces(matches)
    points = []
    for pl1 in range(len(matches)-1):
        for pl2 in range(pl1+1, len(matches)):
            
            assign_points(matches, matches[pl1], matches[pl2], k)
            
            points.insert(0, pl1)
            points.insert(1,pl2)
            
    rank = sorted(range(len(points)), key=lambda k: points[k], reverse=True)
    return rank    
# =============================================================================
# def trial02(matches, k):
#     #part 1: remove spaces, compare string elements
#     matches = [i.replace(' ','') and i.replace('\t','') for i in matches]
#     pointsA = []
#     pointsB = [] #consider making these two ints
#     for i in range(len(matches)):
#         for j in range(len(matches)):
#             #part 1.5: assign points like said in the .py
#             if (ord(matches[i][j]) - ord(matches[j][i])) <= k:
#                 if (ord(matches[i][j]) > ord(matches[j][i])):
#                     pointsA.append(1)
#                 elif (ord(matches[i][j]) < ord(matches[j][i])):
#                     pointsB.append(1)
#             elif (ord(matches[i][j]) - ord(matches[j][i])) >= k:
#                 if (ord(matches[i][j]) > ord(matches[j][i])):
#                     pointsB.append(1)
#                 elif (ord(matches[i][j]) < ord(matches[j][i])):
#                     pointsA.append(1)               
#         total1 = sum(pointsA)
#         total2 = sum(pointsB)
#      #part 2: tie   
#         if total1 == total2:
#             if ord(sum(matches[i])) < ord(sum(matches[j])):
#                 pass
#                 #point given to A, else give point to B
#             #do the if like before, but w/out sums, the smaller is given a point accordingli
#                     
#     #return ranking
# =============================================================================
                
if __name__ == "__main__":
    trial03(["aac","ccc","caa"], 2)   
          
    
    
    
    