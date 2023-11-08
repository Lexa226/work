def frequency_word(number_of_words: int, string: str) -> list[tuple[int, str]]:
    string = string.split()
    counted_words = [(string.count(word), word) for word in set(string)]
    return sorted(counted_words, reverse=True)[:number_of_words]


def info_print(result_data: list[tuple[int, str]], number_of_words: int) -> None:
    print(f"{number_of_words} самых часто встречаемых слов:\n")
    print(f"+{'-' * 38}+")
    print(f"|{'СЛОВО':^18}|{'ЧАСТОТА':^18} |")
    print(f"+{'-' * 38}+")
    for elem in result_data:
        print(f"|{elem[1]:^18}|{elem[0]:^18}|")
    print(f"+{'-' * 38}+")


def main():
    number_of_words = input('Кол-во самых часто встречаемых слов: ')
    string = input('Введите строку разделенную пробелами: ')
    if number_of_words.isdigit():
        result_data = frequency_word(int(number_of_words), string)
        info_print(result_data, int(number_of_words))
    else:
        print('Вы ввели некорректные данные!')


if __name__ == "__main__":
    main()

