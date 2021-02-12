import pandas
import random

data = pandas.read_excel("final_data_multy_choise.xlsx")
data_length = len(data)
data_list = data.values.tolist()
print(data_list)
print(len(data_list))

# for index, row in data.iterrows():
#     print(index)
#     print(row["questions"], row["correct_answers"], row["wrong1"], row["wrong2"], row["wrong3"])

class QAndA:
    def __init__(self):
        self.question_num = 0
        self.q_list = data_list
        random.shuffle(self.q_list)
    def next_turn(self):
        self.question_num += 1

