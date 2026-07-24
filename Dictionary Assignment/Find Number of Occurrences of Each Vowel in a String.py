string = input("Enter a string: ").lower()

vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

for ch in string:
    if ch in vowels:
        vowels[ch] += 1

print("\nVowel Occurrences:")
for key, value in vowels.items():
    print(key, ":", value)