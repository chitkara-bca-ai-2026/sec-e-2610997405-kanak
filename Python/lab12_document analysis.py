sentence = input("Enter a sentence: ")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

letters = vowels + consonants
vowel_percentage = (vowels / letters) * 100

print("=" * 44)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 44)
print("Sentence:", sentence)
print("Total characters:", len(sentence))

print()
print("--- Character Breakdown ---")
print("Words:             ", words)
print("Vowels:            ", vowels)
print("Consonants:        ", consonants)
print("Digits:            ", digits)
print("Spaces:            ", spaces)
print("Special characters:", special)

print()
print("--- Summary ---")
print("Total letters:", letters)
print(f"Vowel percentage: {vowel_percentage:.1f}%")

print()
print("=" * 44)
print("Analysis Complete!")
print("=" * 44)