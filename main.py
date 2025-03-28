def read_file(file_path):
    """Зчитує вміст текстового файлу та повертає його як рядок."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено!")
        return ""
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return ""