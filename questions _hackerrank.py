# if __name__ == '__main__': 
#     n = int(input())
#     arr = map(int, input().split()) 
#     if n>=2 and n <=10:
#          arr=list(set(arr)) 
#          a=max(arr) 
#          arr.remove(a) 
#          b=max(arr) 
#          print(b)

import random 
num=random.randint(1,100)
print(" hi ,please chosse number b/w 1 to 100")
guesses=1
user_input=-1
while(user_input != num):
 user_input=int(input(" enter your guess: "))

 if user_input < num :
        print(f"number is greater than your guess")
        guesses+=1
 elif user_input > num:
      print("number is less than your guess")
      guesses+=1

print(f"congratulation your guess is correct number {num},you take {guesses} attempt ")

#swap case question 
def swap_case(s):
    d=[]
    if len(s)>0 and len(s)<=1000  :
        for ch in s :
            if ch.isalpha()  :
                if  ch.isupper():
                    ch=ch.lower()
                    d.append(ch)
                elif  ch.islower():
                    ch=ch.upper()
                    d.append(ch)
            else:
                d.append(ch)
    return "".join(d)