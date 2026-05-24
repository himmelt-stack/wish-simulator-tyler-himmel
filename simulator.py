import random
import numpy as np


def get_five_star_probability(pulls_since_5star):
    base = 0.006 # 0.6% chance for 5stars

    if pulls_since_5star >=90: # Hard Pity Cap
        return 1.00 
    if pulls_since_5star < 75: # Using base pity under 75 pulls
        return base

    extra = (pulls_since_5star-74)*0.06 # Soft Pity Bonuses
    return min(1.0, base+extra)

def get_four_star_probability():
    return 0.051 # 5.1% chance for 4stars





def simulate_banner(n_pulls = 100000):
    # Establishing pulls + guarantee count
    total_4stars = 0
    total_5stars = 0
    featured_5stars = 0

    # pity trackers
    pulls_since_5star = 0
    pulls_since_4star = 0

    guarantee = False

    for wishes in range(n_pulls):
        pulls_since_5star += 1
        pulls_since_4star += 1


        # 5 Star Check
        p5 = get_five_star_probability(pulls_since_5star)
        if random.random() < p5:
            total_5stars+=1
            pulls_since_5star = 0
            pulls_since_4star = 0

            # 50/50
            if guarantee:
                featured_5stars += 1
                guarantee = False
            else:
                if random.random() < 0.5:
                    featured_5stars += 1
                    guarantee = False
                else:
                    guarantee = True
            continue

        # 4 stars
        if pulls_since_4star >= 10:
            total_4stars += 1
            pulls_since_4star = 0
        else: 
            if random.random() < get_four_star_probability():
                total_4stars += 1
                pulls_since_4star = 0


    return total_4stars, total_5stars, featured_5stars






def run_many_simulations(n=10):
    return np.array([simulate_banner() for run in range(n)]) # Simulation runner function based on n input