import os
from os import path
from settings.settings import EXPORT_FOLDER
from export.export_helper import write_json
from export.export_player_data import export_player_list


def export_tournament_data(tournament) -> None:
    folder_path = f"{EXPORT_FOLDER}tournaments/{tournament.name}/"
    if not path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = f"{folder_path}{tournament.name}_{tournament.starting_time}.json"

    for player in tournament.players_list:
        export_player_list(player, folder_path)

    with open(file_path, "w") as f:
        write_json(f, tournament.convert_data())




