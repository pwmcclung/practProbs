from preloaded import alpha

def name_score(name):
    score = []
    name_list = list(name.upper())
    for x in name_list:
        for key, value in alpha.items():
            if x in key:
                score.append(value)
    summed_score = sum(score)
    summed_dict = {f'{name}':summed_score}
    return summed_dict