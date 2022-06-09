from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from src.Lista02_Classes.Exerc04.classExamManager import ExamManager
from src.Lista02_Classes.Exerc02.AppDate import apart
from string import ascii_lowercase
from random import choice


def answers_list():
    ans_list = list()
    for c in range(1, 16):
        while True:
            alt = input_number(f'Enter the answer to question {c}: ', str).lower().strip()
            if (alt in ascii_lowercase[:5]) and (alt != ''):
                ans_list.append(alt)
                break
            print('\033[31mOnly alternatives between A-E!!\033[m')
    return ans_list


def input_answers_list():
    exam_answers = list()
    for c in range(15):
        alt = choice(ascii_lowercase[:5])
        exam_answers.append(alt)
    stud_answers = answers_list()
    return ExamManager(stud_answers, exam_answers)


def main():
    apart('Welcome to Exam Manager', 50)
    main_exam = input_answers_list()
    while True:
        print('=' * 50)
        select = input_number(
            "1 - View answer for a specific question;\n"
            "2 - ;\n"
            "3 - ;\n"
            "4 - ;\n"
            "5 - ;\n"
            "6 - Exit.\n"
            "> ")

        if select == 1:
            while True:
                quest = input_number('> Enter the question number: ')
                ans = main_exam.question_answer(quest)
                if ans != 0:
                    print(f'\033[32mThe answer to question {quest} is {str(ans).upper()}.\033[m')
                    break
                print('\033[31mOnly enter numbers between 1-15!\033[m')


if __name__ == '__main__':
    main()
