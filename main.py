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
    
def count_words(text):
    """Підраховує частоту слів у тексті та повертає словник {слово: кількість}."""
    words = text.lower().split()
    word_freq = {}
    
    for word in words:
        word = word.strip('.,!?():;"\'')
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
            
    return word_freq

