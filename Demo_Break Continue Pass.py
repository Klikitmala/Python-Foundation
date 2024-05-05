#EX 1
LEKTAI = 69
while True :
    number = int(input("Please fill your 2 digit number : "))
    if number > 99 :
        print("Wrong, it should be only 2 digits")
        break
    elif number == LEKTAI :
        print("You win!")
    else :
        print("Sorry!")
        
#EX 2
secret_code = "H$A$N$NIN$AR$AK$JU$DJ$$$UD"
hidden_code = ""
for c in secret_code :
    if c == "$":
        continue
    hidden_code = hidden_code + c
    print("Hidden code : ", hidden_code)
print("Code without $ :", hidden_code)
       