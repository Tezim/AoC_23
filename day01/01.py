import re


with open("input.txt", "r") as f:
    content1 = f.readlines()

with open("input2.txt", "r") as f:
    content = f.readlines()


def part1(content):
    sum = 0
    d_ = []
    for line in content:
        line = list(line)
        d = ""
        for i in range(len(line)):
            if line[i].isdigit():
                d += line[i]
        if len(d) > 2:
            d = d[0] + d[len(d) - 1]
        if len(d) == 1:
            d += d
        d_.append(d)
        sum += eval(d)
    print(sum)


replacements = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"),
                ("eight", "8"), ("nine", "9"), ("ten", "10")]


def get_number(string):
    global replacements
    for str, num in replacements:
        if str == string:
            return num
    return None


def first_last(string):
    fisrt_i = None
    last_i = None
    for i, char in enumerate(string):
        if char.isdigit():
            if fisrt_i is None:
                fisrt_i = i
            last_i = i

    return fisrt_i, last_i


def extract(input_string, substrings):
    occurrences = []
    indexes = []
    for substring in substrings:
        start = 0
        while True:
            index = input_string.find(substring, start)
            if index == -1:
                break
            occurrences.append(substring)
            indexes.append(index)
            start = index + 1

    combined = list(zip(occurrences, indexes))
    sorted_ = sorted(combined, key=lambda x: x[1], reverse=False)
    occurrences = [item[0] for item in sorted_]
    return occurrences


def part2(content):
    substr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    new_content = []
    for line in content:
        numbers = extract(line, substr)
        f, l = first_last(line)
        if len(numbers) > 0:
            f_t = line.find(numbers[0])
            l_t = line.rfind(numbers[len(numbers) - 1])
            if f_t < f:
                to_replace_first = get_number(numbers[0])
                line = line.replace(numbers[0], to_replace_first)
            if l_t > l:
                to_replace_last = get_number(numbers[len(numbers) - 1])
                line = line.replace(numbers[len(numbers) - 1], to_replace_last)
        new_content.append(line)
    part1(new_content)

part1(content1)
part2(content)