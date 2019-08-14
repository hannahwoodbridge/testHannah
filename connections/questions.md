# Questions

## Question 1

Fill in the two functions `compute_histogram_bins` and `plot_histogram` in `histogram.py`. As an example, we would like to be able to plot something similar to histogram_example.png` as a minimum result.

## Question 2

Go to the file `question2.py`:
1. fill in `send_data_to_backend` so that it returns the list of the peer's connection durations.
2. fill in `process_backend_data` which must do all necessary processing to return the connection durations histogram bins counts. **Don't call `plot_histogram` in this method, we just want to compute the histogram bins counts**.

## Question 3

With peers sending such datastructure and our _backend_ server making such operations, we retrieve exactly **all** the connection durations on the network at the moment of the snapshot and we are able to plot the _exact distribution_ of the connection durations.
1. `question2.py` main has several simulations with increasing numbers of peers and peer pool size. Run the simulations with your implementation. What do you see? Can you explain the limitations of the implementations of question 2 taking into account that a _real_ peer network can have _millions_ of peers? (answer below in this file)

>> Backend processing time increases with the number of peers but most quickly
with the max peer pool size. When computing the durations, we are looping through each peer and each of its neighbours. The complexity is  O(n_peers*max_peer_pool_size). We could reduce this by viewing the network as a graph (where a peer is a vertice and the connection duration is an edge) and do a single depth first search to get all of the connection durations in a single list. This also would avoid looping through a list of lists in process_backend_data.



## Question 4

Go to the file `question4.py`:
1. propose new implementations of `send_data_to_backend` and `process_backend_data` that can deal with millions of peers _and_ still provide a good representation of the _distribution_ of the connection duration. You are free to add any written comments, add pictures etc...to enhance your answer.

>> Here we can't modify retrieve_data_from_peers so are trying different approaches:

Kernel density estimation to avoid calculating the bin for each value.
Is actually slower in implementation:
Running peer simulation with:
 - number_of_peers: 10
 - max_peer_pool_size: 2
Backend processing time: 0:00:00.001100

Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 10
Backend processing time: 0:00:00.027508

Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 100
Backend processing time: 0:00:00.669203

Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 1000
Backend processing time: 0:00:07.871220

Running peer simulation with:
 - number_of_peers: 10000
 - max_peer_pool_size: 10
Backend processing time: 0:00:00.605157

Running peer simulation with:
 - number_of_peers: 10000
 - max_peer_pool_size: 100
Backend processing time: 0:00:52.608474

We could also try a different binning approach: using numpy.digitize and a Counter speeds up the computation a bit.
Counter({7: 12, 4: 6, 2: 4, 5: 4, 3: 2})
Running peer simulation with:
 - number_of_peers: 10
 - max_peer_pool_size: 2
Backend processing time: 0:00:00.000377

Counter({7: 10116, 6: 3156, 5: 1622, 4: 1606, 3: 1602, 2: 1356, 1: 322})
Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 10
Backend processing time: 0:00:00.017212

Counter({7: 90832, 6: 30478, 4: 15056, 5: 15048, 3: 14700, 2: 12050, 1: 2964})
Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 100
Backend processing time: 0:00:00.092867

Counter({7: 374356, 6: 124776, 5: 61946, 3: 61784, 4: 61654, 2: 50036, 1: 12376})
Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 1000
Backend processing time: 0:00:00.497087

Counter({7: 100272, 6: 32692, 5: 16842, 3: 16694, 4: 16546, 2: 13466, 1: 3326})
Running peer simulation with:
 - number_of_peers: 10000
 - max_peer_pool_size: 10
Backend processing time: 0:00:00.103022

Counter({7: 990058, 6: 329664, 3: 165484, 5: 165286, 4: 165076, 2: 131738, 1: 32786})
Running peer simulation with:
 - number_of_peers: 10000
 - max_peer_pool_size: 100
Backend processing time: 0:00:01.257111

We could also reduce the number of bins to speed it up more, if we are just interested in an approximate distribution.
