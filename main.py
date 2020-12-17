import importlib

from helper_methods import check_next_task, error_handler, get_user_ids, pretty, print_tasks, sign_in  # noqa: E501


@error_handler
def main():
    api = sign_in()
    user_ids = get_user_ids(api)
    while True:         
        print_tasks()
        print('Введите номер задания: ', end='')
        task_number = input()
        try:
            task = importlib.import_module(f'tasks.task_{task_number}')
        except ModuleNotFoundError:
            print('Номер задания должен быть в диапазоне от 1 до 5')
            continue
        answer = task.main(api, user_ids)
        print(pretty(answer))
        check_next_task()


if __name__ == '__main__':
    main()
