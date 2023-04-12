from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

        #buffer is < infinity
        #theashold => 1
        #find a path that genarates the most revenue
        #is not the bfs path (so it seems)(rec)
        #bandwidth is the amount of packet it can send at a tick
        #treshold is the max wait time (so if tick > treshold == no payment) (i belive thats what alpha is gotta check again tbh)

        #isp = start node
        #client_list = info["list_clients"]
        #bandwidths = info["bandwidths"]
        #alphas(threshold) = info["alphas"]
        #payments = info["payments"]   not sure if we need to use this
        #basically create the shortest path function with these constraints
        
    def output_paths(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """
        paths, bandwidths, priorities = {}, {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        
        
        
        

        paths = bfs_path(self.graph, self.isp, self.info["list_clients"])
        bandwidths.update(self.info["bandwidths"])

        return (paths, bandwidths, priorities)

