input_text = "\n".join(open("input.txt", mode="r", encoding="utf-8").readlines())
open('output.txt', mode='w', encoding='utf-8').write("\t".join(' ' * i for i in map(ord, input_text)))
