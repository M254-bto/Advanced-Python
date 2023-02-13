from decorators import timer

z = [19]
u = []

@timer
def randoom(a, c, m):
    while len(z) < m:
        z.append((a * z[-1] + c) % m)
       
        

    for i in z:
        uni = i / m
        u.append(uni)
    
    return [z[1:]]



print(randoom(22, 4, 63))
    


        
