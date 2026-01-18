# python-practice--question
que1 
Problem Submissions Leaderboard Discussions Editorial Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given scores.Store them in a list and find the score of the runner-up. 
Input Format The first line contains . 
The second line contains an array of integers each separated by a space. 
Constraints Output Format Print the runner-up score. 
Sample Input 0: 5 2 3 6 6 5 
Sample Output 0 :5 
 
 my thinking :
 pehle mene isme constraints lagaye uske bad mein directly arr pe remove laga raha tha mene dhyan nahi,
  diya ki vo list mein chnage nahi wo map mein tha jis ke karan error ara tha phir uske bad mene usko , 
  list mein kiya taki remove method chal jaye aur jo max element hai wo remove ho jaye phir uske bad bhi, 
  output nahi ayi kyuki usme repeted max element the fhir mene setb ka use karke duplictae value fremove ,
  ki uske bad max element remove hua aur fir se max element print karwaya jis se agya second highest score, 
  
Question 2 : make a game of random guess 

question of hackker rank 
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints

len(s)>0 and len(s)<=1000 
Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".


today hackerrank questions date 18 jan 2026
Question1 :

We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

Example

>>> string = "abracadabra"
You can access an index by:

>>> print string[5]
a
What if you would like to assign a value?

>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
How would you approach this?

One solution is to convert the string to a list and then change the value.
Example

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
Another approach is to slice the string and join it back.
Example

>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
Task
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string
Input Format

The first line contains a string, .
The next line contains an integer , the index location and a string , separated by a space.

Sample Input

STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
Sample Output

abrackdabra

Question2 :

You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Function Description

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
Prints

string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last names are each ≤ .

Sample Input 0

Ross
Taylor
Sample Output 0

Hello Ross Taylor! You just delved into python.
Explanation 0

The input read by the program is stored as a string data type. A string is a collection of characters.