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
        
        map = []
        for vertex in self.graph:
            for node,val in self.info["bandwidths"].items():
                if(vertex==node): 
                    map.append((vertex,val,self.graph[vertex]))

        sorted_map = sorted(map, key= lambda x: x[1])
        #map is a sorted list of (node, bandwidth of node, connected nodes list)
        print(sorted_map)
       
        
        
        
        

        paths = bfs_path(self.graph, self.isp, self.info["list_clients"])
        bandwidths.update(self.info["bandwidths"])

        return (paths, bandwidths, priorities)

