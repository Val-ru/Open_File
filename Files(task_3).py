class File:
    files_info = []

    file = open('1.txt', encoding='utf-8')
    name = '1.txt'
    lines = 0
    for line in file:
        lines += 1

    files_info.append((name, lines))
    file.close()

    file = open('2.txt', encoding='utf-8')
    name = '2.txt'
    lines = 0
    for line in file:
        lines += 1

    files_info.append((name, lines))
    file.close()

    file = open('3.txt', encoding='utf-8')
    name = '3.txt'
    lines = 0
    for line in file:
        lines += 1

    files_info.append((name, lines))
    file.close()

    files_info.sort(key=lambda x: x[1])

    result = []
    for name, lines in files_info:
        result.append(name)
        result.append(lines)
        with open(name, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
            for line in all_lines:
                result.append(line)
    for line in result:
        print(str(line).strip())