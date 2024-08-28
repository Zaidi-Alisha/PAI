def check(input):
    vowels = "aeiouAEIOU"

    last = input.strip()[-1]

    if last.isalpha():
        if last in vowels:
            return "The last letter is a vowel."
        else:
            return "The last letter is a consonant."
    else:
        return "The last character is not a letter."


a = input("Enter a string: ")
result = check(a)
print(result)
