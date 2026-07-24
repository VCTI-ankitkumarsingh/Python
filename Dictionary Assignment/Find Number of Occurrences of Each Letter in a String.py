string = input("Enter a string: ")

count = {}

for ch in string:
    if ch.isalpha():
        ch = ch.lower()
        count[ch] = count.get(ch, 0) + 1

print("\nLetter Occurrences:")
for key, value in sorted(count.items()):
    print(key, ":", value)