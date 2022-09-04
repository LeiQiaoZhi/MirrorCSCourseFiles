from sorting import *
import random
from utils.logger import Logger
import time
from typing import *
from utils.plotter import Plotter

# set seed for reproducibility
random.seed(1234)

plotter = Plotter()


def test_in_order(list_to_test):
    in_order = (list_to_test == sorted(list_to_test))
    if in_order:
        Logger.important(
            "\nGood job. The sorted list is in order.", color=Logger.GREEN)
    else:
        Logger.important(
            "\nAppears that the sorted list is not in order. :(", color=Logger.RED)
        Logger.info(f"Sorted list should be {sorted(list_to_test)}")


def test_selection_sort(lengths: Union[int, List[int]] = 20):
    if isinstance(lengths, int):
        lengths = [lengths]

    for length in lengths:
        Logger.print_title(
            f"Testing Selection Sort | Length: {length}", char='=', total_length=60)

        list_to_sort = [random.randint(0, length*2) for _ in range(length)]
        Logger.info(
            f"Original list: {list_to_sort if length <= 10 else str(list_to_sort[:10]) + ' ......'}")

        start_time = time.time()
        selection_sort(list_to_sort)
        end_time = time.time()

        Logger.info(
            f"Sorted list: {list_to_sort if length <= 10 else str(list_to_sort[:10]) + ' ......'}")

        # time used
        time_used = round(end_time-start_time, 5)
        Logger.info(
            f"\nThe algorithm takes {Logger.bold(Logger.blue(time_used))} ms"
            f" to sort a list of length {Logger.bold(Logger.blue((length)))}")

        # plot time used
        plotter.add_scalar("Time vs Length", x=length,
                           y=time_used, xlabel="Length", ylabel="Time Used")

        test_in_order(list_to_sort)


def main():
    test_selection_sort(list(range(100, 10000, 1000)))

    Logger.title("Testing Finished", char='=', total_length=60)

    plotter.plot()


if __name__ == '__main__':
    main()
