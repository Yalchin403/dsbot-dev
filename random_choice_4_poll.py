RANDOM_CHOICES="""✅
🧚
🚶
🚴
🤸
🌸
🌺
🌻
🌼
🌱
🌲
🌳
🌴
🌍
🌎
🌏
🗺️
❎
👇
👍
👎
✊
👊
🤛
🤜
👏
🙌
👐
🤲
🤝
🛴"""
RANDOM_CHOICES = RANDOM_CHOICES.split("\n")
import random
def random_choice(n):
    choices = list()
    for i in range(n):
        choice = random.choice(RANDOM_CHOICES)
        while(True):

            if choice in choices:
                choice = random.choice(RANDOM_CHOICES)
            else:
                choices.append(choice)
                break
    return choices