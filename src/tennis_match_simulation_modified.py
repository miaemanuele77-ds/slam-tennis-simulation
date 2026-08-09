#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 00:49:10 2026

@author: miaemanuele
"""

import random

def slam_dice_game_mod():
    '''
    Simulates a complete game of Slam while recording
    performance measures including aces, double faults
    and average rally length.
    '''
    
    yellow_dice = random.randint(1, 6)

    victor = None
    result_type = None # added variable
    rally_length = 0 # added varable
    keep_going = True

    
    if yellow_dice == 1 or yellow_dice == 2:
        victor = 'server'
        result_type = 'ace'
        keep_going = False

    elif yellow_dice == 3:
        victor = 'receiver'
        result_type = 'double_fault'
        keep_going = False

    else:
        result_type = 'rally'

        while keep_going:

            blue_dice = random.randint(1, 6)
            rally_length += 1

            if blue_dice == 1:
                victor = 'receiver'
                keep_going = False

            elif blue_dice == 2:
                victor = 'server'
                keep_going = False

            else:
                red_dice = random.randint(1, 6)
                rally_length += 1

                if red_dice == 1:
                    victor = 'server'
                    keep_going = False

                elif red_dice == 2:
                    victor = 'receiver'
                    keep_going = False

    return victor, result_type, rally_length # return different values




def slam_mod_points_and_stats():
    '''
    Scoring for and tallying the outcomes of the 
    modified game of Slam. 
    '''
       
    server_points = 0
    receiver_points = 0

    ace_count = 0 # new variable
    double_fault_count = 0 # new variable
    rally_total = 0 # new variable
    rally_points = 0 # new variable

    first_point_winner = None # new variable
    winner = None # new variable
    keep_going = True

    while keep_going:

        victor, result_type, rally_length = slam_dice_game_mod()

        if first_point_winner is None:
            first_point_winner = victor

        if result_type == 'ace':
            ace_count += 1 # counting aces

        if result_type == 'double_fault':
            double_fault_count += 1 # counting double faults

        if rally_length > 0:
            rally_total += rally_length
            rally_points += 1 # counting rallies

       
        if victor == 'server':
            server_points += 1
        else:
            receiver_points += 1

        if server_points >= 4 and server_points >= receiver_points + 2:
            winner = 'server'
            keep_going = False

        elif receiver_points >= 4 and receiver_points >= server_points + 2:
            winner = 'receiver'
            keep_going = False

    game_stats = { # new dictionary to show stats
        'aces': ace_count,
        'double_faults': double_fault_count,
        'rally_total': rally_total,
        'rally_points': rally_points
    }

    return winner, first_point_winner, game_stats




#######################


def simulate_games(total_games):
    '''
    Running the game and calculating the averages
    of the two performance measures outcomes.
    '''
    
    games_15_0 = 0 # 15-0 stats
    server_wins_15_0 = 0
    aces_15_0 = 0
    df_15_0 = 0
    rally_len_15_0 = 0
    rally_pts_15_0 = 0

    
    games_0_15 = 0 # 0-15 stats
    server_wins_0_15 = 0
    aces_0_15 = 0
    df_0_15 = 0
    rally_len_0_15 = 0
    rally_pts_0_15 = 0

    for i in range(total_games):

        winner, first_point, stats = slam_mod_points_and_stats()

        # ---------------------------------- 
        # If game starts at 15-0
        # ---------------------------------- 
        if first_point == 'server':

            games_15_0 += 1

            if winner == 'server':
                server_wins_15_0 += 1

            aces_15_0 += stats['aces']
            df_15_0 += stats['double_faults']
            rally_len_15_0 += stats['rally_total']
            rally_pts_15_0 += stats['rally_points']

        # ---------------------------------- 
        # If game starts at 0-15
        # ---------------------------------- 
        else:

            games_0_15 += 1

            if winner == 'server':
                server_wins_0_15 += 1

            aces_0_15 += stats['aces']
            df_0_15 += stats['double_faults']
            rally_len_0_15 += stats['rally_total']
            rally_pts_0_15 += stats['rally_points']

    # ----------------------------------------------
    # Calculating averages for performance measures
    # ----------------------------------------------
    if rally_pts_15_0 > 0:
        avg_rally_15_0 = rally_len_15_0 / rally_pts_15_0
    else:
        avg_rally_15_0 = 0

    if rally_pts_0_15 > 0:
        avg_rally_0_15 = rally_len_0_15 / rally_pts_0_15
    else:
        avg_rally_0_15 = 0

    if games_15_0 > 0:
        server_dom_15_0 = server_wins_15_0 / games_15_0
    else:
        server_dom_15_0 = 0

    if games_0_15 > 0:
        server_dom_0_15 = server_wins_0_15 / games_0_15
    else:
        server_dom_0_15 = 0

    print('Total games simulated:', total_games)
    print('\n-- Games Starting 15-0 (Server has 1-point advantage) --')
    print('Games:', games_15_0)
    print('Server win rate:', server_dom_15_0)
    print('Total aces:', aces_15_0)
    print('Total double faults:', df_15_0)
    print('Average rally length:', avg_rally_15_0)

    print('\n-- Games Starting 0-15 (Receiver has 1-point advantage) --')
    print('Games:', games_0_15)
    print('Server win rate:', server_dom_0_15)
    print('Total aces:', aces_0_15)
    print('Total double faults:', df_0_15)
    print('Average rally length:', avg_rally_0_15)

    return



simulate_games(10000)




########################


def simulate_games(total_games):
    '''
    Scoring for and tallying the outcomes of the 
    modified game of Slam. 
    '''

    server_wins_0_0 = 0

    aces_0_0 = 0
    df_0_0 = 0
    rally_len_0_0 = 0
    rally_pts_0_0 = 0

    for i in range(total_games):

        winner, first_point, stats = slam_mod_points_and_stats()

        if winner == 'server':
            server_wins_0_0 += 1

        aces_0_0 += stats['aces']
        df_0_0 += stats['double_faults']
        rally_len_0_0 += stats['rally_total']
        rally_pts_0_0 += stats['rally_points']

    # ---------------------------------- 
    # Compute averages
    # ---------------------------------- 
    if rally_pts_0_0 > 0:
        avg_rally_length = rally_len_0_0 / rally_pts_0_0
    else:
        avg_rally_length = 0

    server_win_rate = server_wins_0_0 / total_games

    print('Total games simulated:', total_games)
    print('\n-- Games Starting from 0-0 --')
    print('Server win rate:', server_win_rate)
    print('Total aces:', aces_0_0)
    print('Total double faults:', df_0_0)
    print('Average rally length:', avg_rally_length)

    return

simulate_games(10000)




################
print('Aces per game (0-0):', 
      21844/10000)
print('Double faults per game (15-0):',
    10838/10000)

print('\nAces per game (15-0):', 
      13690/5873)
print('Double faults per game (15-0):',
      4994/5873)

print('\nAces per game (0-15):', 
      8231/4127)
print('Double faults per game (0-15):',
      5891/4127)







