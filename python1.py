s = input("Enter a string: ")
words = s.split()
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)
result = " ".join(unique_words)

print("String after removing duplicate words:")
print(result)
