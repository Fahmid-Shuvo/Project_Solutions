numbers_found = 0
happy_numbers = []
i = 1
while numbers_found != 8:
    j = i
    print "i = ", i
    string_number = str(i)
    sum_of_squares = 0
    while True:
        for k in string_number:
            sum_of_squares += int(k) ** 2
        if sum_of_squares == i and i != 1:
            break
        if sum_of_squares == 1:
            happy_numbers.append(i)
            numbers_found += 1
            break
        string_number = str(sum_of_squares)
        sum_of_squares = 0
    i += 1

print happy_numbers
