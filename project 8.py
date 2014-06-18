baseball_positions = ["Pitcher", "Outfielder", "First", "Second", "Third", "baseman", "Shortstop",
                      "Utility", "infielder", "Designated", "hitter", "Catcher"]

# This is a list of characters that the program should ignore
ignored_words = ["\xce\xb2", "\xe2\x80\x932004"]

player_dict = {}

original_file = open("project_8.dat", "r")

for line in original_file:
    name = ""
    position = ""
    info = line.split()
    for word in info:
        if not ((word in baseball_positions) \
                or (word in ignored_words) \
                or (word.startswith("(")) \
                or (word.endswith(")"))):
            if name != "":
                name = name + " " + word
            else:
                name += word
        elif word in baseball_positions:
            if position != "":
                position = position + " " + word
            else:
                position += word
    player_dict[name] = position


player_dict_to_list = sorted(player_dict.items())

for key, value in player_dict_to_list:
    print key + ": " + value