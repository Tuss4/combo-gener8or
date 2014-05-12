import random

"""A tricking combination generator
"""
kicks = ['540', 'hook', 'tornado', 'cheat 720']
flips = ['front tuck', 'back tuck', 'side flip']
twists = ['btwist', 'cork', 'full twist']


def combo_generator():
    '''The combo generator function'''
    # setup your random tricks
    k = random.choice(kicks)
    f = random.choice(flips)
    t = random.choice(twists)
    return [k, t, f]


def multi_combos():
    '''List of combos'''
    for i in range(10):
        print combo_generator()

multi_combos()
