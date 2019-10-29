from collections import Counter

import timeit
import itertools


def timing(f):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        try:
            action = f(*args, **kwargs)
        except Exception:
            print('Function failed!')
        else:
            end_time = timeit.default_timer()
            print(end_time - start_time)
            return action

    return wrapper


def even_odd_iterator(iterator, even=True):
    start = 1 if even else 0
    for i in range(start, len(iterator), 2):
        yield iterator[i]


@timing
def one_two_sorting(numbers: list):
    one, two = numbers.count(1), numbers.count(2)
    return itertools.chain(itertools.repeat(2, two), itertools.repeat(1, one))
    # return [i for i in itertools.repeat(2, two)] + \
    #        [j for j in itertools.repeat(1, one)]


@timing
def palindrome(letters: str):
    diff_letters = Counter(letters)

    counter = 0
    for key, value in diff_letters.items():
        if value % 2 != 0:
            counter += 1
            if counter > 1:
                return False
    return True


for i in (one_two_sorting([1, 1, 1, 2, 2, 2])):
    print(i)
