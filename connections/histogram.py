from random import randint

"""
    custom addition
"""
import matplotlib.pyplot as plt


def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted number that represents your histogram
              bin thresholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use
    """
    n_bins = len(bins) - 1
    counts = {f"{bins[i]}-{bins[i+1]}": 0 for i in range(n_bins)}
    counts[f"{bins[-1]}+"] = 0

    for d in data:
        if d >= bins[-1]:
            counts[f"{bins[-1]}+"] += 1
        else:
            for i in range(n_bins):
                if bins[i] <= d < bins[i+1]:
                    counts[f"{bins[i]}-{bins[i+1]}"] += 1
                    break

    return counts


def plot_histogram(bins_count):
    """
        Quesion 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommand using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    bins = list(bins_count.keys())
    counts = list(bins_count.values())
    print(bins, counts)
    ax = plt.bar(bins, counts)
    ax.set_xlabel('x')
    plt.show()

if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 120) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
