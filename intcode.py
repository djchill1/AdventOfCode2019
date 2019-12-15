# Add:          opcode 1
# Multiply:     opcode 2
# Input:        opcode 3
# Output:       opcode 4

# opcode param lengths
num_params = {
    'ADD': 3,
    'MULTIPLY': 3,
    'INPUT': 1,
    'OUTPUT': 1
}

# opcode param modes
POSITION_MODE = 0
IMMEDIATE_MODE = 1



def execute_add(intcode, index):
    numberA = intcode[intcode[index + 1]]
    numberB = intcode[intcode[index + 2]]
    intcode[intcode[index + 3]] = numberA + numberB
    index += 4
    return intcode, index


def execute_multiply(intcode, index):
    numberA = intcode[intcode[index + 1]]
    numberB = intcode[intcode[index + 2]]
    intcode[intcode[index + 3]] = numberA * numberB
    index += 4
    return intcode, index


def execute_input(intcode, index):
    print("Input:")
    # user_input = input()
    user_input = '1'
    ## user input set to 1 for day 5 + tests for intcode!

    intcode[intcode[index + 1]] = int(user_input.strip())
    index += 2
    return intcode, index


def execute_output(intcode, index):
    print("Output: ", intcode[intcode[index + 1]])
    index += 2
    return intcode, index


def execute_done(intcode):
    return intcode[0]


def intcode(input_arr):
    intcode = input_arr[:]
    index = 0

    while index <= len(intcode):
        # print(index, len(intcode))
        opcode = intcode[index]
        # print ('opcode', opcode)

        if opcode == 99:
            return execute_done(intcode)

        if opcode == 1:
            # print('add')
            intcode, index = execute_add(intcode, index)
            # print(intcode, index)

        if opcode == 2:
            # print('multiply')
            intcode, index = execute_multiply(intcode, index)
            # print(intcode, index)

        if opcode == 3:
            intcode, index = execute_input(intcode, index)

        if opcode == 4:
            intcode, index = execute_output(intcode, index)

    return execute_done(intcode)
