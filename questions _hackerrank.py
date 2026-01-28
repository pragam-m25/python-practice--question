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


# question 18jan 2026 
# Question 1 solution 
def mutate_string(string, position, character):
   string=string[:position]+character+string[position+1:]
   return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#question 2 solution
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    if len(first) and len(last) <=10:
        print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    def avg_return():
        total=0
        for j in student_marks[query_name]:
            if j >=0 and j <=100:
                if len(scores)==3:
                    if n>=2 and n<=10 :
                        total+=j
                        avg = total/len(scores)
        return avg
    print(f"{avg_return():.2f}")
