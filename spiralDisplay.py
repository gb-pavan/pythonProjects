def print_spiral_elements(given_matrix):
    first_row_index = 0
    last_column_index = len(given_matrix[0]) - 1
    last_row_index = len(given_matrix) - 1 
    first_column_index = 0

    while True:
        if first_column_index > last_column_index:
            break

        for each_column in range(first_column_index, last_column_index + 1):
            print(given_matrix[first_row_index][each_column])
        first_row_index += 1 
        
        if first_row_index > last_row_index:
            break 

        for each_row in range(first_row_index, last_row_index + 1):
            print(given_matrix[each_row][last_column_index])
        last_column_index -= 1

        if first_column_index > last_column_index:
            break
        
        for each_column in range(last_column_index, first_column_index - 1, -1):
            print(given_matrix[last_row_index][each_column])
        last_row_index -= 1 

        if first_row_index > last_row_index:
            break
        for each_row in range(last_row_index, first_row_index - 1, -1):
            print(given_matrix[each_row][first_column_index])
        first_column_index += 1 
        




row , column = list(map(int, input().split()))

given_matrix = []

for each_row in range(row):

    row_matrix = list(map(int, input().split()))

    given_matrix.append(row_matrix[:column])
    
#print(matrix)

print_spiral_elements(given_matrix)
