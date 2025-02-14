def how_many_pizzas(n):
    if n <= 0:
        return "pizzas: 0, slices: 0"

    area_n = (n / 2) ** 2
    area_8 = (8 / 2) ** 2

    num_pizzas_float = area_n / area_8
    num_pizzas = int(num_pizzas_float)
    remaining_area = area_n - num_pizzas * area_8
    
    remaining_slices = round((remaining_area / area_8) * 8)
    
    return f"pizzas: {num_pizzas}, slices: {remaining_slices}"