# --- RANDOM SPAWN OF TARGET (ISKANDER) ---

from module import imports
np = imports().np
random = imports().random

def random_target_spawn():
    choice = random.choice(["bottom", "left", "top"])

    if choice == "bottom":
        x = np.random.uniform(-250, -100)
        y = -170
    elif choice == "left":
        x = -100
        y = np.random.uniform(-170, 170)
    else:  # "top"
        x = np.random.uniform(-250, -100)
        y = 170
    return x, y