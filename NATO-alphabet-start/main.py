import pandas

csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in csv_data.iterrows()}
wrong_input = True

while wrong_input:
    user_name = input("Enter your name: ").upper()
    try:
        nato_name_list = [nato_dict[letter] for letter in user_name]
    except KeyError:
        print("Sorry, Only letters in the alphabet please!!")
    else:
        print(nato_name_list)
        wrong_input = False


