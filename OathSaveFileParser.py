import json
from os import path
from pathlib import Path
from suits import Suit
from visions import visions
import tkinter as tk
from tkinter import filedialog

tts_save_location = path.join(str(Path.home()), "Documents", "My Games", "Tabletop Simulator", "Saves")

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


def order_by_suit(card_list):
    suit_lists = [[], [], [], [], [], []]
    full_card_list = read_json_file("cardsuits.json")

    for card in card_list:
        if card not in visions:  # ignore visions - they have no suit
            suit_id = full_card_list[card]
            suit_lists[suit_id].append(card)

    return suit_lists


def print_suit_ordered_card_list(suit_ordered_card_list):
    i = 0
    for suit in suit_ordered_card_list:
        print(Suit(i).name)
        if not suit:
            print("\tNone")
        for card in suit:
            print(f"\t{card}")
        i += 1


def parse_oath_save_json(json_data):
    save_game_state = json.loads(json_data[game_state_key])
    full_card_list = read_json_file("cardsuits.json")

    dispossessed = save_game_state[dispossessed_cards_key]
    world_deck = save_game_state[world_deck_cards_key]
    cards_on_map = save_game_state[map_cards_key]

    # Remove sites, relics, and edifices - we only care about denizens
    denizen_cards_on_map = []
    for site in cards_on_map:
        for card, flipped in site:
            if card in full_card_list:
                denizen_cards_on_map.append(card)

    # The archive is everything else
    archive = []
    for card in full_card_list:
        if card not in dispossessed \
                and card not in world_deck \
                and card not in denizen_cards_on_map:
            archive.append(card)

    # Print out our card lists ordered by suit
    print(f"Cards on map ({len(denizen_cards_on_map)}):")
    print_suit_ordered_card_list(order_by_suit(denizen_cards_on_map))
    print()

    print(f"The Dispossessed ({save_game_state[dispossessed_cards_count_key]}):")
    print_suit_ordered_card_list(order_by_suit(dispossessed))
    print()

    print(f"World Deck ({save_game_state[world_deck_cards_count_key]} including 5 Visions):")
    print_suit_ordered_card_list(order_by_suit(world_deck))
    print()

    print(f"The Archive: {len(archive)}")
    print_suit_ordered_card_list(order_by_suit(archive))


if __name__ == '__main__':
    default_path = tts_save_location if path.isdir(tts_save_location) else "."

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir=default_path,
                                           title="Oath Save File",
                                           filetypes=[("json files","*.json")])

    if file_path:
        save_file_json = read_json_file(file_path)
        parse_oath_save_json(save_file_json)

