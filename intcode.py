def intcode(input_arr):
    arr = input_arr[:]

    for index in range(0, len(arr), 4):
        operator = arr[index]

        if operator == 99:
            return arr[0]

        numberA = arr[arr[index + 1]]
        numberB = arr[arr[index + 2]]

        if operator == 1:
            arr[arr[index + 3]] = numberA + numberB

        if operator == 2:
            arr[arr[index + 3]] = numberA * numberB

    return arr[0]