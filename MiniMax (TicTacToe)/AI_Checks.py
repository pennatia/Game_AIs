# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 08:45:20 2019

@author: Samuel Fisher, Intern
Johns Hopkins University Applied Physics Laboratory
"""
from math import inf as infinity
import numpy as np
#Display who won and add to win counter

def whoWin(x,End,Xwin,Owin): 
    Xwin = 0
    Owin = 0
    if x == 1:
        End.configure(text="Player 1 has won!", background = 'white')
        Xwin = 1
    elif x == 2:
        End.configure(text="Player 2 has won!", background = 'white')
        Owin = 1
    else:
        End.configure(text="Nobody Wins", background = 'white')
    gameover = 1
    L = [Xwin,Owin,gameover]
    return L

#Check if there is a three in a row
#If there is a win, a display which team one and count that win
def checkWin(place,AIturn,End,Xwin,Owin,turn, aiSkill): 
    if place[1] == place[0] and place[0] == place[2] and place[1] != 0:
        print ("Player",place[1]," wins")
        return whoWin(place[1],End,Xwin,Owin)
    if place[0] == place[3] and place[0] == place[6] and place[0] != 0:
        print ("Player",place[0]," wins")
        return whoWin(place[0],End,Xwin,Owin)
    if place[0] == place[4] and place[0] == place[8] and place[0] != 0:
        print ("Player",place[0]," wins")
        return whoWin(place[0],End,Xwin,Owin)
    if place[1] == place[4] and place[1] == place[7] and place[1] != 0:
        print ("Player",place[1]," wins")
        return whoWin(place[1],End,Xwin,Owin)
    if place[2] == place[4] and place[2] == place[6] and place[2] != 0:
        print ("Player",place[2]," wins")
        return whoWin(place[2],End,Xwin,Owin)
    if place[2] == place[5] and place[2] == place[8] and place[2] != 0:
        print ("Player",place[2]," wins")
        return whoWin(place[2],End,Xwin,Owin)
    if place[3] == place[4] and place[3] == place[5] and place[3] != 0:
        print ("Player",place[3]," wins")
        return whoWin(place[3],End,Xwin,Owin)
    if place[6] == place[7] and place[8] == place[6] and place[6] != 0:
        print ("Player",place[6]," wins")
        return whoWin(place[7],End,Xwin,Owin)
    tie = 1
    for i in place:
        if i == 0:
            tie = 0
    if tie == 1:
        return whoWin(3,End,Xwin,Owin)
    return [0,0,0]

#Check who won without calling whoWin
#Necessary for MiniMax
def checkWin2(place):
    if place[1] == place[0] and place[0] == place[2] and place[1] != 0:
        return place[1]
    if place[0] == place[3] and place[0] == place[6] and place[0] != 0:
        return place[0]
    if place[0] == place[4] and place[0] == place[8] and place[0] != 0:
        return place[0]
    if place[1] == place[4] and place[1] == place[7] and place[1] != 0:
        return place[1]
    if place[2] == place[4] and place[2] == place[6] and place[2] != 0:
        return place[2]
    if place[2] == place[5] and place[2] == place[8] and place[2] != 0:
        return place[2]
    if place[3] == place[4] and place[3] == place[5] and place[3] != 0:
        return place[3]
    if place[6] == place[7] and place[8] == place[6] and place[6] != 0:
        return place[6]
    tie = 1
    for i in place:
        if i == 0:
            tie = 0
    if tie == 1:
        return 0
    return [0,0,0]

#######################################################################################################
## This is where I implement my goal based agent#######################################################
#######################################################################################################
def Goal_Based_Agent(place):
    winning_combos = [[0,1,2],
                    [3,4,5],
                    [6,7,8],
                    [0,3,6],
                    [1,4,7],
                    [2,5,8],
                    [0,4,8],
                    [2,4,6]]

    decision_order = [2,1]

    for mark in decision_order:
        for combo in winning_combos:
            if place[combo[0]] == 0 and place[combo[1]] == place[combo[2]] and place[combo[2]] == mark:
                return combo[0]
            if place[combo[1]] == 0 and place[combo[0]] == place[combo[2]] and place[combo[2]] == mark:
                return combo[1]
            if place[combo[2]] == 0 and place[combo[0]] == place[combo[1]] and place[combo[1]] == mark:
                return combo[2]

#######################################################################################################
## This is where I implement my minimax#######################################################
#######################################################################################################

def minimax(place, depth, is_Max):

    # Check whether a player wins

    # Return negative value if Player Wins
    if checkWin2(place) == 1:
        return -100, 0

    # Return positive value if AI wins
    elif checkWin2(place) == 2:
        return 100, 0

    # Return 0 with a draw
    elif checkWin2(place) == 0:
        return 0, 0 


    # Initiate the Maximizing Layer
    if is_Max:

        # Initiate Value to Maximize 
        BS = -1000
        bestmove = 0

        # Iterate through each board place
        for i in range(len(place)):
            if place[i] == 0:
                # Place AI mark
                place[i] = 2
                
                # Recursive Call, with Minimize (by having False)
                score = minimax(place,depth+1,False)[0]

                # Update Score, punishing depth
                score = score - depth
                place[i] = 0
                if(score > BS):
                    BS = score
                    bestmove = i
        return BS, bestmove
    
    if not is_Max:

        # Initiate Value to Minimize
        BS = 800
        bestmove = 0

        # Iterate through each board place
        for i in range(len(place)):
            if place[i] == 0:
                # Place AI mark
                place[i] = 1

                # Recursive Call, with Minimize (by having False)
                score = minimax(place,depth+1,True)[0]

                # Update Score, punishing depth
                score = score + depth
                place[i] = 0
                if(score < BS):
                    BS = score 
                    bestmove = i
        return BS, bestmove


    
