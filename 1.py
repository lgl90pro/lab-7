import string

while True:
    while True:
        text = (input('Введіть текст, що складається із цифр і малих латинських літер (у кінці - крапка): '))
        b = set(string.ascii_lowercase)
        c = set(string.digits)
        vowel = set('aeiou')
        vowel_list = []
        consonant = set('bcdfghjklmnpqrstvwxyz')
        consonant_list = []

        for i in text:
            if((i in b) or (i in c) or (i == ' ') or (i == '.')):
                pass
            else:
                print('Текст може містити лише малі латинські літери та цифри.')
                print()
                break

        if(text[-1] != '.'):
            print('У кінці тексту повинна бути крапка.')
            print()
            continue

        for i in text:
            if(i in vowel):
                vowel_list.append(i)
            elif(i in consonant):
                consonant_list.append(i)
            else:
                pass

        if(len(vowel_list) > len(consonant_list)):
            print('Голосних букв у тексті більше.')
        elif(len(consonant_list) > len(vowel_list)):
            print('Приголосних букв у тексті більше.')
        elif(len(consonant_list) == len(vowel_list)):
            print('Голосних та приголосних букв у тексті однаково.')

        print()
        print('Бажаєте повторити задачу?')
        while True:
            question = input('(Так/Ні): ')
            if (
                    question == 'Так' or question == 'так' or question == 'Yes' or question == 'yes' or question == 'y' or question == '+'):
                print()
                break
            elif (
                    question == 'Ні' or question == 'ні' or question == 'No' or question == 'no' or question == 'n' or question == '-'):
                exit(0)
            else:
                print()
                print('Бажаєте повторити задачу?')

