EXPECTED_BAKE_TIME = 40
MINS_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes depending on the number of layers of lasagna

    :param number_of_layers: int
    :return: int * int (in minutes) derived from 'MINS_PER_LAYER'.

    Function that takes the number of layers the lasagna has as
    an argument and returns how long it takes to prepare the lasagna
    based on the `MINS_PER_LAYER`.
    """
    return number_of_layers * MINS_PER_LAYER
    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param number_of_layers: int defined previously
    :return: preparation_time_in_minutes + elapsed_bake_time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time