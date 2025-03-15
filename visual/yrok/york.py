films = []
for i in range(3):
    film = input("Введите название фильма:")
    films.append(film)
print(films)

delete = input("Введите название фильма, который хотите удалить")
if delete in films:
    films.remove(delete)
else:
    print("Фильм не найден")

print(films)