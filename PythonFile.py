import sys 
# sys.stdin=open("input.in","r")
# sys.stdout=open("output.out","w")
# WE WILL BUILD A GAME 

print("Please Guess a Number betweeen 1 to 100")
# we will do something 
print("Enter 1  if you have guesses")
print("ENTER 0 if you have not gussed")
n=int(input())
if n==1:
    start=1
    end=100
    #BINARY SEARCH
    while start<end:
        mid=(start+end)//2
        print(mid)
        print("ENTER 1 if your number is greater")
        print("ENTER 2 if your number is smaller")
        print("ENTER 3 if your number is equal")
        user=int(input())
        if user==1:
            start=mid
            # YAHA KO LGGIC
        elif user==2:
            end=mid
            # YAHA koi LOGIC
        else:
            print("Congratulation")
            break
elif n==0:
    print("USER DID NOT RESPOND ")