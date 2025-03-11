import streamlit as st
from streamlit_sortables import sort_items
import pandas as pd

dict_teams = {'Fluminense': ['Fabio', 'Samuel Xavier', 'Thiago Silva', 'Ignacio', 'Fuentes', 'Otávio', 'Martinelli', 'Serna', 'Arias', 'Cano', 'Canobbio', 'Mano Menezes'],
                'Flamengo': ['Rossi', 'Wesley', 'Leo Ortiz', 'Leo Pereira', 'Alex Sandro', 'Pulgar', 'Gerson', 'Arrascaeta', 'Plata', 'Bruno Henrique', 'Michael', 'Filipe Luis'],
                'Vasco': ['Leo Jardim', 'Paulo Henrique', 'João Victor', 'Lucas Freitas', 'L. Piton', 'Hugo Moura', 'Jair', 'Coutinho', 'Rayan', 'Vegetti', 'Nuno Moreira', 'Carille'], # Lemos, Cocão/Paulinho, Tchê Tchê, Loide/Garré
                'Botafogo': ['John', 'Vitinho', 'Danilo Barbosa', 'A. Barboza', 'Alex Telles', 'Gregore', 'Marlon Freitas', 'Newton', 'Savarino', 'Igor Jesus', 'Matheus Martins', 'C. Caçapa'], # Santiago Rodriguez
                'Santos': ['João Paulo', 'JP Chermont', 'Gil', 'Zé Ivaldo', 'G. Escobar', 'João Schmidt', 'Thaciano', 'Neymar', 'Soteldo', 'Tiquinho', 'Guilherme', 'Pedro Caixinha'], # Leo Godoy, Barreal, Luan Peres, Veron, G.Bontempo
                'Palmeiras': ['Weverton', 'Marcos Rocha', 'Gustavo Gomez', 'Murilo', 'Vanderlan', 'E. Martínez', 'Richard Ríos', 'R. Veiga', 'Estêvão', 'V. Roque', 'Facundo Torres', 'Abel Ferreira'],
                'Corinthians': ['Hugo S.', 'Matheuzinho F.', 'Félix Torres', 'Gustavo Henrique', 'M. Bidu', 'J. Martínez', 'Breno Bidon', 'Garro', 'Carrillo', 'Yuri Alberto', 'Depay', 'Ramon Díaz'], # AndréRamalho/Tchoca/Cacá, Anglieri
                'São Paulo': ['Rafael', 'Cedric', 'Arboleda', 'Alan J. Franco', 'Enzo Díaz', 'Alisson', 'Marcos Antônio', 'Luciano', 'Lucas Moura', 'Calleri', 'Oscar', 'Zubeldia'],
                'Grêmio': ['Volpi', 'João Pedro', 'Jemerson', 'Wagner Leonardo', 'Lucas Esteves', 'Cuéllar', 'Villasanti', 'Cristaldo', 'C. Olivera', 'Braithwaite', 'Monsalve', 'G. Quinteros'],
                'Inter': ['Rochet', 'B. Aguirre', 'Vitão', 'Victor Gabriel', 'Bernabei', 'Fernando', 'Bruno Henrique C.', 'Alan Patrick', 'Wanderson', 'Borré', 'Wesley R.', 'Roger Machado'], # Thiago Maia, Bruno Tabata, Vitinho, E. Valencia
                'Cruzeiro': ['Cássio', 'William', 'Fabricio Bruno', 'Jonathan Jesus', 'Kaiki', 'Lucas Romero', 'Eduardo', 'Matheus Henrique', 'Kaio Jorge', 'Gabigol', 'Dudu', 'Leonardo Jardim'],
                'Atlético-MG': ['Everson', 'Natanael', 'Lyanco', 'Junior Alonso', 'Arana', 'Alan Franco', 'G. Menino', 'G. Scarpa', 'Rony', 'Hulk', 'Cuello', 'Cuca'],
                'Bahia': ['Marcos Felipe', 'Gilberto', 'Gabriel Xavier', 'Kanu', 'S. Mingo', 'Caio Alexandre', 'Jean Lucas', 'Éverton Ribeiro', 'Ademir', 'L. Rodríguez', 'Erick Pulga', 'Rogério Ceni'],
                'Vitória': ['Lucas Arcanjo', 'R. Cáceres', 'Neris', 'L. Halter', 'Jamerson', 'Willian Oliveira', 'Baralhas', 'Matheuzinho', 'W. Rato', 'Carlinhos', 'Lucas Braga', 'Carpini'],
                'Fortaleza': ['João Ricardo', 'Mancuso', 'David Luiz', 'Kuscevic', 'Bruno Pacheco', 'Zé Welison', 'G. Fernández', 'Pochettino', 'Marinho', 'Lucero', 'Moisés', 'Vojvoda'],
                'Ceará': ['Bruno Ferreira', 'Dieguinho', 'Marllon', 'Ramon', 'M. Bahia', 'Richardson', 'F. Sobral', 'Lucas Mugni', 'Pedro Henrique K.', 'Aylon', 'Fernandinho', 'Léo Condé'],
                'Juventude': ['Gustavo', 'Ewerton', 'Abner', 'Adriano Martins', 'M. Paulo', 'Giraldo', 'Jádson', 'Jean Carlos', 'Batalla', 'Erick Farias', 'Ênio', 'Fábio Matias'],
                'Bragantino': ['Cleiton', 'Hurtado', 'Eduardo S.', 'Pedro Henrique', 'Juninho Capixaba', 'Gabriel', 'Matheus Fernandes', 'Lucas Evangelista', 'Helinho', 'Pitta', 'Vinicinho', 'Fernando Seabra'],
                'Sport': ['Caique França', 'Di Plácido', 'Antônio Carlos', 'João Silva', 'Igor Cariús', 'Sergio Oliveira', 'F. Domínguez', 'Atencio', 'C. Barletta', 'Pablo', 'Romarinho', 'Pepa'],
                'Mirassol': ['Muralha', 'Lucas Ramon', 'J. Victor', 'A. Empereur', 'Daniel Borges', 'Danielzinho', 'José Aldo', 'Gabriel Jamal', 'Negueba', 'Iury Castilho', 'Chico Kim', 'Ivan Baitello'],
}
# lesionados: Pedro, Pablo Maia, Ganso, Adson, David

