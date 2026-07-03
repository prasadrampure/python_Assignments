def Checkvowel(Character):
    if (Character == "A" or Character == "a" or
        Character == "E" or Character == "e" or
        Character == "I" or Character == "i" or
        Character == "O" or Character == "o" or
        Character == "U" or Character == "u"):
        return True
    else:
        return False

def main():
    Character = input('Enter a character:')

    Ret = Checkvowel(Character)
    if (Ret == True):
        print("The character is a vowel")
    else:
        print("The character is not a vowel")


if __name__ == "__main__":
    main()