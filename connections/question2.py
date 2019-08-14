from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ2(Peer):

    def send_data_to_backend(self):
        """
            Question 2: implement this method
        """
        durations = list(self.peer_pool.values())

        return durations


class SimulationQ2(Simulation):

    def generate_network(self):
        self.network =  [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 2: implement this method
        """
        final_counts = compute_histogram_bins(self.backend_database[0], BINS)
        for durations in self.backend_database[1:]:
            counts = compute_histogram_bins(durations, BINS)
            final_counts = {key: final_counts[key] + counts[key]
                            for key in final_counts.keys()}
        print(final_counts)
        return final_counts

if __name__ == "__main__":

    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
