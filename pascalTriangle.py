triangle_size = int(input())

pascal_triangle_list = []

for each_row in range(triangle_size):

    each_row_elements_list = []

    for each_column in range(each_row ):

        if each_column == 0 or each_column == each_row - 1:

            each_row_elements_list.append(1)

        else:

            each_row_elements_list.append(pascal_triangle_list[each_row - 1][each_column - 1] + pascal_triangle_list[each_row - 1][each_column])
            
    pascal_triangle_list.append(each_row_elements_list)

for each_sub_list in pascal_triangle_list:

    for i in range(len(each_sub_list)):

        print(each_sub_list[i], end = " ")

    print()

     
