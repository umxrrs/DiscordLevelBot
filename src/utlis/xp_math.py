def calculate_level(xp):
    return int((xp / 100) ** 0.5)

def calculate_xp_for_level(level):
    return int(100 * (level ** 2))
