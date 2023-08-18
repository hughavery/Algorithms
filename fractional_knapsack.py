def fractional_knapsack(capacity, items):
    """find unit per unit and sort it"""
    items.sort(key = lambda a: a[1] / a[2])
    items.reverse()

    max_value = 0

    
    for i in items:
    
        
        if capacity == 0:
            return max_value
                
        if i[2] <= capacity:
            max_value += i[1]
            capacity -= i[2]
        
        else:
            fraction = capacity / i[2]
            max_value += fraction * i[1]
            capacity = 0
    return(max_value)