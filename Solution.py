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
        print(self.info["rho1"])
        print(self.info["rho2"])
        print(self.info["is_fcc"])
        paths = {}
        bandwidths = self.info["bandwidths"].copy()
        priorities = {}  # If priorities are needed, populate them accordingly

        def bfs_path(graph, isp, list_clients):
            myQueue = []
            myQueue.append((isp, []))
            visited = set()

            while myQueue and list_clients:
                currentNode, pathSoFar = myQueue.pop(0)

                if currentNode in visited:
                    continue

                visited.add(currentNode)
                newPathSoFar = pathSoFar.copy()
                newPathSoFar.append(currentNode)

                if currentNode in list_clients:
                    list_clients.remove(currentNode)
                    paths[currentNode] = newPathSoFar

                for neighbor in graph[currentNode]:
                    if neighbor not in visited:
                        myQueue.append((neighbor, newPathSoFar))
            
            return paths

        bfsclients = self.info["list_clients"].copy()
        bfs_path(self.graph, self.isp, bfsclients)

        currentlyFilled = [0] * len(self.graph)
        ticks = [1] * len(self.graph)
        pathsFinished = 0
        nodes = self.info["list_clients"].copy()
        paths2 = paths.copy()

        while len(nodes) != 0:
            nodesToMove = nodes.copy()
            visitedNodes = []

            while len(nodesToMove) != 0:
                client = nodesToMove.pop(0)

                if client in visitedNodes:
                    for i in range(len(currentlyFilled)):
                        currentlyFilled[i] -= self.info["bandwidths"][i]
                        if currentlyFilled[i] < 0:
                            currentlyFilled[i] = 0
                else:
                    visitedNodes.append(client)

                path = paths2[client]
                nodeToVisit = path.pop(1)

                if nodeToVisit == client:
                    nodes.remove(client)
                    pathsFinished += 1
                    ticks[client] += 1

                #print(ticks)

                alpha_complaint=0
                band_cost = self.info["cost_bandwidth"]
                beta_complaint = 0

                alpha = self.info["alphas"][client]
                beta = self.info["betas"][client]

                threshold_fcc = self.info["rho2"]

                #idk if we wanna increase band for everyone who complains
                if (ticks[client] > beta):
                    if(client in self.info["is_fcc"]):
                        beta_complaint += 1

                if(beta_complaint > threshold_fcc * len(self.info["is_fcc"])):
                    bandwidths[client] += 1
                    band_cost += self.info["cost_bandwidth"]

                #i assume we have to increase everytime there is a tick>unsubscribe thres
                if (ticks[client] > alpha):
                    if(client in self.info["is_fcc"]):
                        bandwidths[client] += 1
                        band_cost += self.info["cost_bandwidth"]
                        alpha_complaint += 1
                

                fill = currentlyFilled[nodeToVisit]

                if fill < self.info["bandwidths"][nodeToVisit]:
                    currentlyFilled[nodeToVisit] += 1
                else:
                    nodesToMove.append(client)
                    paths2[client].insert(0, nodeToVisit)

                
                #if(ticks[client] > beta):
                    

        

        return paths2, self.info["bandwidths"], priorities
