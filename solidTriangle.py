triangle_size = int(input())

for i in range(1, triangle_size + 1):

    for j in range(i, triangle_size):

        print("  ", end = "")

    for k in range(1, i + 1):

        print("* ", end = "")

    for l in range(1, i):

        print("* ", end = "")
        
    print()
