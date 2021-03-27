from pathlib import Path
from os import path, listdir
import json

tts_save_location = path.join(str(Path.home()), "Documents", "My Games", "Tabletop Simulator", "Saves")
my_tts_save_location = path.join("D:\\", "Documents", "My Games", "Tabletop Simulator", "Saves") # TODO: Documents doesn't exist??
game_state_key = "LuaScriptState"
dispossessed_cards_key = "curDispossessedDeckCards"
dispossessed_cards_count_key = "curDispossessedDeckCardCount"
world_deck_cards_key = "curWorldDeckCards"
world_deck_cards_count_key = "curWorldDeckCardCount"


def read_save_file(save_file_name):
    save_file = path.join(my_tts_save_location, save_file_name + ".json")
    with open(save_file, 'r') as f:
        data = f.read()
        return json.loads(data)


def parse_oath_save_json(json_data):
    save_game_state = json.loads(json_data[game_state_key])

    print(f"Dispossessed cards ({save_game_state[dispossessed_cards_count_key]}):")
    for card in save_game_state[dispossessed_cards_key]:
        print(card)
    print()

    print(f"World Deck ({save_game_state[world_deck_cards_count_key]}):")
    for card in save_game_state[world_deck_cards_key]:
        print(card)
    print()

    print("The Archive: Everything else not on the board!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    save_file_name = "TS_Save_6" # Have user enter this?
    json_data = read_save_file(save_file_name)
    parse_oath_save_json(json_data)

