def find_warrior_rank(skill):
    if skill >= 10:
        end = 'rathi'
        mid = 'maha-' * (skill // 10)
        if skill - ((skill //10) * 10) > 7:
            return 'maha-' + mid + end
        elif skill - ((skill //10) * 10) > 2 and skill - ((skill //10) * 10) < 8:
            return 'ati-' + mid + end
        else: 
            return mid + end
    if skill < 8 and skill > 2:
        return 'ati-rathi'
    if skill < 3:
        return 'rathi'