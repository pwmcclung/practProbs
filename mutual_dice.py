def mutually_exclusive(dice, call1, call2):
    total = 0
    total_dice = 0
    for x in range(len(dice)):
        total_dice += dice[x][1]
        if dice[x][0] == call1 or dice[x][0] == call2:
            total += dice[x][1]
    rounded_dice = round(total,2)
    if total_dice != 1.0:
        return None
    else:
        return f'{rounded_dice:.2f}'