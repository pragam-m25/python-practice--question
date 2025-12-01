a=input(" enter a word ").split()
print(len(a))

b=input(" enter a sentence ").split()
longest=""
for ch in b :
   if len(ch)>len(longest):
      maximum=len(ch)
      print("maximum word is ",ch ,maximum)

Input="hello,world!"

l=[]

for ch in Input :
    if (ch.isalnum() or ch==" "):
        l.append(ch)

result="".join(l)
print(result)

inp=input()
def clean_text(text):
    result=""
    for ch in text:
        if ch.isalnum() or ch == " ":
            result += ch 
    return result
print(clean_text(inp))

Inp=input()
no_digit=0
for ch in Inp:
    if ch.isdigit():
        no_digit +=1 
print(no_digit)


s= input("enter a string : ")
for ch in s :
    if s.count(ch) == 1 :
        print("First,non-repeating character :",ch)
        break

s="programing"
l=[]
for ch in s :
    if ch in l :
        continue
    else:
        l.append(ch)
result="".join(l)
print(result)


s="python is fun "
print(s.title())


text=input("enter a title: ")
out = ""
for w in text.split():
    out += w[0].upper() + w[1:] + " "
print(out.strip())



word="Admin" 
inp=input()
if word.lower() == inp.lower():
    print(True)
else:
    print(False)


w1="python"
w2="typhoon"

common=[]
for ch in w1 :
    if ch in w2 and ch not in  common:
        common.append(ch)
print(common)