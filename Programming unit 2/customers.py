#write a function that takes an input the number of customers and the cost of tickets for a
#museum entrance and returns the amount the group should pay considering that
#is the number of customers is >= 10 there will be a discount of 25% for each ticket

def amount(customers, cost):    
    if customers >= 10:
        cost=cost*0.75       
    return cost*customers
