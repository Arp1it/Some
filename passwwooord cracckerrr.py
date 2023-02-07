import random

user_input = input("enter password: \n")

a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
"s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "`", "~", "-", "+", "=", "_", ";",
":", ",", "/", "<", ">", ".", "?", "'", '"', "|"]

guess = ""

while (guess != user_input):
    guess = ""

    for i in range(len(user_input)):
        guess_letter = a[random.randint(0, 92)]
        guess = str(guess_letter) + str(guess)

        print(guess)