i=0
while 1:
    print("===========")
    print("i="+str(i))
    if i > 0 and i < 10:
        i=i+5
        continue
    elif i == 25:      
        print(str(i+2))
        break
    elif i%2 == 0:  # % operator (modulo), special way to find remainders
        print("EVEN")
    elif i%2 == 1:
        print("ODD")
    
    i=i+1