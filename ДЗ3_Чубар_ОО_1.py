from pathlib import Path
import shutil
import sys

def copy_and_sort_files(source_dir, dest_dir=Path('dist')):
    # Створюємо директорію призначення, якщо вона ще не існує
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Рекурсивно перебираємо всі файли та піддиректорії у вихідній директорії
    for item in Path(source_dir).iterdir():
        if item.is_dir():
            copy_and_sort_files(item, dest_dir) # Рекурсивний виклик функції
        elif item.is_file(): # Отримуємо розширення файлу
            ext = item.suffix
            if ext:
                ext_dir = dest_dir / ext.strip('.').lower()
                ext_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy(str(item), str(ext_dir))  # Копіюємо файл у директорію на основі його розширення

def main():
    if len(sys.argv) < 2:
        print("Використання: python script.py <source_directory> [<destination_directory>]")
        sys.exit(1)
    
    source_directory = Path(sys.argv[1])
    destination_directory = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')
    
    try:
        copy_and_sort_files(source_directory, destination_directory)
        print(f"Файли було успішно скопійовано та відсортовано в директорію {destination_directory}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()
    
