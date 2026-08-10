#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 00:38:15 2026

@author: miaemanuele
"""

# ==================================
# Simulation
# ==================================

import random

def slam_dice_game():
    '''
    Simulates a complete game of Slam using the official
    Slam dice rules and returns the winning player.
    '''
    
    print('\n-- New Point --')
    
    keep_going = True 
    

    
    yellow_dice = random.randint(1,6)
    print('Server rolls a', yellow_dice, 'with yellow dice')
    
    if (yellow_dice == 1 or yellow_dice == 2):
        keep_going = False
        victor = 'server'
        print('Ace winner, server wins point!')
        
    elif (yellow_dice == 3):
        keep_going = False
        victor = 'receiver'
        print('Double fault, receiver wins point!')
        
    else:
        print('Rally begins')
        
    
    while (keep_going):
        
        blue_dice = random.randint(1,6)
        print('Reciever rolls a', blue_dice, 'with blue dice')
        
        if (blue_dice == 1):
            keep_going = False
            victor = 'receiver'
            print('In! Receiver wins point!')
            
        elif (blue_dice == 2):
            keep_going = False
            victor = 'server'
            print('Out! Server wins point!')
            
        else:
            print("Receiver hits in, rally continues")
                
        
        if (keep_going):
            
            red_dice = random.randint(1,6) 
            print('Server rolls a', red_dice, 'with red dice')
        
            if (red_dice == 1):
                keep_going = False
                victor = 'server'
                print('In! Server wins point!')
            
            elif (red_dice == 2):
                keep_going = False
                victor = 'receiver'
                print('Out! Receiver wins point!')
            
            else: 
                print("Server hits in, rally continues")
        
    return victor


# ==================================
# Tennis Scoring
# ==================================

def slam_dice_game_points():
    '''
    Simulates a single point in a game of Slam and
    returns the winning player for that point.
    '''
    
    print("\n------------------------")
    print('New game begins')
    
    points = {0: "0", 1: "15", 2: "30", 3: "40"}
    server_points = 0
    receiver_points = 0
    keep_going = True
    
    
    
    while (keep_going):
        
        victor = slam_dice_game()
        if (victor == 'server'):
            server_points += 1
            
        else:
            victor == 'receiver'
            receiver_points += 1
        
        # ----------------------------------
        # Scoring if game reaches a deuce
        # ----------------------------------
        if (server_points >= 3 and receiver_points >= 3):
            if (server_points == receiver_points):
                print('Score: Deuce (40-40)')
                
            elif (server_points == receiver_points + 1):
                print('Score: Server has advantage')
                
            elif (receiver_points == server_points + 1):
                print('Score: Receiver has advantage')
                
            elif (server_points >= receiver_points + 2):
                print('Server wins the game!')
                print('\n-- Game over --')
                keep_going = False
                
            elif (receiver_points >= server_points + 2):
                print('Receiver wins the game!')
                print('\n-- Game over --')
                keep_going = False
        
        # ----------------------------------    
        # Scoring before/if no deuce
        # ----------------------------------
        else:
            if (server_points == 4):
                print('Server wins the game!')
                print('\n-- Game over --')
                keep_going = False
                
            elif (receiver_points == 4):
                print('Receiver wins the game!')
                print('\n-- Game over --')
                keep_going = False
                
            else:
                print('Score:',
                      points[server_points], "-",
                      points[receiver_points])
    return    
            
slam_dice_game_points()            
    



# ==================================
# Testing function
# ==================================
for i in range(20):
    slam_dice_game_points()
  
    
# ==================================
# Probability of server winning  
# ==================================
server_wins = 0
receiver_wins = 0

for i in range(500):
    winner = slam_dice_game()
    
    if winner == 'server':
        server_wins += 1
    else:
        receiver_wins += 1

print('Server:', server_wins)
print('Receiver:', receiver_wins)


# =====================================
# Probability of server winning if 0-0
# =====================================
print('Probability of server winning =', 307/500)
print('Probability of server winning =', 293/500)
print('Probability of server winning =', 292/500)
    

for _ in range(20):
    slam_dice_game_points()






