from random import seed, randrange
import os

def end(played, correct):
    print("Exiting program!")
    try:
        print("You got {} out of {} correct!".format(correct, played))
        print("Your accuracy was {}%.".format(correct / played * 100))
    except:
        exit   
    exit

def eng(e, r):
    guess = "a"
    status = ["Incorrect", "Correct!"]
    played = 0
    correct = 0
    s = 0
    while guess != '0':
        screen_clear()
        print("Type '0' to exit game.")
        
        if played == 0:
            print("Давай начнем!")
        else:
            print("\nPrevious Round --", status[s])
            print("----------------")
            print("Prompt:", r[n])
            print("Guess:", guess)
            print("Correct:", e[n])
            print()
            
        seed()
        n = randrange(0, 66)
        print("Russian Prompt:", r[n])
        guess = str(input("English Letter: "))
        if e[n] == guess:
            s = 1
            correct += 1
        else:
            s = 0

        played += 1
        print()
    end(played, correct)

def rus(e, r):
    guess = "a"
    status = ["Incorrect", "Correct!"]
    played = 0
    correct = 0
    s = 0
    while guess != '0':
        screen_clear()
        print("Type '0' to exit game.")
        
        if played == 0:
            print("Давай начнем!")
        else:
            print("\nPrevious Round --", status[s])
            print("----------------")
            print("Prompt:", r[n])
            print("Guess:", guess)
            print("English:", e[n])
            print()
            
        seed()
        n = randrange(0, 66)
        print("Russian Prompt:", r[n])
        guess = str(input("Russian Letter: "))
        if r[n] == guess:
            s = 1
            correct += 1
        else:
            s = 0

        played += 1
        print()
    end(played, correct)

def screen_clear():
   #mac and linux
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      #windows
      _ = os.system('cls')


def main():
    russian = ["ё", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ",
               "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э",
               "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", ".",
               "Ё", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ",
               "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э",
               "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю", ","]
    
    english = ["`", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
               "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'",
               "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
               "~", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}",
               "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", '"',
               "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?"]
    
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

