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

def get_top_words(word_freq, top_n=10):
    """Повертає список із top_n найпопулярніших слів у форматі (слово, кількість)."""
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]

def write_results(top_words, output_file):
    """Записує результати у вихідний файл у форматі 'слово-кількість'."""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word, count in top_words:
                file.write(f"{word}-{count}\n")
        print(f"Результати записано у файл {output_file}")
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")

def main(input_file, output_file):
    """Основна функція для обробки файлу та запису результатів."""

    text = read_file(input_file)
    if not text:
        return
    
    word_freq = count_words(text)

    top_words = get_top_words(word_freq)

    write_results(top_words, output_file)

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    main(input_file, output_file)