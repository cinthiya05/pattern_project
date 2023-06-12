# input 4
# output '* * * *'

# same  input 4
# output '* * *'

# same input 4
# output  7 stars varum

# for x in range(4):
#     print("*",end=" ")
    
#for x in range(1,4):
#    print("*",end=" ")

# for x in range(-3,4):
#     print("*",end=" ")
# n=6
# for x in range(n):
#     print("*",end=" ")
#     # print('x',x)
#     for j in range(0,n-1):
#         # print('j',j)
#         print("*",end=" ")
# for j in range(0,5-1):
#         # display star
#     print("*", end=' ')



# paru na sona matiri tha agiruku 
#rows = 5
#for i in range(rows + 1, 0, -1):
    # nested reverse loop
#    for j in range(0, i - 1):
#        print("*",end=" ")
#    print(" ")

#row = 6
#for i in range(row):
#    print(' '* i,end=" ")
#    for j in range(row - i):
#        print("*",end=" ")
#    print()


row = 6
for i in range(row):
    print(' ' * i,end=" ")
    for j in range(row-i):
        print("*",end=" ")
    print()

