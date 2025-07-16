class File:

    files_info = []
    files = ['1.txt', '2.txt', '3.txt']
    for f in files:
        file = open(f, encoding='utf-8')
        name = f
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