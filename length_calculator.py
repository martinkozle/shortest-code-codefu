def get_len(file_name):
    lines = []
    read_flag = False
    with open(file_name, mode="r", encoding="utf-8") as f:
        for line in f:
            if '# --' in line:
                read_flag = not read_flag
                continue
            if read_flag:
                lines.append(line)
    input_code = '\n'.join(lines)
    input_code = input_code.replace('\n', '')
    input_code = input_code.replace(' ', '')
    input_code = input_code.replace('\t', '')
    input_code = input_code.replace('\r', '')
    length = len(input_code)
    return 500 - length


if __name__ == '__main__':
    print(get_len('input.txt'))
