def payInCoins(x):
    coins=[25,10,5]
    num={"Quarters":0,"Dimes":0,"Nickel":0,"Pennies":0}
    for i in range(len(coins)):
        while x+1>coins[i]:
            x-=coins[i]
            if i==0:
                num["Quarters"]+=1
            if i==1:
                num["Dimes"]+=1
            if i==2:
                num["Nickel"]+=1
    num["Pennies"]=x
    return num
print(payInCoins(0))
print(payInCoins(1))
print(payInCoins(5))
print(payInCoins(10))
print(payInCoins(25))
print(payInCoins(12))
print(payInCoins(99))
print(payInCoins(76))

