"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:
    Nodes are labeled uniquely.

    We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

    First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    Second node is labeled as 1. Connect node 1 to node 2.
    Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        soln = UndirectedGraphNode(node.label)
        nodes = {node.label : soln}
        # DFS
        stack = [node]
        # BFS
        #stack = collections.deque([node])
        while stack:
            # DFS
            topnode = stack.pop()
            # BFS
            #topnode = stack.popleft()
            currnode = nodes[topnode.label]
            for neighbor in topnode.neighbors:
                if neighbor.label not in nodes:
                    nodes[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    stack.append(neighbor)
                currnode.neighbors.append(nodes[neighbor.label])
        return soln

"""
# Recursive dfs:
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.cloned = {}
    
    def cloneGraph(self, node):
        if not node:
            return None
        else:
            return self.dfs(node)
            
    def dfs(self, node):
        if not node:
            return None
        new_node = UndirectedGraphNode(node.label)
        self.cloned[node.label] = new_node
        for neighbor in node.neighbors:
            nb_label = neighbor.label
            if nb_label in self.cloned:
                new_node.neighbors.append(self.cloned[nb_label])
            else:
                new_node.neighbors.append(self.dfs(neighbor))
        return new_node
"""
