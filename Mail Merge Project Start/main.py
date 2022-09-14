with open("./input/letters/starting_letter.txt", 'r') as f:
    letter = f.read()
    print(letter)
with open("./input/names/invited_names.txt", 'r') as invited:
    # name = invited.readline()
    # print(name)
    # names = invited.readlines()
    # print(names)
    for names in invited.readlines():
        generated_file_name = "letter_to_" + names.strip("\n") + ".txt"
        new_letter = letter.replace("[name]", names.strip("\n"))
        # print(new_letter)
        final_file_path = "./output/ReadyToSend/"+generated_file_name
        with open(final_file_path, 'w') as ready_to_send:
            ready_to_send.write(new_letter)

