import random

players = ["Isaiah", "Max","Braylen",
          "Jefferey", "Xavier", "Avery",
          "Carl","Walter", "Darren",
          "Ej", "Nahum", "Joaquin", 
          "Marshawn", "Ja'Den", "Kenlon", 
          "Nishad", "Kauri", "Kriss", 
          "Joseph", "Semaj", "Tay",
          "Taqari", "Jamauri", "Kamari"]


def PickTeams(players):
    random.shuffle(players)
    team1 = players[:len(players) // 2]
    teamCaptain1 = team1[random.randrange(0, 12)]

    print("TEAM 1:")
    print("Team Captain:" + teamCaptain1)
    for player in team1:
        print(player)
    
    team2 = players[len(players) // 2:]
    teamCaptain2 = team2[random.randrange(0,12)]
    print("\nTEAM 2:")
    print("Team 2 Captain:  " + teamCaptain2)

    for players in team2:
        print(players)
    
PickTeams(players)