def getChange(n):
    op = {'2000Rs':0, '1000Rs':0, '500Rs':0, "100Rs":0, "50Rs":0, "20Rs":0, "10Rs":0, "5Rs":0} # Initialize each denominations with 0 count. 
    while n!=0:
        if n>=2000:
            ch1 = n // 2000
            op['2000Rs']+= ch1
            n= n % 2000
        elif n>=1000:
            ch1 = n // 1000
            op['1000Rs']+= ch1
            n= n % 1000
        elif n>=500:
            ch1 = n // 500
            op["500Rs"]+= ch1
            n = n % 500
        elif n>=100:
            ch1 = n // 100
            op["100Rs"]+= ch1
            n = n % 100
        elif n>= 50:
            ch1 = n // 50
            op["50Rs"]+= ch1
            n = n % 50
        elif n>=20:
            ch1 = n // 20
            op["20Rs"]+= ch1
            n = n % 20
        elif n>=10:
            ch1 = n // 10
            op["10Rs"]+= ch1
            n = n % 10
        elif n>= 5:
            ch1 = n // 5
            op["5Rs"]+= ch1
            n = n % 5
        else:
            print("\nChange left without denominations are: {}".format(n))
            break
    print()
    print("Available Changes are: {}".format(op))

amount = int(input("Enter The Amount You Need to get Change: "))
getChange(amount)
