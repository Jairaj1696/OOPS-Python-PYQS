def Factor(X,Y):
    print('common factor of X and Y are:')
    for i in range(1,min(X,Y)+1):
        if X % i == 0 and Y % i == 0:
            print(i)

a=int(input('Enter the value of x :'))
b=int(input('Enter the value of y :'))
Factor(a,b)