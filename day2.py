import pandas as pd
import numpy as np


### TASK 1 ###

# import the data that I saved as a csv
path = 'D:/'
day2 = pd.read_csv(path + 'day2_input.csv', header = 0)

# slit the game games into two cols, one result that the opponant plays, one that I play
day2[['opponant', 'you']] = day2['result'].str.split(' ', 1, expand=True)

# create columns that hold the amount of points the player got for playing that option
day2['opp_score'] = np.where(
    day2['opponant'] == 'A', 1, np.where(
        day2['opponant'] == 'B', 2, np.where(
            day2['opponant'] == 'C', 3, 0)))

day2['my_score'] = np.where(
    day2['you'] == 'X', 1, np.where(
        day2['you'] == 'Y', 2, np.where(
            day2['you'] == 'Z', 3, 0)))

# create column and populate with who wins the game based on the rules of the game
day2['outcome'] = np.where((
    ((day2['opp_score'] == 1) & (day2['my_score'] == 2)) |
    ((day2['opp_score'] == 2) & (day2['my_score'] == 3)) | 
    ((day2['opp_score'] == 3) & (day2['my_score'] == 1))),
    'i win',
        np.where(
            ((day2['opp_score'] == 1) & (day2['my_score'] == 1)) | 
            ((day2['opp_score'] == 2) & (day2['my_score'] == 2)) | 
            ((day2['opp_score'] == 3) & (day2['my_score'] == 3)),
        'draw',         
        np.where(
            ((day2['opp_score'] == 1) & (day2['my_score'] == 3)) | 
            ((day2['opp_score'] == 2) & (day2['my_score'] == 1)) | 
            ((day2['opp_score'] == 3) & (day2['my_score'] == 2)),
        'opp wins', 0))
)
 
# creating a column and allocating points to players based on the result of the game (6 for win, 3 or draw, 0 for loss)
day2['opp_outcome'] = np.where(
    day2['outcome'] == 'opp wins', 6, np.where(
        day2['outcome'] == 'draw', 3, np.where(
            day2['outcome'] == 'i win', 0, 0)))

day2['my_outcome'] = np.where(
    day2['outcome'] == 'opp wins', 0, np.where(
        day2['outcome'] == 'draw', 3, np.where(
            day2['outcome'] == 'i win', 6, 0)))

# combining the score from the option they chose + the outcome of the game
day2['opp_totalscore'] = day2['opp_score'] + day2['opp_outcome']
day2['my_totalscore'] = day2['my_score'] + day2['my_outcome']

# summing the total point that I achieved in the game
my_sum = day2['my_totalscore'].sum()
print(my_sum)

### TASK 2 ###

# creating another column for what the result should be
day2['required_outcome'] = day2['you']

# labeling the results
day2['outcome_label'] = np.where(
    day2['required_outcome'] == 'X', 'loss', np.where(
        day2['required_outcome'] == 'Y', 'draw', np.where(
            day2['required_outcome'] == 'Z', 'win', 0)))

# allocating what the play should be based on the result
day2['required_play'] = np.where((
    ((day2['outcome_label'] == 'win') & (day2['opponant'] == 'A')) |
    ((day2['outcome_label'] == 'draw') & (day2['opponant'] == 'B')) | 
    ((day2['outcome_label'] == 'loss') & (day2['opponant'] == 'C'))),
    'paper',
        np.where(
            ((day2['outcome_label'] == 'win') & (day2['opponant'] == 'B')) | 
            ((day2['outcome_label'] == 'draw') & (day2['opponant'] == 'C')) | 
            ((day2['outcome_label'] == 'loss') & (day2['opponant'] == 'A')),
        'scissors',         
        np.where(
            ((day2['outcome_label'] == 'win') & (day2['opponant'] == 'C')) | 
            ((day2['outcome_label'] == 'draw') & (day2['opponant'] == 'A')) | 
            ((day2['outcome_label'] == 'loss') & (day2['opponant'] == 'B')),
        'rock', 0))
)

# create column that hold the amount of points I got for playing that option
day2['my_score_2nd_rd'] = np.where(
    day2['required_play'] == 'rock', 1, np.where(
        day2['required_play'] == 'paper', 2, np.where(
            day2['required_play'] == 'scissors', 3, 0)))

# calculating my 2nd round outome points
day2['2nd_rd_outcome'] = np.where(
    day2['outcome_label'] == 'win', 6, np.where(
        day2['outcome_label'] == 'draw', 3, np.where(
            day2['outcome_label'] == 'loss', 0, 0)))

# combining the score from the option I chose + the outcome of the game
day2['totalscore_2nd_rd'] = day2['my_score_2nd_rd'] + day2['2nd_rd_outcome']

# summing the total point that I achieved in the game
my_sum = day2['totalscore_2nd_rd'].sum()
print(my_sum)

