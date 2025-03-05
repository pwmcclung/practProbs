def jumbled_solar_system(solar_system):
    size_order = ["Asteroid", "Pluto", "Mercury", "Mars", "Venus", "Earth", "Neptune", "Uranus", "Saturn", "Jupiter"]
    result = []

    if not solar_system:
        return result

    def get_size_index(body):
        return size_order.index(body)

    for i in range(1, len(solar_system)):
        left = solar_system[i - 1]
        right = solar_system[i]

        if right == "Asteroid" and left == "Asteroid":
            result.append("=")
        elif right == "Asteroid":
            result.append("<") 
        else:
            if get_size_index(right) > get_size_index(left):
                result.append(">")
            elif get_size_index(right) < get_size_index(left):
                result.append("<")
            else:
                result.append("=")

    return result