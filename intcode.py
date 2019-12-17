# Add:          opcode 1
# Multiply:     opcode 2
# Input:        opcode 3
# Output:       opcode 4


def calculate_modes(intcode, pointer, modes):
    # first parameter
    if modes[2] == 0:
        numberA = intcode[intcode[pointer + 1]]
    elif modes[2] == 1:
        numberA = intcode[pointer + 1]
    try:
        # if pointer < len(intcode)-1:
        # second parameter
        if modes[1] == 0:
            numberB = intcode[intcode[pointer + 2]]
        elif modes[1] == 1:
            numberB = intcode[pointer + 2]
    except:
        numberB = 'NA'
        print('WARN: no second mode')

    try:
        # third parameter
        if modes[0] == 0:
            positionC = intcode[pointer + 3]
        elif modes[0] == 1:
            positionC = pointer + 3
    except:
        positionC = 'NA'
        print('WARN: no third mode')

    return numberA, numberB, positionC


def execute_add(intcode, pointer, modes):
    numberA, numberB, positionC = calculate_modes(intcode, pointer, modes)
    intcode[intcode[pointer + 3]] = numberA + numberB
    pointer += 4
    return intcode, pointer


def execute_multiply(intcode, pointer, modes):
    numberA, numberB, positionC = calculate_modes(intcode, pointer, modes)
    intcode[intcode[pointer + 3]] = numberA * numberB
    pointer += 4
    return intcode, pointer


def get_input(text):
    return input(text)


def execute_input(intcode, pointer):
    user_input = get_input('Input ')
    # user_input = input('Input:')
    ## user input set to 1 for day 5 + tests for intcode!
    print('\nyour input: ', user_input)
    intcode[intcode[pointer + 1]] = int(user_input.strip())
    pointer += 2
    return intcode, pointer


def execute_output(intcode, pointer, modes):
    numberA, numberB, positionC = calculate_modes(intcode, pointer, modes)
    print("Output: ", numberA)
    pointer += 2
    return intcode, pointer, numberA


def execute_done(intcode):
    return intcode[0]


def execute_jump_if_true(intcode, pointer, modes):
    numberA, numberB, positionC = calculate_modes(intcode, pointer, modes)
    if numberA != 0:
        pointer = numberB
    else:
        pointer += 3
    return intcode, pointer


def execute_jump_if_false(intcode, pointer, modes):
    numberA, numberB, positionC = calculate_modes(intcode, pointer, modes)
    if numberA == 0:
        pointer = numberB
    else:
        pointer += 3
    return intcode, pointer


def execute_less_than(intcode, pointer, modes):
    numberA, numberB, positionC = calculate_modes(intcode, pointer, modes)
    if numberA < numberB:
        intcode[positionC] = 1
    else:
        intcode[positionC] = 0
    pointer += 4
    return intcode, pointer


def execute_equals(intcode, pointer, modes):
    numberA, numberB, positionC = calculate_modes(intcode, pointer, modes)
    if numberA == numberB:
        intcode[positionC] = 1
    else:
        intcode[positionC] = 0
    pointer += 4
    return intcode, pointer


def intcode(input_arr, day='na'):
    intcode = input_arr[:]
    pointer = 0

    while pointer <= len(intcode):
        # print(pointer, len(intcode))
        val = [int(x) for x in str(intcode[pointer])]
        operation = [0] * (5 - len(val)) + val
        opcode = int("".join(map(str, operation[-2:])))
        # print ('opcode', opcode)
        modes = operation[:3]

        if opcode == 99:
            if day == 2:
                return execute_done(intcode)
            else:
                return output

        if opcode == 1:
            # print('add')
            intcode, pointer = execute_add(intcode, pointer, modes)
            # print(intcode, pointer)

        if opcode == 2:
            # print('multiply')
            intcode, pointer = execute_multiply(intcode, pointer, modes)
            # print(intcode, pointer)

        if opcode == 3:
            intcode, pointer = execute_input(intcode, pointer)

        if opcode == 4:
            intcode, pointer, output = execute_output(intcode, pointer, modes)
            print(output)

        if opcode == 5:
            intcode, pointer = execute_jump_if_true(intcode, pointer, modes)

        if opcode == 6:
            intcode, pointer = execute_jump_if_false(intcode, pointer, modes)

        if opcode == 7:
            intcode, pointer = execute_less_than(intcode, pointer, modes)

        if opcode == 8:
            intcode, pointer = execute_equals(intcode, pointer, modes)

    return output
