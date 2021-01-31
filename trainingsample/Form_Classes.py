import pandas


def get_class_from_score(score: int) -> int:
    if 1 <= score <= 2.9: return 1
    if 3 <= score <= 5: return 2
    if 5.1 <= score <= 7: return 3


answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')
# X = numpy.zeros((5, 18))

# making classes
for i in range(len(answers_frame['O  '])):
    answers_frame['O  '][i] = get_class_from_score(answers_frame['O  '][i])

for i in range(len(answers_frame['C  '])):
    answers_frame['C  '][i] = get_class_from_score(answers_frame['C  '][i])

for i in range(len(answers_frame['E  '])):
    answers_frame['E  '][i] = get_class_from_score(answers_frame['E  '][i])

for i in range(len(answers_frame['A  '])):
    answers_frame['A  '][i] = get_class_from_score(answers_frame['A  '][i])

for i in range(len(answers_frame['N  '])):
    answers_frame['N  '][i] = get_class_from_score(answers_frame['N  '][i])

answers_frame.to_csv('../answerprocessing/answers.csv', index=False)

#####

dataset = answers_frame.values
X = dataset[:, 8:]
y_o = dataset[:, 3]
y_c = dataset[:, 4]
y_e = dataset[:, 5]
y_a = dataset[:, 6]
y_n = dataset[:, 7]
print(y_n)
