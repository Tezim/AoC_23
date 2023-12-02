with open("input.txt", "r") as f:
    content = f.read().split('\n')
with open("input2.txt", "r") as f:
    content2 = f.read().split('\n')


def part1(content):
    RED = 12
    GREEN = 13
    BLUE = 14
    imp = []

    counter = 1
    for line in content:
        tmp = line.split(':')[1].split(';')
        for round in tmp:
            b, r, g = 0, 0, 0
            values = round.split(',')
            for v in values:
                v = v.split()
                if v[1] == 'blue':
                    b += int(v[0])
                elif v[1] == 'green':
                    g += int(v[0])
                elif v[1] == 'red':
                    r += int(v[0])
            if b > BLUE or r > RED or g > GREEN:
                imp.append(counter)
                break
        counter += 1

    games = list(range(1, len(content) + 1))
    print(sum([num for num in games if num not in imp]))


def part2(content):
    result = []
    for line in content:
        tmp = line.split(':')[1].split(';')
        b, r, g = 0, 0, 0
        for round in tmp:
            values = round.split(',')
            for v in values:
                v = v.split()
                if v[1] == 'blue' and int(v[0]) > b:
                     b = int(v[0])
                elif v[1] == 'green' and int(v[0]) > g:
                    g = int(v[0])
                elif v[1] == 'red' and int(v[0]) > r:
                    r = int(v[0])
        result.append(b*r*g)
    print(sum(result))


part1(content)
part2(content2)
