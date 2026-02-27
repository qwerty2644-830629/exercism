"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    return touching_dot or touching_power_pellet
    

def lose(power_pellet_active, touching_ghost):
    return(not power_pellet_active) and touching_ghost
    

def win(has_eat_all_dot, power_pellet_active, touching_ghost):
    return has_eat_all_dot and not ( touching_ghost and (not power_pellet_active))