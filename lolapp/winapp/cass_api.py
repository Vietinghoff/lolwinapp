import cassiopeia as cass

#get's the match of the selected summoner
def get_match(summoner_name, summoner_region):
    summoner = cass.get_summoner(name=summoner_name, region=summoner_region)
    return summoner

#gets all the champions that are being played in a specific match and returns a list of them.
def get_champions(summoner):
    id_num = 0
    champion = []
    summoner_match = summoner.current_match
    while id_num < 10:
        temp = summoner_match.participants[id_num].champion
        champion.append(temp)
        id_num = id_num + 1
    return champion
