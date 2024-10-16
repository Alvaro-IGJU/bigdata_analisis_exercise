import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar todos los archivos CSV
try:
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
except FileNotFoundError as e:
    print(f"Error al cargar los archivos: {e}")

# Agrupación de datos
pts_por_ciudad_home = line_score.groupby('team_nickname_home')['pts_home'].sum()
pts_por_ciudad_away = line_score.groupby('team_nickname_away')['pts_away'].sum()

# Sumar los puntos de casa y de visita por equipo
pts_totales_por_ciudad = pts_por_ciudad_home.add(pts_por_ciudad_away, fill_value=0)
pts_totales_por_ciudad = pts_totales_por_ciudad.sort_values(ascending=False)

# Mostrar los equipos que estén por encima de la media de puntos totales
pts_totales_por_ciudad = pts_totales_por_ciudad[pts_totales_por_ciudad > pts_totales_por_ciudad.mean()]

# Crear el DataFrame para la capacidad de los estadios
arena_capacity = pd.DataFrame({
    'arena': team_details['arena'],
    'arena_capacity': team_details['arenacapacity']
})
arena_capacity = arena_capacity.sort_values(by='arena_capacity', ascending=False)
arena_capacity.dropna(inplace=True)

# Equipos por estado
equipos_por_estado = team.groupby('state').size()
equipos_por_estado_df = equipos_por_estado.reset_index(name='cantidad').sort_values(by='cantidad', ascending=False)

# Número de jugadores activos e inactivos
active_count = (player['is_active'] == 1).sum()
inactive_count = (player['is_active'] == 0).sum()

# Configurar el estilo de la gráfica
sns.set(style="whitegrid")

# Crear los subgráficos
fig, axs = plt.subplots(3, 2, figsize=(14, 18))  # 3 filas, 2 columnas

# Gráfico de la suma total de puntos por equipo
pts_totales_por_ciudad.plot(kind='bar', color='lightgreen', width=0.8, ax=axs[0, 0])
axs[0, 0].set_title('Suma total de puntos por equipo (Local y Visitante)', fontsize=16)
axs[0, 0].set_xlabel('Equipo', fontsize=14)
axs[0, 0].set_ylabel('Suma de puntos totales', fontsize=14)
axs[0, 0].tick_params(axis='x', rotation=90)

# Gráfico de la capacidad por estadio
axs[0, 1].barh(arena_capacity['arena'], arena_capacity['arena_capacity'], color='red', height=0.8)
axs[0, 1].set_title('Capacidad por estadio', fontsize=16)
axs[0, 1].set_xlabel('Capacidad', fontsize=14)
axs[0, 1].set_ylabel('Estadio', fontsize=14)

# Gráfico de la cantidad de equipos por estado
sns.barplot(x='state', y='cantidad', data=equipos_por_estado_df, color='skyblue', ax=axs[1, 0])
axs[1, 0].set_title('Cantidad de Equipos por Estado', fontsize=16)
axs[1, 0].set_xlabel('Estado', fontsize=14)
axs[1, 0].set_ylabel('Cantidad de Equipos', fontsize=14)
axs[1, 0].tick_params(axis='x', rotation=90)

# Gráfico de Active vs Inactive Players
labels = ['Active', 'Inactive']
sizes = [active_count, inactive_count]
colors = ['#8BCB8B', '#D75B5B']

axs[1, 1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
axs[1, 1].axis('equal')  # Para que el gráfico sea circular
axs[1, 1].set_title('Active vs Inactive Players', fontsize=16)

# Gráfico de cantidad de jugadores por equipo
jugadores_por_equipo = common_player_info.groupby('team_name').size()
jugadores_por_equipo_df = jugadores_por_equipo.reset_index(name='cantidad').sort_values(by='cantidad', ascending=False)

sns.barplot(x='team_name', y='cantidad', data=jugadores_por_equipo_df, color='orange', ax=axs[2, 0])
axs[2, 0].set_title('Cantidad de Jugadores por Equipo', fontsize=16)
axs[2, 0].set_xlabel('Equipo', fontsize=14)
axs[2, 0].set_ylabel('Cantidad de Jugadores', fontsize=14)
axs[2, 0].tick_params(axis='x', rotation=90)

# Ocultar el último subgráfico (axs[2, 1])
axs[2, 1].axis('off')

# Ajustar el espacio entre subgráficos
plt.subplots_adjust(hspace=0.8, wspace=0.4)  # Espaciado vertical y horizontal

# Mostrar los gráficos
plt.show()
