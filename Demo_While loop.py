#psuedo_code
#While Saving is not greater than $1,000
current_money = 20
n_days = 0
while current_money <= 1000 :
    current_money = current_money + 35
    n_days = n_days + 1
    print("Day "+str(n_days)+ " Current money = "+ str(current_money))
 
print("I reach to my target within "+str(n_days)+"days"+" ,and the current money in my saving is $"+str(current_money))