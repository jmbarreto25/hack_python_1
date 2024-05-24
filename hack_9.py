"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i = 0
    nueva = []  
    while i < len(result):
        nueva.extend([result[i], '@'])
        i += 1 
    result = nueva  
    return result
