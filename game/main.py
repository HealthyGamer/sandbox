from random import randint


def run_game():
    player1 = {"health": 50, "damage": 5}
    player2 = {"health": 50, "damage": 5}

    while True:
        # rolls a dice between 1 and player1's damage
        damage_dealt = randint(1, player1["damage"])
        player2["health"] -= damage_dealt
        print(
            f"Player 2 took {damage_dealt} damage: {player2['health']} health left"
        )
        if player2["health"] <= 0:
            print("Player 1 wins")
            break
        damage_dealt = randint(1, player2["damage"])
        player1["health"] -= damage_dealt
        print(
            f"Player 1 took {damage_dealt} damage: {player1['health']} health left"
        )
        if player1["health"] <= 0:
            print("Player 2 wins")
            break


if __name__ == "__main__":
    run_game()
