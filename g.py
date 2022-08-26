from colorama import Back
def Output(table, guide_column, guide_row):
    for i, row in enumerate(table):
        for j in range(12):
            if j != guide_column:
                print(f'{"+":-<7}', end='')
            else:
                print('+', end='')
                print(Back.WHITE + f'{"":-<6}', end='')
                print(Back.RESET, end='')
        print('+')
        for j, value in enumerate(row):
            if isinstance(value, float):
                value = round(value, 2)
            if i == guide_row:
                print(Back.WHITE + f'|{value:^6}', end='')
                print(Back.RESET, end='')
            elif j == guide_column:
                print('|', end='')
                print(Back.WHITE + f'{value:^6}', end='')
                print(Back.RESET, end='')
            else:
                print(f'|{value:^6}', end='')
        if i == guide_row:
            print(Back.WHITE + '|', end='')
            print(Back.RESET)
        else:
            print('|')
    for j in range(12):
        if j != guide_column:
            print(f'{"+":-<7}', end='')
        else:
            print('+', end='')
            print(Back.WHITE + f'{"":-<6}', end='')
            print(Back.RESET, end='')
    print('+')
    print()
def calculate_delta(table):
    for i in range(2, 3):
        for j in range(4, 9):
            count_m = 0
            count_num = 0
            if type(table[i][2]) == str:
                count_m += table[i][j]
            else:
                count_num += table[i][2] * table[i][j]
            if type(table[i+1][2]) == str:
                count_m += table[i+1][j]
            else:
                count_num += table[i+1][2] * table[i+1][j]
            count_num -= table[0][j]
            table[4][j] = count_num
            table[5][j] = count_m
    for i in range(2, 3):
        for j in range(9, 11):
            count_m = 0
            count_num = 0
            if type(table[i][2]) == str:
                count_m += table[i][j]
            else:
                count_num += table[i][2] * table[i][j]
            if type(table[i+1][2]) == str:
                count_m += table[i+1][j]
            else:
                count_num += table[i+1][2] * table[i+1][j]
            count_m -= 1
            table[4][j] = count_num
            table[5][j] = count_m
    count_m = 0
    count_num = 0
    if type(table[2][2]) == str:
        count_m += table[2][3]
    else:
        count_num += table[2][2] * table[2][3]
    if type(table[3][2]) == str:
        count_m += table[3][3]
    else:
        count_num += table[3][2] * table[3][3]
    table[4][3] = count_num
    table[5][3] = count_m
    return table
def calculate_theta(table, column):
    for i in range(2, 4):
        if table[i][column] > 0:
            table[i][11] = table[i][3] / table[i][column]
def continue_iterations(table):
    for i in range(4, 11):
        if round(table[4][i], 3) > 0 and round(table[5][i], 3) > 0 or round(table[4][i], 3) < 0 and round(table[5][i], 3) > 0:
            return True
    return False
def func(table, column, row):
    table = table[::]
    guide_element = table[row][column]
    for i in range(3, 11):
        table[row][i] = table[row][i] / guide_element
    for i in range(2, 4):
        if i != row:
            temp = table[i][column]
            for j in range(3, 11):
                table[i][j] -= table[row][j] * temp
    table[row][1] = table[1][column]
    table[row][2] = table[0][column]
    calculate_delta(table)
    guide_column = 4
    for i in range(5, 11):
        if table[5][i] > table[5][guide_column]:
            guide_column = i
        elif table[5][i] == table[5][guide_column] and table[4][i] > table[4][guide_column]:
            guide_column = i
    calculate_theta(table, guide_column)
    guide_row = -1
    for i in range(2, 4):
        if table[i][11] and guide_row == -1:
            guide_row = i
        elif table[i][11] and table[i][11] < table[guide_row][11]:
            guide_row = i
    return table, guide_column,guide_row
F = [4, -2, 1, 0, 0]
a1 = [-2, -1, 1, -1, 0]
a2 = [-1, -3, -1, 0, -1]
b1 = 2
b2 = 10
table = [
    ['', '', '', '', *F, 'M', 'M', ''],
    ['i', 'Base', 'C', 'X', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', '\u0398'],
    ['1', 'x6', 'M', b1,  *a1, 1, 0, ''],
    ['2', 'x7', 'M', b2, *a2, 0, 1, ''],
    ['3', 'j', '', '', '', '', '', '', '', '', '', ''],
    ['4', 'j', '', '', '', '', '', '', '', '', '', ''],
]
Output(table, -1, -1)
print()
calculate_delta(table)
guide_column = 4
for i in range(5, 11):
    if table[5][i] > table[5][guide_column]:
        guide_column = i
    elif table[5][i] == table[5][guide_column] and table[4][i] > table[4][guide_column]:
        guide_column = i
calculate_theta(table, guide_column)
guide_row = -1
for i in range(2, 4):
    if table[i][11] and guide_row == -1:
        guide_row = i
    elif table[i][11] and table[i][11] < table[guide_row][11]:
        guide_row = i
Output(table, guide_column, guide_row)
while True:
    new_table, guide_column, guide_row = func(table, guide_column, guide_row)
    Output(table, guide_column, guide_row)
    table = new_table
    if not continue_iterations(table):
        break
