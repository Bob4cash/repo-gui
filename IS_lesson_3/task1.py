# task 1-2
eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(eng_word):
    if eng_word[0].isupper():
        eng_word = eng_word.lower()
        if eng_rus_dict.get(eng_word) is None:
            return None
        else:
            return eng_rus_dict.get(eng_word).capitalize()
    else:
        return eng_rus_dict.get(eng_word)


new_word = input('Введите число от 1 до 10 на английском: ')
print(num_translate_adv(new_word))
