from pyswip import Prolog

prolog = Prolog()
prolog.consult("lab1.pl")

strategies = {
    "strategy": "Стратегия",
    "board": "Настольная",
    "word": "Словесная",
    "card": "Карточная"
}


def query(message: str):
    return list(map(lambda x: x["X"], prolog.query(message)))


games = query("game(X)")

game_name = input(f"Выберите игру {games}: ").strip()

players_count = tuple((str(query(f"players({game_name}, X)")[0]).replace('-(', '')
                       .replace(')', '').replace(' ', ''))
                      .split(","))

count = None
if game_name != "chess" and game_name != "checkers":
    count = input(f"Введите количество игроков в промежутке от {players_count[0]} до {players_count[1]}: ")
    while count < players_count[0] or count > players_count[1]:
        count = input(f"Введите количество игроков в промежутке от {players_count[0]} до {players_count[1]}: ")
    print(f"Количество игроков: {count}")
else:
    count = players_count
    print(f"Доступное количество игроков: {players_count[0]}")

game_type = query(f"type({game_name}, X)")[0]
print(f"Категория Вашей игры: {strategies[game_type]}")

rule = query(f"rules({game_name}, X)")[0]
print(f"Правила Вашей игры: {rule}")

characters = query(f"character({game_name}, X)")
character = input(f"Выберите одного персонажа из Вашей игры: {characters} ")
while character not in characters:
    character = input(f"Выберите одного персонажа из Вашей игры: {characters}: ")


def game_suitability(game):
    # Query Prolog to find who the game is suitable for
    for result in prolog.query(f"suitable_for_family('{game}')"):
        print(f"The game '{game}' is suitable for the whole family.")
    for result in prolog.query(f"suitable_for_adults('{game}')"):
        print(f"The game '{game}' is suitable for adults.")
    for result in prolog.query(f"suitable_for_children('{game}')"):
        print(f"The game '{game}' is suitable for kids.")
    for result in prolog.query(f"two_player_adult_game('{game}')"):
        print(f"The game '{game}' is suitable for two adult players.")
    for result in prolog.query(f"multiplayer_children_game('{game}')"):
        print(f"The game '{game}' is suitable for multiplayer children.")


game_suitability(game_name)
