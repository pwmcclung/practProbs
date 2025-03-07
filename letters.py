from collections import Counter

def play_if_enough(hand, play):

    hand_count = Counter(hand)
    play_count = Counter(play)

    can_play = all(hand_count[resource] >= play_count[resource] for resource in play_count)

    if can_play:
        updated_hand = ""
        for resource, count in hand_count.items():
            updated_hand += resource * (count - play_count.get(resource, 0))
        return (True, updated_hand)
    else:
        return (False, hand)