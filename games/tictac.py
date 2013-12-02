#Tic Tac Toe game defs
def check_rows(array):
    if array[0] == array[1] == array[2]:
        return array[0]
    if array[3] == array[4] == array[5]:
        return array[3]
    if array[6] == array[7] == array[8]:
        return array[8]
    return 0

def check_columns(array):
    if array[0] == array[3] == array[6]:
        return array[0]
    elif array[1] == array[4] == array[7]:
        return array[1]
    elif array[2] == array[5] == array[8]:
        return array[8]
    else:
        return 0


def check_diagonals(array):
    if array[0] == array[4] == array[8]:
        return array[0]
    elif array[2] == array[4] == array[6]:
        return array[2]
    else:
        return 0


def get_first_empty_move(array):
    for i in range (0,9):
        if array[i] == 0:
            return i
    return -1
