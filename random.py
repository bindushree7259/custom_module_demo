import random

print("Random integer:", random.randint(1, 10))
print("Random decimal:", random.random())

colors = ["Red", "Blue", "Green"]
print("Random color:", random.choice(colors))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

print("Random decimal 1 to 10:", random.uniform(1, 10))