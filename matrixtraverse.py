row, column = list(map(int, input().split()))

matrix = []

for each_row in range(row):

    row_matrix = list(map(int, input().split()))

    matrix.append(row_matrix[:column])

print()
print()    
print(matrix)
   
for line_num in range(row + column - 1):

    strt_ele_row = max(line_num - (column - 1) , 0)


    #print(strt_ele_row)

    ele_in_each_line = min(line_num, min((column - 1),(row - 1)), sum([(column - 1),(row - 1)]) - line_num) + 1

    #print(strt_ele_row)

    #print(ele_in_each_line, end = " ")

    for i in range(ele_in_each_line):

        new_row = strt_ele_row + i 

        new_column = max((column - 1) - line_num, 0) + i 

        #print(new_row)

        print(matrix[new_row][new_column], end = " ")

    print()
