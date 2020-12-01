import importlib

from helper_methods import error_handler, pretty


@error_handler
def main():
    print_tasks()
    print('Введите номер задания: ', end='')
    task_number = input()
    task = importlib.import_module(f'tasks.task_{task_number}')
    answer = task.main()
    print(pretty(answer))


def print_tasks():
    print('1. Определить, на каких известных личностей подписан пользователь')
    print('2. Определить, на какие блоги подписан пользователь')
    print('3. Определить, насколько активно пользователь ведёт свою страницу')
    print('4. Получить геометки с последних публикаций пользователя')
    print('5. Получить максимальное/минимальное и среднее количество лайков по последним записям\n')  # noqa: E501


if __name__ == '__main__':
    main()
