# Oath Save File Parser
A quick and dirty tool for porting a TTS chronicle over to a physical game by reading a Tabletop Simulator save file and printing out a suit-ordered list of which denizen cards are in the dispossessed, archive, world deck, and on the board. 

# Usage
`python OathSaveFileParser.py` will open a file dialog. Use this dialog to open a TTS save file (which are usually called `TS_Save_X.json`). You may need to open some up beforehand and check which save file is the one you want. The very start of the save file will tell you the name, game, and date saved.

A list of suit-ordered cards in each location will be printed in the console. Note that relics, edifices, sites, and which site cards on the board are at are NOT listed. You can work these things out from the TTS game or oath.vision.

# Credits
- Leder Games for making the game in the first place,
- AgentElrond for having very readable JSON in his TTS mod
- Seiyria for making cool tools and for the cardsuits.json file