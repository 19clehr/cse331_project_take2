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

        #self.info["list_clients"] = client list
        #self.info["alphas"] = alpha
        #self.info["bandwidths"] = bu 
        #self.info["betas"] = betas
        #self.isp = start_node

    def output_paths(self):
        paths, bandwidths, priorities = {}, {}, {}
        for client in self.info["list_clients"]:
            path = self.compute_path(self.isp, client)
            paths[client] = path
            bandwidths[client] = self.info["bandwidths"]
            priorities[client] = self.info["betas"]
        return (paths, bandwidths, priorities)

    def compute_path(self, start, client):
        max_val = 999999999999999999999999999999999999
        distances = {}
        parent = {}
        distances[start] = 0
        parent[start] = -1
        for vertex in self.graph:
            distances[vertex] = max_val
            parent[vertex] = None

        for i in range((len(self.graph)) - 1):
            situation = False

            for vertex in self.graph:
                for next_vertex in self.graph[vertex]:
                    if(distances[vertex] != max_val and 
                        distances[vertex] + self.info["bandwidths"][next_vertex] < 
                        distances[next_vertex]):
                            
                        distances[next_vertex] = distances[vertex] + self.info["bandwidths"][next_vertex]
                        parent[next_vertex] = vertex
                        situation = True
                        self.info["bandwidths"][next_vertex] -= 1 
                        
                    if (situation == False):
                        break
            
            
        path = []
        current_node = client
        while (current_node is not None):
            path.append(current_node)
            current_node = parent[current_node]
        path = path[::-1]               

        return path

