def rule_append(arr):
    if len (arr) < 8:
        while 8 != len (arr):
            arr.insert(0,'0')
    return arr

def decimal_to_binary_arr(number):
    binary_string = bin(int(number))
    arr = [i for i in binary_string[2:]]
    arr = rule_append(arr)
    return arr

cases = ['***','**_','*_*','*__','_**','_*_','__*','___']
symbols = ['*','_']
str_to_check = ''
temp_automat = ''




def is_alive(str,rule):
    case = cases.index(str)
    state = rule[int(case)]
    if state == '1':
        return True
    return False


def check_next_state(content,rule):
    automat_content = content
    global temp_automat
    temp_automat = ''
    len_of_content = len(content)

    for i in range(0,len_of_content):
        if i == 0:
            str_to_check = automat_content[len_of_content-1] + automat_content[0] + automat_content[1]
        elif i == len_of_content-1:
            str_to_check = automat_content[i-1] + automat_content[i] + automat_content[0]
        else:
            str_to_check = automat_content[i-1] + automat_content[i] + automat_content[i+1]

        if is_alive(str_to_check,rule):
            temp_automat += '*'
        else:
            temp_automat += '_'


def return_new_automat_content():

    global temp_automat
    new_automat_content = temp_automat
    return new_automat_content

# print("to jest wywolywane !")