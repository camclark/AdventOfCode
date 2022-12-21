# The following code was created by ChatGPT 21st Dec 2022
# You can also play with this tooling at https://chat.openai.com/chat
# What a time to be alive.

def find_start_of_packet(data):
    # Keep track of the last four characters seen
    last_four = []

    # Iterate through the data
    for i, c in enumerate(data):
        # Add the current character to the list of last four
        last_four.append(c)
        if len(last_four) > 4:
            last_four.pop(0)

        # Check if the last four characters are all different
        if len(set(last_four)) == 4:
            # Return the number of characters processed
            return i + 1

def find_start_of_message(data):
    # Keep track of the last 14 characters seen
    last_fourteen = []

    # Iterate through the data
    for i, c in enumerate(data):
        # Add the current character to the list of last fourteen
        last_fourteen.append(c)
        if len(last_fourteen) > 14:
            last_fourteen.pop(0)

        # Check if the last fourteen characters are all different
        if len(set(last_fourteen)) == 14:
            # Return the number of characters processed
            return i + 1

input_data = open("input.txt").read()
print("Part 1:", find_start_of_packet(input_data))
print("Part 2:", find_start_of_message(input_data))