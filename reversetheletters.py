sentence = input()
sentence = sentence.split()
length = len(sentence)
new_sentence = ""
for i in range(length):
    character = sentence[i]
    character = character[ : : -1]
    new_sentence = new_sentence + character + " "

print(new_sentence)