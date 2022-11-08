#!/usr/bin/env python

from game_data import games
from veto_data import vetos
import random
import sys

def check_vetos():
    # dirty but works
    all_games = set().union(*list(games.values()))
    # print(all_games)
    for player, p_vetos in vetos.items():
        for veto in p_vetos:
            if veto not in all_games:
                print(f'{player} tried to veto "{veto}" which is not a valid game.')

def get_random_game_no_veto(veto):
    for i in range(200):
        game = get_random_game()
        if game[0] not in veto:
            return game
    else:
        return ("You don't deserve to play.", "You are beating the odds or you vetoed almost everything")

def get_random_game():
    possible_games = random.choice(list(games.values()))
    return random.choice(list(possible_games.items()))

def get_game_for_players(players):
    actual_vetos = set()
    for player in players:
        actual_vetos = actual_vetos.union(vetos.get(player,set()))
    return get_random_game_no_veto(actual_vetos)


if __name__ == "__main__":
    check_vetos()
    if len(sys.argv) > 1:
        players = sys.argv[1:]
    else:
        players = []
    game = get_game_for_players(players)
    print(f"**Gamemode:**{game[0]}\n**Details:**\n{game[1].strip()}")

