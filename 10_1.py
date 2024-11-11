def write_words(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f'Какое-то слово № 1')


print(write_words('example1.txt'))


from time import sleep
import time
from pprint import pprint


def write_words(word_count, file_name):
    count = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        while count < word_count:
            count += 1
            file.write(f'\nКакое-то слово № {count}')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


print(write_words(10, 'example1.txt'))
print(write_words(30, 'example2.txt'))
print(write_words(200, 'example3.txt'))
print(write_words(100, 'example4.txt'))
