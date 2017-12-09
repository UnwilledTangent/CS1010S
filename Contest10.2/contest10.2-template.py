#
# CS1010S --- Programming Methodology
#
# Contest 10.2 Template


from random import *
from puzzle_AI import *


def AI(mat):
    
    a = merge_left(mat), 'a'
    d = merge_right(mat), 'd'
    w = merge_up(mat), 'w'
    s = merge_down(mat), 's'

    states = [a,d,w,s]
    states = [state for state in states if state[0][1]]
    states.sort(key=lambda l: l[0][2], reverse=True)

    if len(states) == 1:
    	return states[0][-1]
    elif len(states) == 0:
    	return False

    elif len(states)==2:
    	try:
    		if AI(states[0][0][0]):
    			return states[0][-1]
    		elif AI(states[1][0][0]):
    			return states[1][-1]
    	except:
    		return states[0][-1] if states[0][0][1] else states[1][-1]

    elif len(states)==3:
    	try:
    		if AI(states[0][0][0]):
	    		return states[0][-1]
	    	elif AI(states[1][0][0]):
	    		return states[1][-1]
	    	elif AI(states[2][0][0]):
	    		return states[2][-1]
    	except:
	    	return states[0][-1]

    elif len(states)==4:
    	try:
    		if AI(states[0][0][0]):
	    		return states[0][-1]
	    	elif AI(states[1][0][0]):
	    		return states[1][-1]
	    	elif AI(states[2][0][0]):
	    		return states[2][-1]
	    	elif AI(states[3][0][0]):
	    		return states[3][-1]
    	except:
	    	return states[0][-1] if states[0][0][1] else states[1][-1]

# def AI(mat):
# 	a = merge_left(mat), 'a'
# 	d = merge_right(mat), 'd'
# 	w = merge_up(mat), 'w'
# 	s = merge_down(mat), 's'
# 	states.sort(key=lambda l: l[0][2], reverse=True)


    	



# UNCOMMENT THE FOLLOWING LINES AND RUN TO WATCH YOUR SOLVER AT WORK
# game_logic['AI'] = AI
# gamegrid = GameGrid(game_logic)

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
# Note: Your solver is expected to produce only valid moves.
get_average_AI_score(AI, True)

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]

def has_zero(mat):
    return 0 in flatten(mat)

def transpose(mat):
    return [[row[i] for row in mat] for i in range(len(mat[0]))]

def reverse(mat):
    return list(map(lambda l: l[::-1], mat))

def merge_left(mat):
    sum_inc = 0
    new_mat = []
    for row in mat:
        
        new_row = [elem for elem in row]
        for i in range(len(row)):
            pointer = i-1
            while pointer >=0:

                if new_row[pointer] == 0:
                    if pointer == 0:
                        new_row[pointer] = new_row[i]
                        new_row[i] = 0
                        break
                    pointer -= 1

                elif new_row[pointer] == new_row[i]:
                    new_row[pointer] = 2*new_row[pointer]
                    new_row[i] = 0
                    cursor = pointer-1
                    while cursor>=0 and new_row[cursor] == new_row[cursor+1]:
                        new_row[cursor] = 2*new_row[cursor]
                        new_row[cursor+1] = 0
                        cursor -= 1
                    break

                elif new_row[pointer]!=new_row[i]:
                    new_row[pointer+1] = new_row[i]
                    if pointer+1 < i:
                        new_row[i] = 0
                    break

        for i in range(len(new_row)):
            if new_row[i] > max(row[i:]):
                sum_inc += new_row[i]

        new_mat.append(new_row)
    
    is_valid = new_mat != mat
    return new_mat, is_valid, sum_inc


def merge_right(mat):
    m_state = merge_left(reverse(mat))
    return reverse(m_state[0]), m_state[1], m_state[2]


def merge_up(mat):
    m_state = merge_left(transpose(mat))
    return transpose(m_state[0]), m_state[1], m_state[2]


def merge_down(mat):
    m_state = merge_right(transpose(mat))
    return transpose(m_state[0]), m_state[1], m_state[2]
