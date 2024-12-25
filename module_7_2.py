def custom_write(file_name, strings):

    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, line in enumerate(strings, start=1):
            start_position = file.tell()
            file.write(line + '\\n')
            strings_positions[(i, start_position)] = line

    # Возвращаем словарь с позициями
    return strings_positions

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Вывод результата
for elem in result.items():
    print(elem)