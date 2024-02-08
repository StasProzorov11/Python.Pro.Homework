TEAM_TYPE = dict[int, dict]

_TEAM: TEAM_TYPE = {
    1: {"name": "John", "age": 20},
    3: {"name": "Mark", "age": 33},
    12: {"name": "Cavin", "age": 31},
}


def get_team() -> TEAM_TYPE:
    return _TEAM


def get(id_) -> dict | None:
    try:
        player = _TEAM[id_]
    except KeyError:
        return None
    else:
        return player


def save(id_: int, instance: dict, debug: bool = False) -> bool:
    try:
        print(_TEAM[id_])
        if debug is True:
            print(f"Instance with id: {id_} already exist")
        return False
    except KeyError:
        _TEAM[id_] = instance
        return True


def update(id_: int, instance: dict, debug: bool = False):
    _TEAM[id_] = instance


def delete(id_: int, debug: bool = False) -> bool:
    try:
        del _TEAM[id_]
    except KeyError:
        if debug is True:
            print(f"There is not instance with id: {id_}")
        return False
    else:
        return True


def repr_players():
    team: dict[int, dict] = get_team()
    for number, player in team.items():
        print(f"\t[Player {number}]: {player['name']},{player['age']}")


def player_add(name: str, age: int, number: int) -> dict | None:
    player: dict = {"name": name, "age": age}
    saved: bool = save(id_=number, instance=player)

    if not saved:
        raise Exception(f"Player with number: {number} already exist")
    else:
        return player


def player_update(name: str, age: int, number: int) -> dict | None:
    player: dict | None = get(id_=number)
    if player is not None:
        player["name"] = name
        player["age"] = age
        update(id_=number, instance=player)
        return player
    else:
        print(f"Player with number {number} is not exist")
        return None


def player_delete(number: int) -> bool:
    team: dict[int, dict] = get_team()
    if not team.get(number):
        return False
    else:
        delete(id_=number)
        return True


def commands_dispatcher(operation: str):
    operations = ("add", "del", "repr", "update", "exit")

    if operation not in operations:
        raise Exception(f"Operation: '{operation}' is not available\n")

    if operation == "exit":
        raise SystemExit("Bye! Exiting the application")

    elif operation == "repr":
        repr_players()
    elif operation == "add":
        user_data = input("Enter new player information[name,age,number]: ")

        user_items: list[str] = user_data.split(",")
        name, age, number = user_items
        try:
            player_add(name=name, age=int(age), number=int(number))
        except ValueError:
            raise Exception("Age and number of player must be integers\n\n")

    elif operation == "del":
        user_data = input("Enter player's number[int]: ")
        try:
            _user_data = int(user_data)
        except ValueError:
            raise Exception("Age and number of player must be integers\n\n")
        else:
            player_delete(number=_user_data)

    elif operation == "update":
        user_data = input("Enter a new player's information[name,age,number]: ")
        user_items: list[str] = user_data.split(",")
        name, age, number = user_items
        try:
            new_player = player_update(name=name, age=int(age), number=int(number))
        except ValueError:
            raise Exception("Age and number of player must be integers\n\n")
        else:
            if new_player is None:
                print(f"Player [{number}] is not updated")
            else:
                print(
                    f"Player [{number}] is updated. "
                    f"Name: [{new_player['name']}], "
                    f"age: [{new_player['age']}]"
                )


def main():
    while True:
        operation = input("Please enter the operation: ")
        try:
            commands_dispatcher(operation=operation)
        except SystemExit as error:
            raise error
        except Exception as error:
            print(error)
            continue


if __name__ == "__main__":
    main()
