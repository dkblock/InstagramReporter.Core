import sys
import importlib


def run(number):
    module = importlib.import_module(f'tasks.{number}')
    module.main()


def main():
    number = ''
    try:
        number = sys.argv[1]
        if int(number) > 5 or int(number) < 1:
            print('Номер задачи находится в диапозоне от 1 до 5')
    except IndexError:
        sys.exit("Чтобы запустить приложение используйте комманду: 'python3 main.py <номер задания>'")  # noqa: E501
    importlib.import_module(f'tasks.{number}').main()


if __name__ == "__main__":
    main()
