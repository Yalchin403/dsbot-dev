RANDOM_CHOICES="""β
π§
πΆ
π΄
π€Έ
πΈ
πΊ
π»
πΌ
π±
π²
π³
π΄
π
π
π
πΊοΈ
β
π
π
π
β
π
π€
π€
π
π
π
π€²
π€
π΄"""
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