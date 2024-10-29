from random import randint
import time
from logic import *
from data import *


name = input('Назови себя путник: ')
hero['Name'] = name
current_enemy = 0

time.sleep(1)
print('Ты проснулся в неизвeстном для тебя месте, вокруг тебя пустой, гремящий лес, что же тебя ждет?')
time.sleep(3)
print('Осмотревшись ты понял что не помнишь ни то где ты, ни то как ты оказался тут')
time.sleep(2)
print('Ты чувствуешь себя слегка истощенным')
time.sleep(1.5)

while True:
    defult()
    if hero['HP'] <= 0:
        break
