import os
from os import path, stat
import json
from settings.settings import EXPORT_FOLDER
from export.export_helper import write_json


def update_player_list(json_data, player, total_points: bool) -> list:
    found = False
    for json_player in json_data:
        if json_player['id'] == player.chess_id:
            found = True
            json_player["total points"] = player.total_points if total_points else player.tournament_points

    if not found:
        new_player_data = player.format_data()
        json_data.append(new_player_data)

    return json_data


def export_player_list(player, folder_path=f"{EXPORT_FOLDER}global_players_list/") -> None:
    if not path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = f"{folder_path}players_list.json"
    json_data = []

    if path.exists(file_path) and stat(file_path).st_size != 0:
        with open(file_path, 'r') as f:
            data = json.load(f)
        global_folder: bool = folder_path == f"{EXPORT_FOLDER}global_players_list/"
        json_data = update_player_list(data, player, global_folder)

    else:
        json_data.append(player.format_data())

    with open(file_path, "w") as f:
        write_json(f, json_data)


def update_global_players_list(player) -> None:
    file_path = f"{EXPORT_FOLDER}global_players_list/players_list.json"
    if path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)

        for p in data:
            if player.chess_id == p["id"]:
                p["total points"] += player.tournament_points
                break

        with open(file_path, "w") as f:
            write_json(f, data)
