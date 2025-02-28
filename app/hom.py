def action_func(num1, cur_action, num2):
    if cur_action == '+':
        return num1 + num2
    if cur_action == '-':
        return num1 - num2
    if cur_action == '*':
        return num1 * num2
    try:
        if cur_action == '/':
            return num1 / num2
        if cur_action == '//':
            return num1 // num2
        if cur_action == '%':
            return num1 % num2
    except ZeroDivisionError:
        return 0


def main_func(line):
    line_list = line.split()
    first, action, second = line_list
    number1, number2 = int(first), int(second)
    if len(action) != 1:
        raise TypeError
    result = action_func(number1, action, number2)
    return result


total_result = 0

try:
    with open('calc.txt', 'r') as calc_file:
        for i_line in calc_file:
            try:
                total_result += main_func(i_line)
            except (ValueError, TypeError):
                print(f'Обнаружена ошибка в строке: {i_line[:-1]}')
                question = input('Хотите исправить? ').lower()
                if question == 'да':
                    corrected_string = input('Введите исправленную строку: ')
                    total_result += main_func(corrected_string)

        print('Сумма результатов:', total_result)

except FileNotFoundError:
    print('Файл не найден')