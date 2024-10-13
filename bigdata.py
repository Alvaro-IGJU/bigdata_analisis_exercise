import pandas as pd

#Cargar todos los archivos
common_player_info = pd.read_csv('./csv/csv/common_player_info.csv')
draft_combine_stats = pd.read_csv('./csv/csv/draft_combine_stats.csv')
draft_history = pd.read_csv('./csv/csv/draft_history.csv')
game_info = pd.read_csv('./csv/csv/game_info.csv')
game_summary = pd.read_csv('./csv/csv/game_summary.csv')
game = pd.read_csv('./csv/csv/game.csv')
inactive_players = pd.read_csv('./csv/csv/inactive_players.csv')
line_score = pd.read_csv('./csv/csv/line_score.csv')
officials = pd.read_csv('./csv/csv/officials.csv')
other_stats = pd.read_csv('./csv/csv/other_stats.csv')
player = pd.read_csv('./csv/csv/player.csv')
team_details = pd.read_csv('./csv/csv/team_details.csv')
team_history = pd.read_csv('./csv/csv/team_history.csv')
team_info_common = pd.read_csv('./csv/csv/team_info_common.csv')
team = pd.read_csv('./csv/csv/team.csv')

#Crear un diccionario con todos los DataFrames para facilitar la iteración
dataframes = {
    'common_player_info': common_player_info,
    'draft_combine_stats': draft_combine_stats,
    'draft_history': draft_history,
    'game_info': game_info,
    'game_summary': game_summary,
    'game': game,
    'inactive_players': inactive_players,
    'line_score': line_score,
    'officials': officials,
    'other_stats': other_stats,
    'player': player,
    'team_details': team_details,
    'team_history': team_history,
    'team_info_common': team_info_common,
    'team': team
}

#Mostrar el análisis de cada DataFrame
for name, df in dataframes.items():
    print(f"\n=== {name} ===")
    print("Head (primeras 5 filas):")
    print(df.head())
    print("\nDescripción estadística:")
    print(df.describe())