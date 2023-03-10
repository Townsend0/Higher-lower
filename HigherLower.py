from data import ig,logo,vs
import random
import os
b=True
e=0
def Check(a):
    a[1]=random.choice(ig)
    while a[0]==a[1]:
        a[1]=random.choice(ig)
a=[random.choice(ig),random.choice(ig)]
Check(a)
print(logo)
while b and e!=49:
    print(f"\nCompare A: {a[0][0]}, a {a[0][2]}, from {a[0][3]}.")
    print(vs)
    print(f"Against B: {a[1][0]}, a {a[1][2]}, from {a[1][3]}.")
    c=input("\nWho has more followers? Type 'A' or 'B': ").lower()
    if c=='a' and a[0][1]<a[1][1] or c=='b' and a[0][1]>a[1][1]:
        os.system("clear")
        print(logo)
        print(f"\nSorry, that's wrong. Final score: {e}")
        b=False
    elif c=='a' and a[0][1]>a[1][1] or c=='b' and a[0][1]<a[1][1]:
        e+=1
        if e==49:
            os.system("clear")
            print(logo)
            print("\nCongrats you have literally beaten the game!")
        else:
            os.system("clear")
            print(logo)
            print(f"You're right! Current score: {e}.")
            if c=='a':
                Check(a)
            else:
                a[0]=a[1]
                Check(a)
    else:
        os.system("clear")
        print(logo)
        print("\n( Invalid input! )")