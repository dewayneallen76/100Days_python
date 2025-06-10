import random
# My solution
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends)
print(random.choice(friends))

# Another solution
random_index = random.randint(0, 4)
print(friends[random_index])