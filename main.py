games = { "A":"Adventure",
          "B":"Building",
          "C":"Survival",
          "D":"Multiplayer" }
        
print("This program picks out a video game you might like from some categories.")
print("Choose a category:")
for game in games:
  print(game, ":", games[game])
valid = False
while not valid:
  choice = input("Type a letter for your selection: ")
  if choice.upper() not in games:
    continue
  valid = True
choice = choice.upper()
print("You chose:", games[choice])

adventure = { "A":"Evoland",
              "B":"Legend of Zelda",
              "C":"Skyrim",
              "D":"Celeste"}

building = {"A":"Minecraft",
            "B":"Cities Skylines",
            "C":"The Sims",
            "D":"Kerbal Space Program"}
        
survival = {"A":"The Forest",
            "B":"Don't Starve",
            "C":"Dead by Daylight",
            "D":"The Long Dark"}

multiplayer = {"A":"Roblox",
               "B":"Overwatch",
               "C":"Maplestory",
               "D":"World of Warcraft"}

categories = {"A":adventure, "B":building, "C":survival, "D":multiplayer}

print("\nChoose a game:")
for game in categories[choice]:
  print(game, ":", categories[choice][game])

valid = False
while not valid:
  newchoice = input("Type a letter for your selection: ")
  if newchoice.upper() not in categories[choice]:
    continue
  valid = True
newchoice = newchoice.upper()
print("You chose:", categories[choice][newchoice])