all_players = [el for v in dict_teams.values() for el in v]
repeated = set([el for el in all_players if all_players.count(el) > 1])
assert len(repeated) == 0, f"Repeated players: {repeated}"

players = [{'header': 'Goleiros', 'items': [squad[0] for squad in dict_teams.values()]}, {'header': 'Laterais Direitos', 'items': [squad[1] for squad in dict_teams.values()]},
         {'header': 'Zagueiros Direitos', 'items': [squad[2] for squad in dict_teams.values()]}, {'header': 'Zagueiros Esquerdos', 'items': [squad[3] for squad in dict_teams.values()]},
         {'header': 'Laterais Esquerdos', 'items': [squad[4] for squad in dict_teams.values()]}, {'header': '1º volante', 'items': [squad[5] for squad in dict_teams.values()]},
            {'header': '2º volante', 'items': [squad[6] for squad in dict_teams.values()]}, {'header': 'Meias Ofensivos', 'items': [squad[7] for squad in dict_teams.values()]},
            {'header': 'Pontas Direitas', 'items': [squad[8] for squad in dict_teams.values()]}, {'header': 'Centroavantes', 'items': [squad[9] for squad in dict_teams.values()]},
            {'header': 'Pontas Esquerdas', 'items': [squad[10] for squad in dict_teams.values()]}, {'header': 'Técnicos', 'items': [squad[11] for squad in dict_teams.values()]}]

sorted_items = sort_items(players, direction="vertical", multi_containers=True)

scores = {}
teams_rnk = {}
for team in dict_teams.keys():
    scores[team] = 0
    teams_rnk[team] = []

for team in scores.keys():
    for i,player in enumerate(dict_teams[team]):
        ranking = sorted_items[i]["items"].index(player)
        scores[team] += len(scores) - ranking
        teams_rnk[team].append(ranking)

def show_team(team):
    for i in range(12):
        st.write(f"{dict_teams[team][i]} - {teams_rnk[team][i]+1}º em sua posição")

def duel(team1, team2, print_=False):
    s1, s2 = 0, 0
    for i in range(12):
        if teams_rnk[team1][i] < teams_rnk[team2][i]:
            s1 += 1
            if print_:
                st.write(f"{dict_teams[team1][i]} > {dict_teams[team2][i]}\t{team1} {s1} x {s2} {team2}")
        else:
            s2 += 1
            if print_:
                st.write(f"{dict_teams[team2][i]} > {dict_teams[team1][i]}\t{team1} {s1} x {s2} {team2}")
    if print_:
        st.divider()
        st.write(f"{team1} {s1} x {s2} {team2}")
    return s1, s2

def league():
    league_table = pd.DataFrame("", index=dict_teams.keys(), columns=[k for k in dict_teams.keys()])
    league_table['Vitórias'] = 0
    league_table['Empates'] = 0
    league_table['Derrotas'] = 0
    league_table['Score'] = scores.values()

    for team1 in dict_teams.keys():
        for team2 in dict_teams.keys():
            if team1 != team2:
                s1, s2 = duel(team1, team2)
                league_table.loc[team1, team2] = f"{s1}x{s2}"
                league_table.loc[team2, team1] = f"{s2}x{s1}"
                if s1 > s2:
                    league_table.loc[team1, 'Vitórias'] += 1
                    league_table.loc[team2, 'Derrotas'] += 1
                elif s1 < s2:
                    league_table.loc[team2, 'Vitórias'] += 1
                    league_table.loc[team1, 'Derrotas'] += 1
                else:
                    league_table.loc[team1, 'Empates'] += 1
                    league_table.loc[team2, 'Empates'] += 1
            else:
                league_table.loc[team1, team2] = "-"

    league_table = league_table.sort_values('Vitórias', ascending=False)
    print(league_table)
    return league_table

with st.expander("Tabela de classificação"):
    st.dataframe(league())

with st.expander("Exibir uma equipe"):
    shown_team = st.selectbox("Time", list(dict_teams.keys()))
    show_team(shown_team)

with st.expander("Confronto entre duas equipes"):
    duel_teams = st.multiselect("Escolha dois times", list(dict_teams.keys()))
    if len(duel_teams) == 2:
        duel(duel_teams[0], duel_teams[1], print_=True)
