import random


def generate_math_questions(a, b):
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice(['+', '-', '*', '/'])
    question = f"{num1} {operator} {num2}"
    return question


# expression = "2 + 3 * 4"
# result = eval(expression)
# print(result)  # Вывод: 14

# x = 10
# y = 20
# expression = "x + y"
# result = eval(expression)
# print(result)  # Вывод: 30

def check_answer(question, user_answer):
    try:
        user_answer = float(user_answer)
        return user_answer == eval(question)

    except ValueError:
        return False
        print('Функция проверки работает только с числами')


print(check_answer("2 + 3", "5"))
print(check_answer("5 * 3", "10"))
print(check_answer("10-3", "семь"))


def math_quiz(number_of_questions):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        question = generate_math_questions(1,5)
        user_answer = input(f'{question} = ')
        if check_answer(question, user_answer):
            correct_answers += 1

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers > 0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers > 0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


# Запуск теста
math_quiz(7)
