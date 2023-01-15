# Приветствие и описание игры
print('Автор игры - Зеленков Анатолий')
print('Приветствуем вас в Волшебном доме!')
print('Здесь нужно рассказывать стихи новогодним персонажам, которые находятся в разных комнатах, и если им понравится, то вы получите от них подарок.')
# Введите своё имя
name = input('Как вас зовут? ')
# Начало игры и проверка, хочет ли пользователь её начать
begin = input('Отлично! Вы готовы начать игру? ')
if begin == 'Да' or begin == 'да' or begin == 'ДА':
    print('Отлично! Переместимся в дом!')
    while True:
        while True:
            # Выбор комнаты и персонажа, проверка на верный ввод
            room = input('Укажите номер комнаты, в которую вы хотите войти ')
            if room == '1':
                character = 'Дед Мороз'
            elif room == '2':
                character = 'Снегурочка'
            else:
                print('Неверный ввод')
                break
            print(character, ': Привет, ', name, '!', sep='')
            # Проверка на то, хочет ли игрок вводить стих 
            question = input('Хотите рассказать стих? ')
            if question == 'Да' or question == 'да' or question == 'ДА':
                count = 0
                # Рассказ стиха
                line = input()
                while line != '':
                    count += 1
                    line = input()
                # Проверка на то, понравился ли стих
                if character == 'Дед Мороз' and count <= 8 or character == 'Снегурочка' and count % 2 == 0:
                    print('Вы заслужили подарок. УРА!')
                else:
                    print('Ваше стихотворение не понравилось:(')
            else:
                print('Увы, вы пока не заслужили подарок.')
            break
        # Проверка на то, хочет ли пользователь продолжить игру
        question2 = input('Хотите продолжить? ')
        while question2 != 'Да' and question2 != 'да' and question2 != 'ДА' and question2 != 'Нет' and question2 != 'нет' and question != 'НЕТ':
            print('Попробуйте ввести еще раз')
            question2 = input('Хотите продолжить? ')
        if question2 == 'Да' or question2 == 'да' or question2 == 'ДА':
            continue
        elif question2 == 'Нет' or question2 == 'нет' or question2 == 'НЕТ':
            break
print('До свидания!')
