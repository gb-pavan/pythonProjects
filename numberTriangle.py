triangle_size = int(input())

k = m = 0

for i in range(1, triangle_size + 1):

    for j in range(i, triangle_size):

        print("  ", end = "")

    k += 1
    
    for k in range(k, i + k):

        print(k, end = " ")

    m = k + 1
    
    for m in range(m, i + m - 1):

        print(m, end = " ") 

        k = m
        
    print()
