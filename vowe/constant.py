string = "Hello World!"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string if char in vowels)
consonant_count = sum(1 for char in string if char.isalpha() and char not in vowels)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
