from random import randint
import time
from data import *

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def defult():
    decision = input(f'\nВыберите действие\n1 - Начать поиск врагов\n2 - Осмотреться\n3 - Посмотреть статистику\n4 - Открыть инвентарь\n5 - Заклинания\n6 - Тренироваться\n7 - Магазин\n.. ')

    if decision == '1':
        time.sleep(1)
        print('Ведется поиск врагов в округе.')
        time.sleep(1)
        print('Ведется поиск врагов в округе..')
        time.sleep(1)
        print('Ведется поиск врагов в округе...\n')
        fight_prep()
    elif decision == '2':
        time.sleep(1)
        print('Вы осматриваете округу')
        time.sleep(1)
        print('Вы осматриваете округу..')
        time.sleep(1)
        print('Вы осматриваете округу...')
        rand2 = randint(1, 100)
        if rand2 >= 90:
            print('Вы нашли ценный материал! Возможно его получится продать за хорошую сумму!')
            hero['inventory']['Ценный материал: '] += 1
        else:
            print('Вы не смогли найти ничего интересного')
    elif decision == '3':

            global train_dmg
            global train_armor

            hero_random_dmgA = (hero_defult_dmgA + (hero['LvL'] * 4) + (train_dmg * 3))
            hero_random_dmgB = (hero_defult_dmgB + (hero['LvL'] * 4) + (train_dmg * 3))
            hero['armor'] = (hero_defult_armor + (hero['LvL'] * 5) + (train_armor * 4))

            print('\nВаше имя:',hero['Name'])
            print('Уровень hp:',hero['HP'])
            print('Уровень mp:',hero['MP'])
            print('Ваш уровень:', hero['LvL'])
            print('Ваш урон: от',hero_random_dmgA,'до', hero_random_dmgB)
            print('Ваша защита:', hero['armor'])
            print('Денег в вашем кошельке:', hero['money'])
    elif decision == '4':
        print('\nВаш инвентарь:\nЦенный материал:',hero['inventory']['Ценный материал: '])
        print('Зелье здоровья:',hero['inventory']['Зелье здоровья (+50 hp): '])
        print('Зелье маны:',hero['inventory']['Зелье маны (+50 mp): '])
        print('Редкое украшение:',hero['inventory']['Редкое украшение: '])

        decision_inv = input('\nЕсли требуется, выберите зелье \n1 - Зелье здоровья (+50 hp)\n2 - Зелье маны (+50 mp)\n3 <- Назад \n.. ')
        if decision_inv == '1' and hero['inventory']['Зелье здоровья (+50 hp): '] >= 1:
            hero['inventory']['Зелье здоровья (+50 hp): '] -= 1
            hero['HP'] += 50
            global hero_max_hp
            if hero['HP'] >= hero_max_hp:
                hero['HP'] -= hero['HP'] - hero_max_hp
                print('Вы выпили зелье кровавого цвета, \nвы начали чувствовать как ваше тело наполняется энергией\nвся боль как-будто пропала')
            else:
                hero['HP'] -= 0
                print('Вы выпили зелье кровавого цвета, \nвы начали чувствовать как ваше тело наполняется энергией\nвся боль как-будто пропала')
        elif decision_inv == '2' and hero['inventory']['Зелье маны (+50 mp): '] >= 1:
            hero['inventory']['Зелье маны (+50 mp): '] -= 1
            hero['MP'] += 50
            global hero_max_mp
            if hero['MP'] >= hero_max_mp:
                hero['MP'] -= hero['MP'] - hero_max_mp
                print('Вы выпили зелье бледно-синего цвета, \nвы начали чувствовать как ваше тело наполняется чем-то\nкакая-то сила наполнила ваше тело')
            else:
                hero['MP'] -= 0
                print('Вы выпили зелье бледно-синего цвета, \nвы начали чувствовать как ваше тело наполняется чем-то\nкакая-то сила наполнила ваше тело')
        elif hero['inventory']['Зелье здоровья (+50 hp): '] <= 0 or hero['inventory']['Зелье маны (+50 mp): '] <= 0:
            print('\nПохоже что у вас закончился этот тип зелья\n')
        elif decision_inv == '3':
            print('')
        else:
            print('Кажется такого варианта нет')
    elif decision == '5':
        decision_spells = input('\nВаши заклинания: \n1 - Срочное лечение (50 mp)(+40 hp) \n2 - Каменная пуля (30 mp)(40 dmg)\n3 <- Назад\n.. ')
        if decision_spells == 1:
            if hero['MP'] >= spell_heal1:
                print('\nКак по наитию вы начали говорить слова которые не знаете, \nвокруг вас начали появляться зеленые огни, \nболь уменьшилась\n')
                hero['MP'] -= spell_heal1
                hero['HP'] += spell_heal1_hp
                if hero['HP'] >= hero_max_hp:
                    hero['HP'] -= hero['HP'] - hero_max_hp
                else:
                    hero['HP'] -= 0
            else:
                print('У вас недостаточно mp чтобы кастовать это заклинание\n')
        elif decision_spells == '2':
            print('\nВы не находитесь в бою')
        elif decision_spells == '3':
            print('')
        else:
            print('Кажется такого варианта нет')
    elif decision == '6':
        training()
    elif decision == '7':
        shop()
    else:
        print('Кажется такого варианта нет')
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def shop():

    time.sleep(1)
    print('Перед вами появляется таинственная сфера')
    time.sleep(1)
    print('Сфера начинает вибрировать и превращается в телегу с различными товарами')
    time.sleep(1.5)
    print('Торговец изнутри спрашивает:\n- Чего желаешь путник?')
    time.sleep(1)
    while True:
        
        shop_decision = input('1 - Продать товары из инвентаря\n2 - Купить товары\n3 <- Назад\n.. ')
        time.sleep(1)
        if shop_decision == '1':
            while True:
                print('\nДенег в вашем кошельке:', hero['money'],'\n')
                sell_decision = input('\n1 - [80] Ценный материал\n2 - [50] Продать Зелье здоровья (+50 hp)\n3 - [50] Продать Зелье маны (+50 mp)\n4 - [250] Редкое украшение\n5 <- Назад\n.. ')

                if sell_decision == '1':
                    if hero['inventory']['Ценный материал: '] <= 0:
                        print('У вас недостаточно данного материала')
                    else:
                        hero['inventory']['Ценный материал: '] -= 1
                        hero['money'] += 80
                        time.sleep(1)
                        print('Торговец осмотрел Ценный материал, после чего вручил вам деньги')
                        time.sleep(1)
                        break
                elif sell_decision == '2':
                    if hero['inventory']['Зелье здоровья (+50 hp): '] <= 0:
                        print('У вас недостаточно данного зелья')
                    else:
                        hero['inventory']['Зелье здоровья (+50 hp): '] -= 1
                        hero['money'] += 50
                        time.sleep(1)
                        print('Торговец осмотрел Зелье, после чего вручил вам деньги')
                        time.sleep(1)
                        break
                elif sell_decision == '3':
                    if hero['inventory']['Зелье маны (+50 mp): '] <= 0:
                        print('У вас недостаточно данного зелья')
                    else:
                        hero['inventory']['Зелье маны (+50 mp): '] -= 1
                        hero['money'] += 50
                        time.sleep(1)
                        print('Торговец осмотрел Зелье, после чего вручил вам деньги')
                        time.sleep(1)
                        break
                elif sell_decision == '4':
                    if hero['inventory']['Редкое украшение: '] <= 0:
                        print('У вас нету Редкого Украшения')
                    else:
                        hero['inventory']['Редкое украшение: '] -= 1
                        hero['money'] += 250
                        time.sleep(1)
                        print('Торговец осмотрел Редкое Украшение, встрепенувшись, поторопился вручить вам деньги')
                        time.sleep(1)
                        break
                elif sell_decision == '5':
                    break
                else:
                    print('Кажется такого варианта нет')
        elif shop_decision == '2':
            while True:
                print('\nДенег в вашем кошельке:', hero['money'],'\n')
                buy_decision = input('\n1 - [100] Купить Зелье здоровья (+50 hp)\n2 - [100] Купить Зелье маны (+50 mp)\n3 <- Назад\n.. ')

                if buy_decision == '1':
                    if hero['money'] <= 99:
                        print('У вас недостаточно монет')
                    else:
                        hero['inventory']['Зелье здоровья (+50 hp): '] += 1
                        hero['money'] -= 100
                        time.sleep(1)
                        print('Торговец внимательно осмотрел деньги, после чего вручил вам ваше Зелье')
                        time.sleep(1)
                        break
                elif buy_decision == '2':
                    if hero['money'] <= 99:
                        print('У вас недостаточно монет')
                    else:
                        hero['inventory']['Зелье маны (+50 mp): '] += 1
                        hero['money'] -= 100
                        time.sleep(1)
                        print('Торговец внимательно осмотрел деньги, после чего вручил вам ваше Зелье')
                        time.sleep(1)
                        break
                elif buy_decision == '3':
                    break
                else:
                    print('Кажется такого варианта нет')
        elif shop_decision == '3':
            time.sleep(1)
            print('Как в мгновении ока телега исчезла, как будто ничего на этом месте и не было')
            time.sleep(1)
            break
        else:
            print('Кажется такого варианта нет')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def training():    

        train_decision = input('Выберите что вы будете тренировать:\n1 - Тренировать аттаку\n2 - Тренировать защиту\n3 <- Назад\n.. ')

        if train_decision == '1':
            train_proccess()
            global train_dmg
            train_dmg += 1
            print('После хорошей тренровки ты чувствуешь что стал сильнее (урон увеличен на 3)')
        elif train_decision == '2':
            train_proccess()
            global train_armor
            train_armor += 1
            print('После хорошей тренровки ты чувствуешь что стал более защищенным (защита увеличена на 4)')
        elif train_decision == '3':
            print('')
        else:
            print('Кажется такого варианта нет')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def train_proccess():
    for i in range(10):
                print(f"Загрузка... {i + 1}/10", end='\r')
                time.sleep(1)
    print("Загрузка завершена!     ")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def fight_prep():
    rand_enemy = randint(0, 100)
    if rand_enemy >= 0 and rand_enemy <=60:
        print(f'Цифра {rand_enemy}')
        wolf_enemy()
    elif rand_enemy >= 61 and rand_enemy <=90:
        print(f'Цифра {rand_enemy}')
        druid_enemy()
    else:
        print(f'Цифра {rand_enemy}')
        bandit_enemy()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def wolf_enemy():
    print('Вы встретили обычного волка!')
    print('Схватка начинается!\n')
    fight_procces_wolf()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def druid_enemy():
    print('Вы встретили Лесного Друида!')
    print('Схватка начинается!\n')
    fight_procces_druid()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def bandit_enemy():
    print('Вы встретили Бандита!')
    print(enemies['bandit']['defult'])
    print('Схватка начинается!\n')
    fight_procces_bandit()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

