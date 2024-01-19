import os
from os import path, stat
import json
from settings.settings import EXPORT_FOLDER
from export.export_helper import write_json


def convert_player_in_dict(player) -> dict:
    player_info = dict()
    player_info["id"] = player.chess_id
    player_info["Name"] = player.family_name
    player_info["FirstName"] = player.firstname
    player_info["age"] = player.age
    player_info["totalPoint"] = player.total_point
    return player_info


def add_new_player(json_data, player):
    found = False
    for json_player in json_data:
        if json_player['id'] == player.chess_id:
            found = True
    if not found:
        new_player_data = convert_player_in_dict(player)
        json_data.append(new_player_data)

    return json_data


def export_player_list(player, folder_path=f"{EXPORT_FOLDER}global_players_list/"):
    if not path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = f"{folder_path}players_list.json"
    json_data = []

    if path.exists(file_path) and stat(file_path).st_size != 0:
        with open(file_path, 'r') as f:
            data = json.load(f)
        json_data = add_new_player(data, player)

    else:
        json_data.append(convert_player_in_dict(player))

    with open(file_path, "w") as f:
        write_json(f, json_data)



