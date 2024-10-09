"""
ID: psparip1
LANG: PYTHON3
TASK: ride
"""


def ufo(a, b):
    words = [a, b]
    results = []
    for i in range(len(words)):
        elem = words[i].upper()
        elem_list = [x for x in elem]
        assert len(elem_list) <= 6, "There should less than 6 characters."
        multiplier = 1
        for x in elem_list:
            b = ord(x) - 64
            multiplier *= b
        assert multiplier != 0, "The number should be divisible."
        results.append(multiplier % 47)
        del elem_list, multiplier
    if len(set(results)) == 1:
        return "GO"
    else:
        return "STAY"


if __name__ == '__main__':
    word1 = str(input())
    word2 = str(input())
    with open('ride.out', 'w') as f:
        f.write(ufo(word1, word2))
        f.close()