hero_attack = 0
hero_defence_count = 0
decision_battle = 0

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def hero_defence():
    global hero_defence_count
    hero_defence_count = input('Выберите что вы будете защищать\n1 - голова\n2 - грудь\n3 - пояс\n4 - ноги\n5 - Зелья\n.. ')
    if hero_defence_count == '1':
        print('Вы выбрали защищать голову')
    elif hero_defence_count == '2':
        print('Вы выбрали защищать грудь')
    elif hero_defence_count == '3':
        print('Вы выбрали защищать пояс')
    elif hero_defence_count == '4':
        print('Вы выбрали защищать ноги')
    elif hero_defence_count == '5':
        global decision_battle
        global hero_max_hp
        decision_battle = input('\nВыберите зелье \n1 - Зелье здоровья (+50 hp)\n2 - Зелье маны (+50 mp)\n3 <- Назад \n.. ')
        if decision_battle == '1' and hero['inventory']['Зелье здоровья (+50 hp): '] >= 1:
            hero['inventory']['Зелье здоровья (+50 hp): '] -= 1
            hero['HP'] += 50
            if hero['HP'] >= hero_max_hp:
                hero['HP'] -= hero['HP'] - hero_max_hp
                print('Вы выпили зелье кровавого цвета, \nвы начали чувствовать как ваше тело наполняется энергией\nвся боль как-будто пропала')
            else:
                hero['HP'] -= 0
                print('Вы выпили зелье кровавого цвета, \nвы начали чувствовать как ваше тело наполняется энергией\nвся боль как-будто пропала')
        elif decision_battle == '2' and hero['inventory']['Зелье маны (+50 mp): '] >= 1:
            hero['inventory']['Зелье маны (+50 mp): '] -= 1
            hero['MP'] += 50
            if hero['MP'] >= hero_max_mp:
                hero['MP'] -= hero['MP'] - hero_max_mp
                print('Вы выпили зелье бледно-синего цвета, \nвы начали чувствовать как ваше тело наполняется чем-то\nкакая-то сила наполнила ваше тело')
            else:
                hero['MP'] -= 0
                print('Вы выпили зелье бледно-синего цвета, \nвы начали чувствовать как ваше тело наполняется чем-то\nкакая-то сила наполнила ваше тело')
        elif hero['inventory']['Зелье здоровья (+50 hp): '] <= 0 or hero['inventory']['Зелье маны (+50 mp): '] <= 0:
            print('\nПохоже что у вас закончился этот тип зелья\n')
        elif decision_battle == '3':
            print('')
        else:
            print('Кажется такого варианта нет')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\

