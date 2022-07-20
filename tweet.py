import markovify

with open("./learned_data.json", "r") as f:
    text_model = markovify.Text.from_json(f.read())

print_txt = text_model.make_short_sentence(140)
while print_txt is None:
    print_txt = text_model.make_short_sentence(140)

print(print_txt)
