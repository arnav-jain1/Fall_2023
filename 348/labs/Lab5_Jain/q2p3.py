def nfl_combinations(score):
    combinations = []

    for td_2pt in range(score // 8 + 1):
        for td_fg in range((score - td_2pt * 8) // 7 + 1):
            for td in range((score - td_2pt * 8 - td_fg * 7) // 6 + 1):
                for fg in range((score - td_2pt * 8 - td_fg * 7 - td * 6) // 3 + 1):
                    safety = score - (fg * 3 + td * 6 + td_fg * 7 + td_2pt * 8)
                    if safety % 2 == 0:
                        safety //= 2
                        print(f"{td_2pt} TD + 2pt, {td_fg} TD + FG, {td} TD, {fg} 3pt FG, {safety} Safety")

    return combinations

score = 25
nfl_combinations(score)