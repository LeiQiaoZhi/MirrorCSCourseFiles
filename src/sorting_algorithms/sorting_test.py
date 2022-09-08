import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

try:
    from utils.plotter import Plotter
    from typing import *
    import time
    from utils.logger import Logger
    import random
    from sorting import *
except:
    print("Import Failed")
    quit()


# set seed for reproducibility
random.seed(1234)

plotter = Plotter()


def test_in_order(list_to_test, sorted_original_list):
    in_order = (list_to_test == sorted_original_list)
    if in_order:
        Logger.important(
            "\nGood job. The sorted list is in order.", color=Logger.GREEN)
    else:
        Logger.important(
            "\nAppears that the sorted list is not in order. :(", color=Logger.RED)
        Logger.info(
            f"Sorted list should be {sorted_original_list if len(sorted_original_list) <= 10 else str(sorted_original_list[:10])[:-1]+ ' ......'}")


def plot_sort_using_plotter(sort_fn: Callable, lengths: Union[int, List[int]] = 20):
    if isinstance(lengths, int):
        lengths = [lengths]

    Logger.print_title(
        f"Plotting {sort_fn.__name__} | Lengths: {lengths}", char='*', total_length=60)

    for length in lengths:

        list_to_sort = [random.randint(0, length*2) for _ in range(length)]

        start_time = time.time()
        sort_fn(list_to_sort)
        end_time = time.time()

        # time used
        time_used = round(end_time-start_time, 5)
        Logger.info(
            f"The algorithm takes {Logger.bold(Logger.blue(time_used))} ms"
            f" to sort a list of length {Logger.bold(Logger.blue((length)))}")

        # plot time used
        plotter.add_scalar(f"Time vs Length", x=length,
                           y=time_used, xlabel="Length", ylabel="Time Used")


def get_time_used(sort_fn: Callable, lengths: Union[int, List[int]] = 20) -> Tuple[List[float], List[int]]:
    '''
    returns time_used list, lengths
    '''
    if isinstance(lengths, int):
        lengths = [lengths]

    Logger.print_title(
        f"Plotting {sort_fn.__name__} | Lengths: {lengths}", char='*', total_length=60)

    time_used_list = []
    for length in lengths:

        list_to_sort = [random.randint(0, length*2) for _ in range(length)]

        start_time = time.time()
        sort_fn(list_to_sort)
        end_time = time.time()

        # time used
        time_used = round(end_time-start_time, 5)
        Logger.info(
            f"The algorithm takes {Logger.bold(Logger.blue(time_used))} ms"
            f" to sort a list of length {Logger.bold(Logger.blue((length)))}")

        time_used_list.append(time_used)
    return time_used_list, lengths


def test_in_place_sort(sort_fn: Callable, lengths: Union[int, List[int]] = 20):
    if isinstance(lengths, int):
        lengths = [lengths]

    for length in lengths:
        Logger.print_title(
            f"Testing {sort_fn.__name__} | Length: {length}", char='=', total_length=60)

        list_to_sort = [random.randint(0, length*2) for _ in range(length)]
        original_sorted_list = sorted(list_to_sort)
        Logger.info(
            f"Original list: {list_to_sort if len(list_to_sort) <= 10 else str(list_to_sort[:10])[:-1] + ' ......'}")

        result = sort_fn(list_to_sort)
        if result != None:  # NOTE: if sort_fn is not in place
            list_to_sort = result

        Logger.info(
            f"Sorted list: {list_to_sort if len(list_to_sort) <= 10 else str(list_to_sort[:10])[:-1] + ' ......'}")

        test_in_order(list_to_sort, original_sorted_list)
