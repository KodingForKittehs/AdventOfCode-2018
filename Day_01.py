# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import itertools
import kittehs_funkollection as kf

inp = "input.txt"
lines = [int(line) for line in kf.eat(inp)]

print(f"Part 1: {sum(lines)}")

p2sum = 0
seen = set([p2sum])
for line in itertools.cycle(lines):
    p2sum += line
    if p2sum in seen:
        print(f"Part 2: {p2sum}")
        break
    seen.add(p2sum)

