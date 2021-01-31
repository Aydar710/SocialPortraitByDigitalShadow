import pandas

from answerprocessing.TestResultParser import ANSWERS_CSV


def get_class_from_score(score: int) -> int:
    if 1 <= score <= 2.9: return 1
    if 3 <= score <= 5: return 2
    if 5.1 <= score <= 7: return 1


answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')
for item in answers_frame:
    print(item)
