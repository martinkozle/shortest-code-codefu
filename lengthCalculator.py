input_code = "\n".join(open("input.txt", mode="r", encoding="utf-8").readlines())
print(500 - len(input_code.replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '')))
