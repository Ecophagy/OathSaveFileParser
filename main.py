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
map_cards_key = "curMapNormalCards"


def read_json_file(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
    return json.loads(data)


def read_save_file(save_file_name):
    save_file = path.join(my_tts_save_location, save_file_name + ".json")
    return read_json_file(save_file)


def parse_oath_save_json(json_data):
    save_game_state = json.loads(json_data[game_state_key])
    full_card_list = read_json_file("cardsuits.json")

    dispossessed = save_game_state[dispossessed_cards_key]
    world_deck = save_game_state[world_deck_cards_key]
    map = save_game_state[map_cards_key]

    denizen_cards_on_map = []
    for site in map:
        for card, flipped in site:
            if card in full_card_list:
                denizen_cards_on_map.append(card)

    print(f"Cards on map ({len(denizen_cards_on_map)}):")
    for card in denizen_cards_on_map:
        print(card)
    print()

    print(f"Dispossessed cards ({save_game_state[dispossessed_cards_count_key]}):")
    for card in dispossessed:
        print(card)
    print()

    print(f"World Deck ({save_game_state[world_deck_cards_count_key]}):")
    for card in world_deck:
        print(card)
    print()

    # The archive is everything else
    archive = []
    for card in full_card_list:
        if card not in dispossessed \
                and card not in world_deck\
                and card not in denizen_cards_on_map:
            archive.append(card)
    print(f"The Archive: {len(archive)}")
    for card in archive:
        print(card)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    save_file_name = "TS_Save_6" # Have user enter this?
    json_data = read_save_file(save_file_name)
    parse_oath_save_json(json_data)

