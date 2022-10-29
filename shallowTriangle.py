triangle_size = int(input()) 

for i in range(1, triangle_size  + 1):

    for j in range(1, i + 1):

        if j == 1 or j == i or i == triangle_size:

            print("* ", end = "")

        else:

            print("  ", end = "")
        
    print()

