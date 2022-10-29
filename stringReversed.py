def reverse_string(given_string):

    if len(given_string) == 1:

        return given_string

    else:

        return reverse_string(given_string[1:]) + given_string[0]

given_string = input()

result = reverse_string(given_string)

print(result)
