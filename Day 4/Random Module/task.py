import random
import my_module

rand_num = random.randint(1,10)
print(rand_num)
print(my_module.my_favorite_number)

rand_num_0_to_1 = random.random() * 10
print(rand_num_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

# Create a coin flip program that randomly prints heads or tails
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")