def hero_attack_wolf():
        global hero_attack
        hero_attack = input('Выберите куда вы будете аттаковать!\n1 - голова\n2 - грудь\n3 - пояс\n4 - ноги\n5 - Использовать заклинание "Срочное лечение (50 mp)(+40 hp)"\n6 - Использовать заклинание "Каменная пуля (30 mp)(40 attack)"\n.. ')
        if hero_attack == '1':
            print('Вы выбрали аттаковать голову противника')
        elif hero_attack == '2':
            print('Вы выбрали аттаковать грудь противника')
        elif hero_attack == '3':
            print('Вы выбрали аттаковать пояс противника')
        elif hero_attack == '4':
            print('Вы выбрали аттаковать ноги противника')
        elif hero_attack == '5':
            if hero['MP'] >= spell_heal1:
                print('\nКак по наитию вы начали говорить слова которые не знаете, \nвокруг вас начали появляться зеленые огни, \nболь уменьшилась\n')
                hero['MP'] -= spell_heal1
                hero['HP'] += spell_heal1_hp
                if hero['HP'] >= hero_max_hp:
                    hero['HP'] -= hero['HP'] - hero_max_hp
                else:
                    hero['HP'] -= 0
            else:
                print('У вас недостаточно mp чтобы кастовать это заклинание\n')
        elif hero_attack == '6':
            if hero['MP'] >= spell_attack1:
                print('\nКак по наитию вы начали говорить слова которые не знаете, \nоколо вашей руки начала появляться небольшая каменная глыба, отдаленно напоминающая пулю, \nпуля вылетает, и точно попадает в противника\n')
                hero['MP'] -= spell_attack1
                enemies['wolf']['HP'] -= spell_attack1_dmg
            else:
                print('У вас недостаточно mp чтобы кастовать это заклинание\n')
        return hero_attack

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def hero_attack_druid():
        global hero_attack
        hero_attack = input('Выберите куда вы будете аттаковать!\n1 - голова\n2 - грудь\n3 - пояс\n4 - ноги\n5 - Использовать заклинание "Срочное лечение (50 mp)"\n6 - Использовать заклинание "Каменная пуля (30 mp)"\n.. ')
        if hero_attack == '1':
            print('Вы выбрали аттаковать голову противника')
        elif hero_attack == '2':
            print('Вы выбрали аттаковать грудь противника')
        elif hero_attack == '3':
            print('Вы выбрали аттаковать пояс противника')
        elif hero_attack == '4':
            print('Вы выбрали аттаковать ноги противника')
        elif hero_attack == '5':
            if hero['MP'] >= spell_heal1:
                print('\nКак по наитию вы начали говорить слова которые не знаете, \nвокруг вас начали появляться зеленые огни, \nболь уменьшилась\n')
                hero['MP'] -= spell_heal1
                hero['HP'] += spell_heal1_hp
                if hero['HP'] >= hero_max_hp:
                    hero['HP'] -= hero['HP'] - hero_max_hp
                else:
                    hero['HP'] -= 0
            else:
                print('У вас недостаточно mp чтобы кастовать это заклинание\n')
        elif hero_attack == '6':
            if hero['MP'] >= spell_attack1:
                print('\nКак по наитию вы начали говорить слова которые не знаете, \nоколо вашей руки начала появляться небольшая каменная глыба, отдаленно напоминающая пулю, \nпуля вылетает, и точно попадает в противника\n')
                hero['MP'] -= spell_attack1
                enemies['druid']['HP'] -= spell_attack1_dmg
            else:
                print('У вас недостаточно mp чтобы кастовать это заклинание\n')
        return hero_attack

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def hero_attack_bandit():
        global hero_attack
        hero_attack = input('Выберите куда вы будете аттаковать!\n1 - голова\n2 - грудь\n3 - пояс\n4 - ноги\n5 - Использовать заклинание "Срочное лечение (50 mp)"\n6 - Использовать заклинание "Каменная пуля (30 mp)"\n.. ')
        if hero_attack == '1':
            print('Вы выбрали аттаковать голову противника')
        elif hero_attack == '2':
            print('Вы выбрали аттаковать грудь противника')
        elif hero_attack == '3':
            print('Вы выбрали аттаковать пояс противника')
        elif hero_attack == '4':
            print('Вы выбрали аттаковать ноги противника')
        elif hero_attack == '5':
            if hero['MP'] >= spell_heal1:
                print('\nКак по наитию вы начали говорить слова которые не знаете, \nвокруг вас начали появляться зеленые огни, \nболь уменьшилась\n')
                hero['MP'] -= spell_heal1
                hero['HP'] += spell_heal1_hp
                if hero['HP'] >= hero_max_hp:
                    hero['HP'] -= hero['HP'] - hero_max_hp
                else:
                    hero['HP'] -= 0
            else:
                print('У вас недостаточно mp чтобы кастовать это заклинание\n')
        elif hero_attack == '6':
            if hero['MP'] >= spell_attack1:
                print('\nКак по наитию вы начали говорить слова которые не знаете, \nоколо вашей руки начала появляться небольшая каменная глыба, отдаленно напоминающая пулю, \nпуля вылетает, и точно попадает в противника\n')
                hero['MP'] -= spell_attack1
                enemies['bandit']['HP'] -= spell_attack1_dmg
            else:
                print('У вас недостаточно mp чтобы кастовать это заклинание\n')
        return hero_attack

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def fight_procces_wolf():
    enemies['wolf']['HP'] = 50
    while hero['HP'] >= 1 and enemies['wolf']['HP'] >= 1:

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        global hero_attack
        hero_attack_wolf()
        if hero_attack == '5' or hero_attack == '6':
            while hero_attack == '5' or hero_attack == '6':
                hero_attack_wolf()
        else:
            print('')
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        global hero_defence_count
        hero_defence()
        if hero_defence_count == '5':
            while hero_defence_count == '5':
                hero_defence()
        else:
            print('')
        
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        enemy_attack = randint(1,4)
        if enemy_attack == 1:
            print('Противник выбрал аттаковать твою голову')
        elif enemy_attack == 2:
            print('Противник выбрал аттаковать твою грудь')
        elif enemy_attack == 3:
            print('Противник выбрал аттаковать твой пояс')
        elif enemy_attack == 4:
            print('Противник выбрал аттаковать твои ноги')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        enemy_defence = randint(1,4)
        if enemy_defence == 1:
            print('Противник выбрал защищать голову\n')
        elif enemy_defence == 2:
            print('Противник выбрал защищать грудь\n')
        elif enemy_defence == 3:
            print('Противник выбрал защищать пояс\n')
        elif enemy_defence == 4:
            print('Противник выбрал защищать ноги\n')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        if hero_attack == enemy_defence or hero_attack == '5' or hero_attack == '6':
            print('Противник смог успешно защититься')
            enemies['wolf']['HP'] -= 0
        else:
            print('Ты смог успешно аттаковать противника')
            enemies['wolf']['HP'] -= hero['attack']

    
        if hero_defence_count == enemy_attack:
            print('Ты смог успешно защититься')
            hero['HP'] -= 0
        else:
            print('Противник смог успешно аттаковать тебя')
            hero['HP'] -=  enemies['wolf']['attack'] - hero['armor']
        print('Ваше hp:',hero['HP'])
        print('hp противника:',enemies['wolf']['HP'])
    if hero['HP'] <= 0:
        print('Ты умер :(  Придется начать заново')
        return
    if enemies['wolf']['HP'] <= 0:
        print('Поздравляю! Ты победил обычного волка! Интересно какие плюшки ты смог получить?')
        hero['LvL'] += 3
        for i in range(randint(1, 2)):
            hero['inventory']['Ценный материал: '] += 1
        global wolf_hp
        enemies['wolf']['HP'] = 50
        wolf_hp = enemies['wolf']['HP']
        
    return hero['HP']

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def fight_procces_druid():
    enemies['druid']['HP'] = 150
    while hero['HP'] >= 1 and enemies['druid']['HP'] >= 1:

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        global hero_attack
        hero_attack_druid()
        if hero_attack == '5' or hero_attack == '6':
            while hero_attack == '5' or hero_attack == '6':
                hero_attack_druid()
        else:
            print('')
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        hero_defence()
        if hero_defence_count == '5':
            while hero_defence_count == '5':
                hero_defence()
        else:
            print('')
        
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        enemy_attack = randint(1,4)
        if enemy_attack == 1:
            print('Противник выбрал аттаковать твою голову')
        elif enemy_attack == 2:
            print('Противник выбрал аттаковать твою грудь')
        elif enemy_attack == 3:
            print('Противник выбрал аттаковать твой пояс')
        elif enemy_attack == 4:
            print('Противник выбрал аттаковать твои ноги')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        enemy_defence = randint(1,4)
        if enemy_defence == 1:
            print('Противник выбрал защищать голову\n')
        elif enemy_defence == 2:
            print('Противник выбрал защищать грудь\n')
        elif enemy_defence == 3:
            print('Противник выбрал защищать пояс\n')
        elif enemy_defence == 4:
            print('Противник выбрал защищать ноги\n')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        if hero_attack == enemy_defence or hero_attack == 5 or hero_attack == 6:
            print('Противник смог успешно защититься')
            enemies['druid']['HP'] -= 0
        else:
            print('Ты смог успешно аттаковать противника')
            enemies['druid']['HP'] -= hero['attack']

    
        if hero_defence_count == enemy_attack:
            print('Ты смог успешно защититься\n')
            hero['HP'] -= 0
        else:
            print('Противник смог успешно аттаковать тебя')
            hero['HP'] -= enemies['druid']['attack'] - hero['armor']
        print('Ваше hp:',hero['HP'])
        print('hp противника:',enemies['druid']['HP'])
    if hero['HP'] <= 0:
        print('Ты умер :(  Придется начать заново')
        return
    if enemies['druid']['HP'] <= 0:
        print('Поздравляю! Ты победил Лесного Друида! Интересно какие плюшки ты смог получить?')
        hero['LvL'] += 6
        for i in range(randint(2, 3)):
            hero['inventory']['Ценный материал: '] += 1
        for i in range(randint(1, 3)):
            hero['inventory']['Зелье здоровья (+50 hp): '] += 1
        for i in range(randint(1, 3)):
            hero['inventory']['Зелье маны (+50 mp): '] += 1
        for i in range(1):
            hero['inventory']['Редкое украшение: '] += 1

        global druid_hp
        enemies['druid']['HP'] = 150
        druid_hp = enemies['druid']['HP']

    return hero['HP']

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def fight_procces_bandit():
    enemies['bandit']['HP'] = 120
    while hero['HP'] >= 1 and enemies['bandit']['HP'] >= 1:

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        global hero_attack
        hero_attack_bandit()
        if hero_attack == '5' or hero_attack == '6':
            while hero_attack == '5' or hero_attack == '6':
                hero_attack_bandit()
        else:
            print('')
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        hero_defence()
        if hero_defence_count == '5':
            while hero_defence_count == '5':
                hero_defence()
        else:
            print('')
        
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        enemy_attack = randint(1,4)
        if enemy_attack == 1:
            print('Противник выбрал аттаковать твою голову')
        elif enemy_attack == 2:
            print('Противник выбрал аттаковать твою грудь')
        elif enemy_attack == 3:
            print('Противник выбрал аттаковать твой пояс')
        elif enemy_attack == 4:
            print('Противник выбрал аттаковать твои ноги')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        enemy_defence = randint(1,4)
        if enemy_defence == 1:
            print('Противник выбрал защищать голову\n')
        elif enemy_defence == 2:
            print('Противник выбрал защищать грудь\n')
        elif enemy_defence == 3:
            print('Противник выбрал защищать пояс\n')
        elif enemy_defence == 4:
            print('Противник выбрал защищать ноги\n')

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        if hero_attack == enemy_defence or hero_attack == 5 or hero_attack == 6:
            print('Противник смог успешно защититься')
            enemies['bandit']['HP'] -= 0
        else:
            print('Ты смог успешно аттаковать противника')
            enemies['bandit']['HP'] -= hero['attack']

    
        if hero_defence_count == enemy_attack:
            print('Ты смог успешно защититься')
            hero['HP'] -= 0
        else:
            print('Противник смог успешно аттаковать тебя')
            hero['HP'] -= enemies['bandit']['attack'] - hero['armor']
        print('Ваше hp:',hero['HP'])
        print('hp противника:',enemies['bandit']['HP'])
    if hero['HP'] <= 0:
        print(enemies['bandit']['loss'])
        print('Ты умер :(  Придется начать заново')
        return
    if enemies['bandit']['HP'] <= 0:
        print(enemies['bandit']['win'])
        print('Поздравляю! Ты победил Бандита! Интересно какие плюшки ты смог получить?')
        hero['LvL'] += 10
        for i in range(randint(2, 5)):
            hero['inventory']['Ценный материал: '] += 1
        for i in range(randint(1, 3)):
            hero['inventory']['Зелье здоровья (+50 hp): '] += 1
        for i in range(randint(1, 2)):
            hero['inventory']['Зелье маны (+50 mp): '] += 1
        for i in range(randint(1, 2)):
            hero['inventory']['Редкое украшение: '] += 1
        
        global bandit_hp
        enemies['bandit']['HP'] = 120
        bandit_hp = enemies['bandit']['HP']
    return hero['HP']

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\