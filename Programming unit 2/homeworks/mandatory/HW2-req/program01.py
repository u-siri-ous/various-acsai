# -*- coding: utf-8 -*-

def player_sum(player):
    
    pl_value = 0
    
    for i in player:
        pl_value += i
        
    return pl_value

def match_ord(match):
    
    l = []
    
    for i in match:
        l1 = []
        for j in i:
            l1.append(ord(j))
        l.append(l1)
    
    return l

def assign_points(match, k):
    
    len_match = len(match)
    
    playsum = [-1] * len_match
    total_points = [0] * len_match
    
    for i in range(len_match-1):        
        for j in range(i+1, len_match):
            pointsA, pointsB = 0,0
            for c in range(len(match[i])):
                sub = abs(match[i][c] - match[j][c])
                
                if sub == 0:
                    pass
                
                elif sub <= k:
                    if match[i][c] > match[j][c]:
                        pointsA += 1
                    else:
                        pointsB += 1
                        
                else:
                    if match[i][c] > match[j][c]:
                        pointsB += 1
                    else:
                        pointsA += 1
    
            if pointsA > pointsB:
                total_points[i]+= 1
                        
            elif pointsB > pointsA:
                total_points[j]+= 1
                        
            else:
                        
                if playsum[i] == -1:
                    playsum[i] = player_sum(match[i])
                    
                if playsum[j] == -1:
                    playsum[j] = player_sum(match[j])
                        
                if playsum[i] < playsum[j]:
                    total_points[i]+= 1
                            
                elif playsum[i] > playsum[j]:
                    total_points[j]+= 1
                            
                else:
                    if match[i] < match[j]:
                        total_points[i] += 1
                    else:
                        total_points[j] += 1
                        
    criteria =  lambda index : total_points[index]                   
    return sorted(range(len_match), key = criteria, reverse = True)
    

def ex(matches, k):
    
    match = matches.copy()
    match = [x.replace(' ', '').replace('\t', '') for x in match] 
    
    match = match_ord(match)
    
    return assign_points(match, k)

if __name__ == "__main__":
    pass
