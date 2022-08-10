from ast import main
import json
import requests



def display_all_leagues():
    url = 'https://api-football-standings.azharimm.site/leagues'
    response = requests.get(url)
    data = json.loads(response.text)

    available_leagues = []
    for item in range(len(data['data'])):
        league_id = data['data'][item]['id']
        league_name = data['data'][item]['name']
        available_leagues.append((league_id, league_name))

    for league in available_leagues:
        print(f'ID: {league[0]}, name: {league[1]}')



def league_data(id,season):
    url = f'https://api-football-standings.azharimm.site/leagues/{id}/standings?season={season}&sort=asc'
    response = requests.get(url)
    data = json.loads(response.text)

    if data['status'] is True:
        num_of_teams = len(data['data']['standings'])

        league_table = []
        league_name = data['data']['name']
        league_season = data['data']['seasonDisplay']
        league_table.append((league_name, league_season))
        
        
        for team in range(num_of_teams):
            rank = data['data']['standings'][team]['stats'][8]['value']    
            team_name = data['data']['standings'][team]['team']['name']
            team_wins = data['data']['standings'][team]['stats'][0]['value']
            team_draws = data['data']['standings'][team]['stats'][1]['value']
            team_loses = data['data']['standings'][team]['stats'][2]['value']
            games_played = data['data']['standings'][team]['stats'][3]['value']
            goals_for = data['data']['standings'][team]['stats'][4]['value']
            goals_against = data['data']['standings'][team]['stats'][5]['value']
            goals_diff = data['data']['standings'][team]['stats'][9]['value']
            points = data['data']['standings'][team]['stats'][6]['value']
            goals_diff = data['data']['standings'][team]['stats'][9]['value']

            league_table.append((rank, team_name, games_played, team_wins, team_draws, team_loses, goals_for,goals_against, goals_diff, points))

        return league_table

            
    else:
        return False

def display_user_data(data):
    
    print(f'League: {data[0][0]}, Season: {data[0][1]}')
    print()
    print(f'P \t\tteam \t P \t W \t D \t L \t S \t C \t B \t Pts')
    data.remove((data[0]))
    for item in data:
        print(item[0],"\t", item[1],"\t", item[2],"\t", item[3],"\t", item[4],"\t", item[5],"\t", item[6],"\t", item[7],"\t", item[8],"\t", item[9])


def create_db_file(data):
    pass

def create_csv_file(data):
    pass

def create_json_file(data):
    file_name = input("Input file name: ")
    with open(f'{str(file_name)}.json', "w") as f:
        json_data = json.dump(data, f, indent=2)
        print(json_data)


if __name__ == "__main__":
    print("This app present league tables from few leagues in last years")
    print("Available leagues: ")
    display_all_leagues()
    while True:
        user_id = input("Enter league ID: ")
        user_season = input("Enter a season (year):")
        
        table = league_data(user_id, user_season)
        if table:
            display_user_data(table)
            file_eksport = input("Export data to CSV or DB file? (input: CSV/DB/JSON/EXIT): ")
            if file_eksport.upper == "CSV":
                create_csv_file(table)
            elif file_eksport == "DB":
                create_db_file(table)
            elif file_eksport == "JSON":
                create_json_file(table)
            elif file_eksport == "EXIT":
                pass
            else:
                print("Input error, try again")
            
            break
        else:
            print("Input error or API connection error, try again")
            continue
    

