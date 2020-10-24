import importlib
import sys

from handlers import error_handler


@error_handler
def main():
    number = sys.argv[1]
    importlib.import_module(f'tasks.task_{number}').main()


if __name__ == "__main__":
    main()
