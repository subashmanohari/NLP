from nltk.tokenize import sent_tokenize, word_tokenize
example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."

for x in sent_tokenize(example_text):
    print(x)


for x in word_tokenize(example_text):
    print(x)
