import os
from os import path, stat
import json


def convert_player_in_dict(player) -> dict:
    player_info = dict()
    player_info["id"] = player.chess_id
    player_info["Name"] = player.family_name
    player_info["FirstName"] = player.firstname
    player_info["age"] = player.age
    player_info["totalPoint"] = player.total_point
    return player_info


def write_json(file, players_list) -> None:
    file.write(json.dumps(players_list, indent=4, ensure_ascii=False))


# je crois que cette export doit être global ?
def extract_global_player_list(players_list):
    folder_path = "outputs/global_players_list/"
    if not path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = f"{folder_path}global_players_list.json"

    # si le fichier existe, lis les infos dedans et compare avec la liste en entrée et si le joueur n'existe pas, ajoute le.
    if path.exists(file_path) and stat(file_path).st_size != 0:
        new_player = []
        with open(file_path, 'r') as f:
            json_data = json.load(f)

        for tournament_player in players_list:
            check = False
            for p_id in json_data:
                if p_id['id'] == tournament_player.chess_id:
                    check = True
            if not check:
                new_player_data = convert_player_in_dict(tournament_player)
                json_data.append(new_player_data)
        with open(file_path, "w") as f:
            write_json(f, json_data)

    else:
        data = []
        for player in players_list:
            data.append(convert_player_in_dict(player))

        with open(file_path, "w") as f:
            write_json(f, data)

