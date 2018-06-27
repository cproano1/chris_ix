#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:03:15 2018

@author: Chris
"""
#%%
board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

turn_number = 1
row_input = 3
col_input = 3

while turn_number <= 9:
    print(board)
    if turn_number % 2 == 1: #Player 1's turn
        row_input = input("Player 1, pick a row")
        row_input = int(row_input)
        col_input = input("Player 1, pick a column")
        col_input = int(col_input)
    if turn_number % 2 == 0: #Playr 2's turn
        row_input = input("Player 2, pick a row")
        row_input = int(row_input)
        col_input = input("Player 2, pick a column")
        col_input = int(col_input)   
    if board[row_input][col_input] == " ":
        if turn_number % 2 == 1: #Player 1's turn
            board[row_input][col_input] = "X"
        if turn_number % 2 == 0: #Playr 2's turn1
            board[row_input][col_input] = "O"
        turn_number += 1
    
    #check horizontal win
    if board[0][0] == "X" and board[0][1] == "X" or board[0][2] == "X":
        print("Player 1 wins!")
        exit()
    elif board[1][0] == "X" and board[1][1] == "X" or board[1][2] == "X":
        print("Player 1 wins!")
        exit()
    elif board[2][0] == "X" and board[2][1] == "X" or board[2][2] == "X":  
        print("Player 1 wins!")
        exit()
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("Player 2 wins!")
        exit()
    elif board[1][0] == "O" and board[1][1] == "O" or board[1][2] == "O":
        print("Player 2 wins!")
        exit()
    elif board[2][0] == "O" and board[2][1] == "O" or board[2][2] == "O":
        print("Player 2 wins!")
        exit()
            
            
    #check column win
    if board[0][0] == "X" or board[1][0] == "X" or board[2][0] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][1] == "X" or board[1][1] == "X" or board[2][1] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][2] == "X" or board[1][2] == "X" or board[2][2] == "X":
        print("Player 1 wins!")
        exit()
    elif board[0][0] == "O" or board[1][0] == "O" or board[2][0] == "O":
        print("Player 2 wins!")
        exit()
    elif board[0][1] == "O" or board[1][1] == "O" or board[2][1] == "O":
        print("Player 2 wins!")
        exit()
    elif board[0][2] == "O" or board[1][2] == "O" or board[2][2] == "O":
        print("Player 2 wins!")
        exit()
        
    
    #check diagonal wins
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("Player 1 wins!")
        exit()
    if board[2][0] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Player 1 wins!")
        exit()
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Player 2 wins!")
        exit()
    if board[2][0] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Player 2 wins!")
        exit()
    
    
#%%
#Baby Names
    
def Babynames(name):
    name_num = 0
    name = input("name")
    for num in range(1900, 2018):
        num = str(num)
        x = "data/names_" + num + ".txt"
        file = open(x, "r")
        line = file.readline()
        text = line.split("|")
        if text == name:
            name_num += 1
        print(name_num)
