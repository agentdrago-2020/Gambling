import random
tokens=1000
a=input("Would you like to gamble? (Yes/No) ")
print("You have",tokens,"tokens")
while a=="yes" and tokens>0:
    b=int(input("How many tokens would you like to bet? "))
    if tokens<b:
        print("Funds insufficient")
        break
    tokens=tokens-b
    print("1:   Colour")
    print("2:   Number")
    c=input("What would you like to place your bet on? ")
    if c=='1':
        print("1:   Red")
        print("2:   Black")
        d=int(input("Which colour would you like to bet on? "))
        r=random.randint(1,2)
        print(r)
        if r==d:
            print("You have won the bet!")
            tokens+=2*b
        else:
            print("Better luck next time")
    elif c=="2":
        print("1:   Place bet on single number")
        print("2:   Place bet on a range of numbers")
        d=int(input("Which action would you like to take?"))
        if d==1:
            e=int(input("Which number from 1 to 36 would you like to bet on?"))
            r=random.randint(1,36)
            print("The winning number is",r)
            if r==e:
                print("You have WON!!!")
                tokens+=35*b
            else:
                print("You have LOST")
        if d==2:
            print("1:   1-12 Range")
            print("2:   13-24 Range")
            print("3:   25-36 Range")
            e=int(input("Which action would you like to take? "))
            if e==1:
                n=1
                m=12
            elif e==2:
                n=13
                m=24
            elif e==3:
                n=25
                m=36
            r=random.randint(1,36)
            if r>n and r<m:
                print("You have WON!!!")
                tokens+=3*b
            else:
                print("You have LOST")
    print("You now have",tokens,"tokens")
    a=input("Would you like to gamble again? ")
    if tokens<=0:
        print("Too bad, you're broke")
print("Thank you for playing")
print("You are taking",tokens,"tokens home")
