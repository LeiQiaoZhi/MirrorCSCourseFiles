from sorting_test import *
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    # tests
    # LESSON 1
    # algos = [selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort]
    # LESSON 2
    algos = [count_sort, radix_sort]
    for sort_algo in algos:
        # plot_sort_using_plotter(sort_algo, list(range(1000, 3000, 1000)))
        times, lengths = get_time_used(
            sort_algo, list(range(1000, 10000, 1000)))
        test_in_place_sort(sort_algo, [10, 100, 1000])

        # plot for one alog
        ax.plot(lengths, times, label=sort_algo.__name__)

    Logger.title("Testing Finished", char='=', total_length=60)

    ax.legend()
    ax.set_title("Time used vs Lengths")
    plt.savefig(os.path.join(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__)))), "plots", "Time used vs Lengths (Linear Sorts)"))
    # plotter.plot()


if __name__ == '__main__':
    main()
