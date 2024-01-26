import os

from settings.settings import EXPORT_FOLDER
from os import path
import json


def already_in_tournament(chess_id, tournament) -> bool:
    tournament_players_path = f"{EXPORT_FOLDER}tournaments/{tournament.name}_{tournament.starting_time}/players_list.json"

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


def folder_exist(folder_path: str) -> bool:
    return path.exists(folder_path)


def items_in_folder(folder_path) -> list:
    """
    :param folder_path: path of the folder
    :return: a list of all directories in folder corresponding to path in param
    """
    return [item for item in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, item))]

