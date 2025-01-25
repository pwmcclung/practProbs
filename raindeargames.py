def sort_reindeer(reindeer_names):
    def get_last_name(name):
        return name.split(" ")[1]
    return sorted(reindeer_names, key=get_last_name)