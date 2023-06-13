#def triangle(f):
#    k = f - 1
#    for i in range (0,f):
#        for j in range(0,k):
#            print(end=" ")
#        k = k - 1
#        for j in range(0,i+1):
#            print("*", end=" ")
#        print("\r")
#f = 6
#triangle(f)



for i in range(5):
    for j in range(i):
        print(" ",end=" ")
    for g in range(i,5):
        print("*",end=" ")
    print()
