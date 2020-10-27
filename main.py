import importlib
import sys

from handlers import error_handler
from helper_methods import pretty


@error_handler
def main():
    number = sys.argv[1]
    print(pretty(importlib.import_module(f'tasks.task_{number}').main()))


if __name__ == "__main__":
    main()
