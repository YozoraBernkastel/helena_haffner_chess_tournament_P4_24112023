import os
from os import path, stat
import json
from models.tournament import Tournament
from models.round import Round
from settings.settings import EXPORT_FOLDER
from export.export_helper import write_json
from export.export_player_data import export_player_list


def convert_tournament_in_dict(tournament):
    tournament_info = dict()
    tournament_info["id"] = str(tournament.id)
    tournament_info["name"] = tournament.name
    tournament_info["location"] = tournament.location
    tournament_info["Total Number of Rounds"] = tournament.number_of_rounds
    tournament_info["starting time"] = tournament.starting_time
    tournament_info["ending time"] = tournament.ending_time
    tournament_info["list of rounds"] = {}
    tournament_info["description"] = tournament.description
    return tournament_info


def export_tournament_data(tournament: Tournament):
    folder_path = f"{EXPORT_FOLDER}tournaments/{tournament.name}/"
    if not path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = f"{folder_path}{tournament.name}_{tournament.id}.json"
    json_data = []

    if path.exists(file_path) and stat(file_path) != 0:
        print("existe déjà")

    else:
        for player in tournament.players_list:
            export_player_list(player, folder_path)
        json_data.append(convert_tournament_in_dict(tournament))

    with open(file_path, "w") as f:
        write_json(f, json_data)




