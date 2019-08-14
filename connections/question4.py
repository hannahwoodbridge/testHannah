"""
    addition
"""
import random
import numpy as np
from collections import Counter
from sklearn.neighbors import KernelDensity

from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4: implement this method
        """
        durations = list(self.peer_pool.values())

        return durations


class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4: implement this method
        """
        # flatten durations into a single numpy array
        durations = np.array([item for sublist in self.backend_database
                                   for item in sublist])
        # the grid we'll use for plotting
        x_grid = np.linspace(0, 300, 6)
        kde_skl = KernelDensity(bandwidth=0.6)
        kde_skl.fit(durations.reshape(-1, 1))
        # score_samples() returns the log-likelihood of the samples
        log_pdf = kde_skl.score_samples(x_grid.reshape(-1, 1))

        return np.exp(log_pdf)


    def process_backend_data(self):
        """
            Question 4: implement this method
        """
        # flatten durations into a single numpy array
        durations = np.array([item for sublist in self.backend_database
                                   for item in sublist])
        digitized = np.digitize(durations, BINS)
        counts = Counter(digitized)

        return counts


if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
