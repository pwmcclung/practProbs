def loose_change(cents):
    cents = int(cents) 

    if cents <= 0:
        return {'Quarters': 0, 'Dimes': 0, 'Nickels': 0, 'Pennies': 0}

    quarters = cents // 25
    cents %= 25  

    dimes = cents // 10
    cents %= 10  

    nickels = cents // 5
    cents %= 5  

    pennies = cents

    return {
        'Quarters': quarters,
        'Dimes': dimes,
        'Nickels': nickels,
        'Pennies': pennies
    }