from winapp.models import champs
import cass_api
#this is going to take in the champ variable from the summoner_name_form (which is a list of all the champion names in the current match) 
#it will divide them into the two teams, it seems that the API gives us the teams as 0-4 are the first team and 5-9 are the second team. 
#once the teams are divided, make a call to the database for each of the champions and get their associated numbers and start adding the numbers to the
#individual team arrays
#once the team arrays are filled out then see which number is the largest. Correlate each coloum to it's appropriate tactic and print out the tactic.

def calculate_red_team(champ_list):
    #first declare a few variables
    red_team_numbers = [0,0,0,0,0]
    red_team_names = []
    #next divide the teams up
    red_team_names = champ_list[5:]
    #figure out the red teams numbers
    for names in red_team_names:
        current_champ = champs.object.get(champ_name=str(name))
        red_team_numbers[0] = current_champ.champ_splitpush
        red_team_numbers[1] = current_champ.champ_pick
        red_team_numbers[2] = current_champ.champ_siege
        red_team_numbers[3] = current_champ.champ_control
        red_team_numbers[4] = current_champ.champ_teamfight
    #find the index of the largest number in the list, this correlates directly to the most winning tactic.    
    index_of_max = red_team_numbers.index(max(red_team_numbers))





