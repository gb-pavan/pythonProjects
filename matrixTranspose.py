def get_transposed_matrix(given_matrix):

    transposed_matrix = []

    for column in range(len(given_matrix[0])):

        transposed_matrix.append([])

    for row_number in range(len(given_matrix)):

        for column_number in range(len(given_matrix[0])):

            transposed_matrix[column_number].append(given_matrix[row_number][column_number])

    return transposed_matrix



row , column = list(map(int, input().split()))

given_matrix = []

for each_row in range(row):

    row_matrix = list(map(int, input().split()))

    given_matrix.append(row_matrix[:column])
    
#print(matrix)

print(get_transposed_matrix(given_matrix))
