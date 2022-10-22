num = int(input("Enter Positive Number Check Weather It Is Prime Or not Prime :"))

if num > 1:
    for i in range(2,num,1):
        if num % i == 0:
            print(f"{num} is Not Prime Number")
            break
        else:
            print(f"{num} Is Prime Number" )
            break
else:
    print("Your Entered Negetive Number ")
