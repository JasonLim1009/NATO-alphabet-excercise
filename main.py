student_dict = {'student': ['Aida', 'Jason', 'Jenvice'], 'score': [56, 76, 98]}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#   print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    if row.student == 'Aida':
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
