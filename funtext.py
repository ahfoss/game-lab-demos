import markovify

# Get raw text as string.
with open("wizard_of_oz.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text, state_size = 3)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())
