import importlib

from helper_methods import check_next_task, error_handler, pretty, print_tasks, sign_in


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


if __name__ == '__main__':
    main()
