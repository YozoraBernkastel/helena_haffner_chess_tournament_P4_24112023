import os
from os import path, stat
from settings.settings import EXPORT_FOLDER
from export.export_helper import write_json
from export.export_player_data import export_player_list
from export.export_player_data import update_global_players_list
import json


def export_tournament_data(tournament, last_save=False) -> None:
    folder_path = f"{EXPORT_FOLDER}tournaments/{tournament.export_name}/"
    if not path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = f"{folder_path}{tournament.export_name}.json"

    for player in tournament.players_list:
        export_player_list(player, folder_path)

    with open(file_path, "w") as f:
        write_json(f, tournament.convert_data())

    if last_save:
        [update_global_players_list(player) for player in tournament.players_list]


def add_tournament_to_unfinished_list(tournament) -> None:
    folder_path = f"{EXPORT_FOLDER}unfinished_tournaments_list/"
    if not path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = f"{EXPORT_FOLDER}unfinished_tournaments_list/unfinished_tournaments_list.json"
    data = list()
    tour = dict()

    if path.exists(file_path) and stat(file_path).st_size != 0:
        with open(file_path, "r") as f:
            data = json.load(f)

    tour["id"] = str(tournament.id)
    tour["name"] = tournament.name
    tour["starting_time"] = tournament.starting_time
    tour["folder"] = tournament.export_name
    data.append(tour)

    with open(file_path, "w") as f:
        write_json(f, data)


def remove_tournament_from_unfinished_list(tournament):
    folder_path = f"{EXPORT_FOLDER}unfinished_tournaments_list/"
    if not path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = f"{EXPORT_FOLDER}unfinished_tournaments_list/unfinished_tournaments_list.json"
    data = list()

    if path.exists(file_path) and stat(file_path).st_size != 0:
        with open(file_path, "r") as f:
            data = json.load(f)
            for tour in data:
                if tour["id"] == str(tournament.id):
                    data.remove(tour)
        with open(file_path, "w") as f:
            write_json(f, data)
