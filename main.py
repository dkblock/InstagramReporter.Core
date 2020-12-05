import importlib
import sys

from helper_methods import error_handler, pretty, sign_in


@error_handler
def main():
    api = sign_in()
    while True:
        print_tasks()
        print('Введите номер задания: ', end='')
        task_number = input()
        task = importlib.import_module(f'tasks.task_{task_number}')
        answer = task.main(api)
        print(pretty(answer))
        check_next_task()


def print_tasks():
    print('\n1. Определить, на каких известных личностей подписан пользователь')
    print('2. Определить, на какие блоги подписан пользователь')
    print('3. Определить, насколько активно пользователь ведёт свою страницу')
    print('4. Получить геометки с последних публикаций пользователя')
    print('5. Получить максимальное/минимальное и среднее количество лайков по последним записям\n')  # noqa: E501


def check_next_task():
    print('\nПродолжить? Y/N (да/нет): ', end='')
    answer = input()
    if answer.lower() == 'n':
        sys.exit()
    elif answer.lower() != 'y':
        print('Ошибка! Введите Y/N!')
        check_next_task()


if __name__ == '__main__':
    main()
