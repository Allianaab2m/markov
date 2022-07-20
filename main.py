import MeCab
import re

text = open("./data.txt", "r").read()

table = str.maketrans(
    {
        # '\r': '',
        "(": "（",
        ")": "）",
        "[": "［",
        "]": "］",
        '"': "”",
        "'": "’",
    }
)

text = text.translate(table).split()
url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"

for i in range(10):
    for line in text:
        if re.match(url_pattern, line):
            text.remove(line)
        elif re.match("^@.*", line):
            text.remove(line)
        elif re.match(".*,$", line):
            text.remove(line)
        elif re.match("^#.*", line):
            text.remove(line)
        elif re.match("RT", line):
            text.remove(line)

m = MeCab.Tagger("-Owakati")
f = open("./new_data.txt", "w")
for line in text:
    splited_line = m.parse(line)
    f.write(str(splited_line))
f.close()
