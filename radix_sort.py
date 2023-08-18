def key_positions(seq, key):
    """adsf"""
    mapped = []
    for i in seq:
        mapped.append(key(i))
    k = max(mapped)
    

    c_array = [0 for _ in range(0,k+1)]
    size = len(c_array)
  
    for a in seq:
  
      
        c_array[key(a)] += 1 
    total = 0
    
    for i in range(size):
        c_array[i], total = total, total + c_array[i]
    
    return c_array
    
def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)
    

def radix_sort(numbers, d):
    """asdf"""
    for i in range(1,d+1):
        
        
        numbers = counting_sort(numbers,lambda x:int(("0"*d+str(x))[-i]))

    return numbers



def sorted_array(seq, key, positions):
    """adf"""
    b_array = [0 for i in range(len(seq))]
    p = key_positions(seq, key)
    
    for a in seq:
        b_array[p[key(a)]] = a
        p[key(a)] += 1
    return b_array
