# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import collections
import itertools
import kittehs_funkollection as kf

inp = "input.txt"
lines = kf.eat(inp)

def count_letters(word, c):
    cnter = collections.Counter(word)
    return c in cnter.values()

def find_diffs(word1, word2):
    diffs = []
    for i, _ in enumerate(word1):
        if word1[i] != word2[i]:
            diffs.append(i)
    return diffs

def solve():
    s2 = 0
    s3 = 0

    for line in lines:
        s2 += 1 if count_letters(line, 2) else 0
        s3 += 1 if count_letters(line, 3) else 0

    print(f"Part 1: {s2 * s3}")

    for word1, word2 in itertools.combinations(lines, 2):
        diffs = find_diffs(word1, word2)
        if len(diffs) == 1:
            print(f"Part 2: {word1[:diffs[0]] + word1[diffs[0] + 1:]}")
            break

solve()