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

    def output_paths(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """
        paths, bandwidths, priorities = {}, {}, {}

        
        map = []
        bandwidths = self.info["bandwidths"]
        alphas = self.info["alphas"]
        for vertex in self.graph:
            if vertex in bandwidths and vertex in alphas:
                map.append((vertex, bandwidths[vertex], alphas[vertex], self.graph[vertex]))


        #map is a sorted list of (node, bandwidth of node, alpha)
        #print(map)

        distance = {}
        distance[self.isp] = 0
        for i in self.graph:
            distance[i] = 999999999999999999999999999999999
            queue=[]
        queue.append((self.isp,0))

        explored= []
        explored.append(self.isp)

        sorted_map = sorted(map, key=lambda x: x[1])

        while(len(queue)!= 0):
            node, dis = heapq.heappop(queue)
            if(node not in explored):
                explored.append(node)
            
            for next_node, weight, apl, edge_list in map:
                D = distance[node] + weight
                if(D<=apl):
                    if (D < distance[next_node]):
                        distance[next_node] = D
                        heapq.heappush(queue, (next_node, D))
                        paths[node]=next_node



        return (paths, bandwidths, priorities)
