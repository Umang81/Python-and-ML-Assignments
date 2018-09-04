import yaml

def read_data():
    with open ('335982.yaml', 'r') as f:
        data = yaml.load(f)
        f.close()
    return data

data = read_data()

def import_teams(data):
    teams = data['info']['teams']
    return teams

teams = import_teams(data)
print(teams)

first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print ("The first batsman is: %s" %(first_batsman))

def deliveries_count(data, batsman):
    count = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == batsman:
                count += 1
    return count
RT = (deliveries_count(data, 'RT Ponting'))
print ("The number of deliveries faced by RT Ponting are: " + str(RT))

def runs(data, batsman):
    score = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == batsman:
                score += delivery_info['runs']['batsman']
    return score

BB = runs(data,'BB McCullum')
print ("The amount of runs scored by BB McCullum are: " + str(BB))

def bowled_out(data):
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'wicket' in delivery_info and delivery_info['wicket']['kind'] == 'bowled':
                bowled_players.append(delivery_info['wicket']['player_out'])

    return bowled_players
BP = bowled_out(data)
print ("The players that were out bowled in the second innings are: ")
for i in range(0, len(BP)):
    print ("." + BP[i]),

def extras_runs(data):
    innings1_extras = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            innings1_extras += delivery_info['runs']['extras']
    innings2_extras = 0
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            innings2_extras += delivery_info['runs']['extras']
    difference = abs(innings1_extras - innings2_extras)
    return difference

EXT = extras_runs(data)
print("The difference in extras between the two innings was: " + str(EXT) + " runs")
