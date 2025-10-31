from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

# Solution: randint was only looking between 1 and 6. The dice images are an array
# it should start at 0 and end at 5.