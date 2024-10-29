from random import randint



hero = {
    'Name': '',
    'LvL': 1,
    'HP': 0,
    'MP': 0,
    'attack': 0,
    'armor': 0,
    'money': 100,
    'inventory':{
        'Ценный материал: ': 0,
        'Зелье здоровья (+50 hp): ': 1,
        'Зелье маны (+50 mp): ': 1,
        'Редкое украшение: ': 0,
    },
    'spells': {
        'Срочное лечение (50 mp)(+40 hp): ': 50,
        'Каменная пуля (30 mp)(40 dmg): ': 30,
    }
}

hero_defult_hp = 150
hero_defult_mp = 50
hero_defult_dmgA = 20
hero_defult_dmgB = 70
hero_defult_armor = 10

train_dmg = 0
train_armor = 0

hero_random_dmgA = (hero_defult_dmgA + (hero['LvL'] * 4) + (train_dmg * 3))
hero_random_dmgB = (hero_defult_dmgB + (hero['LvL'] * 4) + (train_dmg * 3))

hero['HP'] = hero_defult_hp + (hero['LvL'] * 5)
hero['MP'] = hero_defult_mp + (hero['LvL'] * 5)
hero['attack'] = randint( hero_random_dmgA , hero_random_dmgB )
hero['armor'] = (hero_defult_armor + (hero['LvL'] * 5) + (train_armor * 4))

hero_max_hp = hero_defult_hp + (hero['LvL'] * 5)
hero_max_mp = hero_defult_mp + (hero['LvL'] * 5)
hero_max_dmg = randint( hero_random_dmgA , hero_random_dmgB )

hero_max_armor = hero_defult_armor + (hero['LvL'] * 5)

spell_heal1 = hero['spells']['Срочное лечение (50 mp)(+40 hp): ']
spell_heal1_hp = 40
spell_attack1 = hero['spells']['Каменная пуля (30 mp)(40 dmg): ']
spell_attack1_dmg = 40

hero['HP'] -= 10
hero['MP'] -= 10

enemies = {
        'wolf':{
            'Name': 'Волк обычный',
            'HP': 50,
            'attack': randint(10, 30),
        },
        'druid':{
            'Name': 'Друид',
            'HP': 150,
            'attack': randint(20, 50),
            
        },
        'bandit':{
            'Name': 'Бандит',
            'HP': 120,
            'attack': randint(30, 70),
            'defult': 'Бандит: Ну дарова парнишь! Приготовся встретить смерть!',
            'win': 'Бандит: Ты одержал победу, забирай все что у меня есть, только оставь в живых!',
            'loss': 'Бандит: Ха-ха! Ты и в правду думал что у тебя есть шансы против меня?!',
        },
}

