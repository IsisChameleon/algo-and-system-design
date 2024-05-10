"""
Best Seat

You walk into a theatre you're about to see a show in. 
The usher within the theatre walks you to your row and mentions you're allowed to sit anywhere within the given row. 
Naturally you'd like to sit in the seat that gives you the most space. You also would prefer 
this space to be evenly distributed on either side of you (e.g. if there are three empty seats in a row, 
you would prefer to sit in the middle of those three seats).

Given the theatre row represented as an integer array, return the seat index of where you should sit. 
Ones represent occupied seats and zeroes represent empty seats.

You may assume that someone is always sitting in the first and last seat of the row. 
Whenever there are two equally good seats, you should sit in the seat with the lower index. 
If there is no seat to sit in, return -1. 
The given array will always have a length of at least one and contain only ones and zeroes.
"""

def bestSeat(seats):
    # Write your code here.
    if sum(seats) == len(seats):
        # no space 
        return -1

    best_spot = -1
    in_hole=False
    max_holes_counter=0
    start_current_hole=-1
    
    for i in range(len(seats)):
        if seats[i]==0:
            if in_hole==False:
                in_hole=True
                start_current_hole=i
                holes_counter=1
            else:
                holes_counter+=1
        else:
            if in_hole==True:
                in_hole=False
                if holes_counter > max_holes_counter:
                    max_holes_counter=holes_counter
                    if holes_counter//2 != holes_counter/2:
                        best_spot=start_current_hole+holes_counter//2
                    else:
                        best_spot=start_current_hole-1+holes_counter//2

        print(f'{seats}: index {i} in_hole {in_hole} start_current_hole {start_current_hole} max {max_holes_counter}')

        print(f'best_spot: {best_spot}')
                
    return best_spot