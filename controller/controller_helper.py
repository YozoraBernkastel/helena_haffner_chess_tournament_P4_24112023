from settings.settings import EXPORT_FOLDER
from os import path
import json


def already_in_tournament(chess_id, tournament_name):
    tournament_players_path = f"{EXPORT_FOLDER}tournaments/{tournament_name}/players_list.json"

    if path.exists(tournament_players_path):
        with open(tournament_players_path, "r") as f:
            data = json.load(f)

            return any(player["id"] == chess_id for player in data)


def is_already_known_id(chess_id):
    global_players_path = f"{EXPORT_FOLDER}global_players_list/players_list.json"

    if path.exists(global_players_path):
        with open(global_players_path, "r") as f:
            data = json.load(f)

            for player in data:
                if player["id"] == chess_id:
                    return True, player

    return False, None


