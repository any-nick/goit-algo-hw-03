import os
import shutil
import argparse
from pathlib import Path

# ANSI код для кольорового виводу
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"

def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        # Використовуємо синій колір для директорій
        print(indent + prefix + COLOR_BLUE + str(path.name) + COLOR_RESET)
        indent += "    " if prefix else ""

        # Отримуємо список елементів, де спочатку файли, потім директорії
        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            # Перевіряємо, чи є поточний елемент останнім у директорії
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))


def copy_files_recursive(src: Path, dest: Path) -> None:
    try:
        # Перебираємо всі елементи у вихідній директорії
        for item in src.iterdir():
            if item.is_dir():
                # Рекурсивно обробляємо піддиректорії
                copy_files_recursive(item, dest)
            else:
                # Копіюємо файли у відповідну директорію за розширенням
                file_extention = item.suffix[1:] if item.suffix else "undefined"
                target_dir = dest / file_extention
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_dir / item.name)
    except Exception as e:
        print(f"Error processing {src}: {e}")


def main():
    # Парсимо аргументи командного рядка
    parser = argparse.ArgumentParser()
    parser.add_argument("src")
    parser.add_argument("dest", nargs="?", default="dist")
    args = parser.parse_args()

    src_path = Path(args.src).resolve()
    dest_path = Path(args.dest).resolve()

    # Перевіряємо, чи існує вихідна директорія
    if not src_path.is_dir():
        print(f"Directory '{src_path}' does not exist.")
        return

    # Викликаємо функцію копіювання файлів
    copy_files_recursive(src_path, dest_path)

    # Виводимо структуру директорій
    print(f"\n'{dest_path}'structure:")
    display_tree(dest_path)


if __name__ == "__main__":
    main()
