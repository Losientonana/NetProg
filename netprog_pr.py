from random import randint

playerMoney = 50

while playerMoney <= 100 and playerMoney > 0:
    coin = randint(1,2)
    choice = randint(1,2)
    
    if(coin == choice):
        playerMoney += 9
    else:
        playerMoney -= 10
    print("current money: ",playerMoney)
print("final player money: ",playerMoney)
