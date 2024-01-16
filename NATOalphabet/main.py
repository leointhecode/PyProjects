import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# student_data_frame = pandas.DataFrame(student_dict)
#
# for (index, row) in student_data_frame.iterrows():
#     Access row.student or row.score

# TODO 1. Create a dictionary in this format:
NATO = pandas.read_csv('nato_phonetic_alphabet.csv')
NATO_dict = {row.letter: row.code for (index, row) in NATO.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    question = input("Type a word: ")
    try:
        if question == "":
            raise KeyError
        q_list = [NATO_dict[n.upper()] for n in question]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_phonetic()
    else:
        print(q_list)


generate_phonetic()
