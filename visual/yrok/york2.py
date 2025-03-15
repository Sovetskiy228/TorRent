animals = []
names = []
feed = []

for i in range(10):
    animal = input("Введите породу животного:")
    name = input("Введите имя:")
    food = int(input("Введите приёмы пищи:"))

action = input()
while True:
    if action == "1":
        name = input("Имя:")
        index = 0
        for i in range(10):
            if names[i] == name:
                index = i
                break
            if feed[index] <3:
                feed[index] +=1
            else:
                print("Животное уже сыто")
    elif action == "2":
        