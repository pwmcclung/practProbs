def goto(level,button):
    if not isinstance(level, int):
        return 0
    elif not isinstance(button, str):
        return 0
    if int(button) < 0 or int(button) > 3 or level > 3 or level < 0:
        return 0
    if int(button) == level:
        return 0
    if int(button) > level:
        return abs(level - int(button))
    if int(button) < level:
        return int(button) - level