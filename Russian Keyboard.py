from random import seed, randrange

def end(e, r):
    print("Exiting program!")
    exit

def eng(e, r):
    print("Type '0' to exit game.")
    guess = "a"
    while guess != '0':
        seed()
        n = randrange(0, 65)
        print("Russian Letter:", r[n])
        guess = str(input("English Letter: "))
        if e[n] == guess:
            print("Correct!")
        else:
            print("Incorrect!  Letter:", e[n])
        print()

    end(e, r)

def rus(e, r):
    print("Type '0' to exit game.")
    guess = "a"
    while guess != '0':
        seed()
        n = randrange(0, 65)
        print("Russian Letter:", r[n])
        guess = str(input("Russian Letter: "))
        if r[n] == guess:
            print("Correct!")
        else:
            print("Incorrect!  Letter:", e[n])
        print()

    end(e, r)


def main():
    russian = ["ё", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю",
               "Ё", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю"]
    english = ["`", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "z", "x", "c", "v", "b", "n", "m", ",", "."
               "~", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", '"', "Z", "X", "C", "V", "B", "N", "M", "<", ">"]
    mode = 0
    
    print("Mode options:")
    print("1 - Enter English")
    print("2 - Enter Russian")
    print("0 - Exit")

    choice = int(input("\nMode: "))
    print()

    modes = {0 : end,
             1 : eng,
             2 : rus,
    }

    modes[choice](english, russian)

if __name__ == "__main__":
    main()

