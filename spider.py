import math

def spider_to_fly(spider, fly):

    def get_coordinates(web_coordinate):

        radial = web_coordinate[0]
        ring = int(web_coordinate[1:])
        return radial, ring

    spider_radial, spider_ring = get_coordinates(spider)
    fly_radial, fly_ring = get_coordinates(fly)

    radial_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    spider_angle = radial_index[spider_radial]
    fly_angle = radial_index[fly_radial]

    angle_difference = abs(spider_angle - fly_angle)
    angle_difference = min(angle_difference, 8 - angle_difference)

    if spider_ring == 0 or fly_ring == 0:
        return float(spider_ring + fly_ring)

    return math.sqrt(spider_ring**2 + fly_ring**2 - 2 * spider_ring * fly_ring * math.cos(math.pi * angle_difference / 4))