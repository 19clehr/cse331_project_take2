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
        paths, bandwidths, priorities = {}, {}, {}
        def bfs_path(graph, isp, list_clients):
        
            myQueue = []
            myQueue.append((isp,[]))
            visited = []
            tick = 0
            while len(list_clients) != 0:
                #print(len(list_clients))
                currentNode, pathSoFar = myQueue.pop(0)
                if currentNode not in visited:
                    visited.append(currentNode)
                else:
                    continue

                newPathSoFar = pathSoFar.copy()
                newPathSoFar.append(currentNode)
                if currentNode in list_clients:
                    list_clients.remove(currentNode)
                    paths[currentNode] = newPathSoFar
                
                for neighbor in graph[currentNode]:
                    if neighbor not in visited:
                        myQueue.append((neighbor,newPathSoFar))

            return paths
        bfsclients = self.info["list_clients"].copy()
        paths = bfs_path(self.graph,self.isp,bfsclients)


        currentlyFilled = [0]*len(self.graph)
        ticks = [1]*len(self.graph)
        pathsFinished = 0
        nodes = self.info["list_clients"].copy()
        paths2 = paths.copy()
        while len(nodes) != 0:
            nodesToMove = nodes.copy()
            visitedNodes = []
            while len(nodesToMove) != 0:
                client = nodesToMove.pop(0)
                print(client)
                if client in visitedNodes:
                    for i in range(0,len(currentlyFilled)-1):
                        currentlyFilled[i] = currentlyFilled[i] - self.info["bandwidths"][i]
                        if currentlyFilled[i] < 0:
                            currentlyFilled[i] = 0
                else:
                    visitedNodes.append(client)
                
                path = paths2[client]
                print(path)
                nodeToVist = path.pop(1)

                if nodeToVist == client:
                    print("made it")
                    print(client)
                    nodes.remove(client)
                    pathsFinished += 1
                    ticks[client] += 1
                print(len(currentlyFilled))
                print(nodeToVist)
                fill = currentlyFilled[nodeToVist]
                
                if fill < self.info["bandwidths"][nodeToVist]:
                    print("packet moved")
                    currentlyFilled[nodeToVist] += 1
                else:
                    nodesToMove.append(client)
                    paths2[client].insert(0,nodeToVist)
                    ticks[client] += 1
                

                
            
        print(ticks)        

        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """

        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, self.info["bandwidths"], priorities)
