"""
Purpose: Write a program that simulates a Magic Ball.
Input: File called 8_ball_responses will be read. User will be asked if they want to continue
       with the program. User will enter 'true' to continue with the program and to quit, input anything else. They will then input a question

Output: The computer will randomly generate an answer to the question. User will be asked
        if they want to continue.
Algorithm:
        1. import the random library
        2. Open the text file
        3. Create a list called magicBall
        4. Ask if the user wants to continue
        5. if the user answers true
            for each line in infile
               a. remove the "\n" from each line
               b. add each line to the list.
        6. Prompt user to enter a question
        7. Program will randomly display a response
        8. Program will ask user if he/she wants to continue

"""
import random

infile = open(r"E:\CMPSC121\8_ball_responses.txt", "r")
magicBall = []
ans = input ("Enter 'true'  if you wish to continue: ")
while ans == 'true':
    for line in infile:
        line = line.rstrip('\n')
        magicBall.append(line)
           
    question = input("Please enter a question here: ")
    print(random.choice(magicBall))
    ans = input ("Enter 'true'  if you wish to continue: ")
    if ans != 'true':
        infile.close() 
