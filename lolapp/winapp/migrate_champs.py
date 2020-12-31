import csv
from winapp.models import champs

with open(r'C:\Users\Justin V\Desktop\lolchamps.csv') as csvfile:
    champreader = csv.reader(csvfile)
    for row in champreader:
        temp = row
        champ = champs(champ_name=temp[0],champ_splitpush=temp[1],champ_pick=temp[2],champ_siege=temp[3],champ_control=temp[4],champ_teamfight=temp[5])

        try:
            print(champ.save())
        except:
            print('there was a problem with champ %s' % temp[0])