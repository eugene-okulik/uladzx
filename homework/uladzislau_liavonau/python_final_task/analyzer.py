import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Путь к папке с файлами")
parser.add_argument("--text", help="Текст для поиска", required=True)
args = parser.parse_args()


# Функция для поиска текста в файлах и вывода части строки
def search_in_files(directory, search_text):
    # Определение пути к каждому файлу в директории
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            with open(file_path, 'r', encoding='utf-8') as file:
                for index, line in enumerate(file, start=1):

                    # Проверка на наличие текста в строке
                    if search_text in line:
                        print(f"Текст найден в файле '{file_name}', строка {index}: \n"
                              f"{extract_text_fragment(line, search_text)}")


def extract_text_fragment(line, search_text):
    # Проверка на наличие текста в строке
    if search_text not in line:
        return line

    # Разделение строки на слова, сохраняя разделители
    words = re.split(r'(\W+)', line)

    # Определение индекса слова, которое содержится в тексте
    word_index = None
    for i, word in enumerate(words):
        if search_text in word:
            word_index = i
            break

    if word_index is None:
        return line

    # Форматирование строки: 5 слов до найденного слова, найденное слово, 5 слов после найденного слова
    start_index = max(0, word_index - 10)  # 5 слов перед текстом (с учётом разделителей)
    end_index = min(len(words), word_index + 11)  # 5 слов после текста (с учётом разделителей)

    # Создание фрагмента строки
    fragment = ''.join(words[start_index:end_index]).strip()

    return fragment


search_in_files(args.directory, args.text)
