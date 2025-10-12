import time
from max_flow import MaxFlowDict

MY_TEAM = 0


def computer_scores(champ: str, matches_list: list[str]):
    num_teams, num_games, played_games = champ.split(" ")
    num_teams = int(num_teams)
    num_games = int(num_games)
    teams_score = [0] * num_teams
    teams_remaining_games = [[0] * num_teams for _ in range(num_teams)]

    for idx in range(num_teams):
        for sub_idx in range(idx + 1, num_teams):
            teams_remaining_games[idx][sub_idx] = teams_remaining_games[sub_idx][idx] = num_games

    for match_info in matches_list:
        if not match_info:
            continue
        team_a, result, team_b = match_info.split(" ")
        team_a, team_b = int(team_a), int(team_b)
        if result == "<":
            teams_score[team_b] += 2
        elif result == "=":
            teams_score[team_a] += 1
            teams_score[team_b] += 1
        if teams_remaining_games[team_a][team_b] > 0:
            teams_remaining_games[team_a][team_b] -= 1
            teams_remaining_games[team_b][team_a] -= 1

    return num_teams, num_games, played_games, teams_score, teams_remaining_games


def can_target_win(num_teams: int, scores: list, remaining_games: list):
    target_team_max = _get_target_max_posssible_score(scores, remaining_games)
    rivals_won = _check_rivals_won(target_team_max, scores)
    if rivals_won:
        return False

    source, terminal = "source", "terminal"
    graph = MaxFlowDict(source_name=source, terminal_name=terminal)
    rivals_total_pool = 0

    rivals_cap = [0] * (num_teams)
    for idx in range(num_teams):
        if idx != MY_TEAM:
            cap_idx = (target_team_max - 1) - scores[idx]
            rivals_cap[idx] = cap_idx

    for team_a in range(num_teams):
        if team_a != MY_TEAM:
            for team_b in range(team_a + 1, num_teams):
                if team_b != MY_TEAM:
                    games = remaining_games[team_a][team_b]
                    if games <= 0:
                        continue
                    node_game = f"{team_a}x{team_b}"
                    cap_pair = 2 * games
                    rivals_total_pool += cap_pair

                    graph.add_edge(source, node_game, cap_pair)

                    graph.add_edge(node_game, team_a, cap_pair)
                    graph.add_edge(node_game, team_b, cap_pair)

    for team in range(num_teams):
        if team != MY_TEAM:
            if rivals_cap[team] > 0:
                graph.add_edge(team, terminal, rivals_cap[team])

    # 4) Checa se todo pool escoa
    flow = graph.max_flow()
    return flow == rivals_total_pool


def _get_target_max_posssible_score(scores: list, remaining_games: list):
    remaining = sum(remaining_games[MY_TEAM])
    points_max = scores[MY_TEAM] + 2 * remaining

    return points_max


def _check_rivals_won(target_team_max: int, scores: list):
    result = False
    for i in range(len(scores)):
        if i != MY_TEAM:
            if scores[i] > target_team_max - 1:
                result = True

    return result


if __name__ == "__main__":
    start_time = time.perf_counter()
    championship_states = open("./tp1_grafos/hooligan/data.txt").read().splitlines()
    champs_list = []
    current_champ = None
    current_champ_matches = []
    for line in championship_states:
        line_split = line.split(" ")
        if all(x.isdigit() for x in line_split):
            if line_split[0] == "0" and line_split[1] == "0" and line_split[2] == "0":
                break
            if current_champ is not None:
                champs_list.append((current_champ, current_champ_matches))
            current_champ = line
            current_champ_matches = []
        else:
            current_champ_matches.append(line)

    if current_champ is not None:
        champs_list.append((current_champ, current_champ_matches))

    for champ_info, matches_list in champs_list:
        num_teams, num_games, played_games, current_score, remaining_games = computer_scores(champ_info, matches_list)

        result = can_target_win(int(num_teams), current_score, remaining_games)
        print(f"result: {result}")

    end_time = time.perf_counter()
    print(f"Code Performance: {end_time - start_time}")
