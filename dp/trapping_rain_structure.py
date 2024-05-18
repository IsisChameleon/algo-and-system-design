"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

from collections import defaultdict

def store_potential(potentials, local_max_wall_height, wall_height):
    for level in range(wall_height, local_max_wall_height):
        print(f'Potentials[{level}]+=1')
        potentials[level] +=1

def gain_potential(potentials, local_max_wall_height):
    water = 0
    for level in range(0, local_max_wall_height):
        print(f'gain potential amount {potentials[level]} at level {level}')
        water += potentials[level]
        potentials[level]=0
    print(f'collected water for local_max_wall_height {local_max_wall_height}:', water)
    return water

def get_water_volume(trapping_array: list[int])->int:
    if trapping_array is None or len(trapping_array) < 3:
        return 0
    
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(f'                  {trapping_array}')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    
    #potentials = defaultdict(int)  #key = level
    potentials = [0]*100000
    current_wall_height =0 
    local_max_wall_height = 0
    global_max_wall_height = 0

    water = 0

    for wall_height in trapping_array:
        print(f'Array item {wall_height}')
        if wall_height > current_wall_height:
            
            local_max_wall_height = wall_height
            if wall_height > global_max_wall_height:
                global_max_wall_height = wall_height
            print(f'wall increase...local max {local_max_wall_height} global max {global_max_wall_height}')
            store_potential(potentials, global_max_wall_height, wall_height)
            water += gain_potential(potentials, local_max_wall_height)
        else:
            store_potential(potentials, global_max_wall_height, wall_height)

        print(f'potentials: {potentials}')
        current_wall_height = wall_height

    return water



        