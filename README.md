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