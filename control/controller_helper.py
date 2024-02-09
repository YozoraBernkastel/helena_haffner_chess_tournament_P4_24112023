from settings.settings import EXPORT_FOLDER
import os
from os import path
import json
import pathlib


def is_user_quits(response: str) -> bool:
    return any(response == q for q in ("Q", "q"))


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


def json_file_exists(folder_path: str) -> bool:
    content = os.listdir(folder_path)
    json_files = any(pathlib.Path(file).suffix == ".json" for file in content)

    return len(content) > 0 and json_files


def items_in_folder(folder_path) -> list:
    """
    :param folder_path: path of the folder
    :return: a list of all directories in folder corresponding to path in param and containing at least one json file.
    """
    all_dir = [item for item in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, item))]

    return [item for item in all_dir if json_file_exists(f"{folder_path}{item}")]
