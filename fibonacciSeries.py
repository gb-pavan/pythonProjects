def fibonacci_series(nth_term):

    if nth_term == 1:

        return 0

    elif nth_term == 2:

        return 1 

    else:

        previous_term = 1

        next_previous_term = 0 

        i = 2

        while i < nth_term:

            next_term = previous_term + next_previous_term

            next_previous_term = previous_term 

            previous_term = next_term 

            i += 1 

        return next_term 

nth_term = int(input())

result = fibonacci_series(nth_term)

print(result)
