# task 5
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes_adv(num, repeats=True):
    """Function to return jokes. num (int) - count of jokes """
    joke_list = []

    if not repeats:
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            return 'No way'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(num):
                joke_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')

    else:
        for i in range(num):
            cur_nouns = random.choice(nouns)
            cur_adverbs = random.choice(adverbs)
            cur_adjectives = random.choice(adjectives)
            joke_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return joke_list


n_jokes = int(input('Введите число n: '))
print(get_jokes_adv(n_jokes, False))
