from collections import Counter

with open("input.txt", "r") as f:
    c1 = f.read().split('\n')
with open("input2.txt", "r") as f:
    c2 = f.read().split('\n')


def part1(content):
    points = 0
    for card in content:
        tmp = card.split(':')[1].split('|')
        winning = list(set(tmp[0].split()).intersection(tmp[1].split()))
        points += 2 ** (len(winning) - 1) if len(winning) > 0 else 0
    print(points)


pts = 0
ca = []


def part2(content, start, end):
    global pts
    global ca
    for i in range(start, end):
        tmp = content[i].split(':')[1].split('|')
        winning = list(set(tmp[0].split()).intersection(tmp[1].split()))
        ca.append(i)
        part2(content, i + 1, i + len(winning) + 1)


part1(c1)
# not the fastest one but it works
part2(c2, 0, len(c2))
print(len(ca))
