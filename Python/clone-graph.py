# Time:  O(n)
# Space: O(n)
#
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# 
# 
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
# 
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# 
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
# 
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
# 
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
#
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        cloned_node = UndirectedGraphNode(node.label)
        cloned, queue = {node:cloned_node}, [node]
        
        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    queue.append(neighbor)
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    cloned[neighbor] = cloned_neighbor
                cloned[current].neighbors.append(cloned[neighbor])
        return cloned[node]


"""
1. Can I think for a second?
2. Think loud

전체를 다 트래버스 하는 방법으로 DFS와 BFS가 있는데,
DFS는 스택이나 재귀를 사용하고, BFS는 큐를 사용하죠
둘 다 오엔 타임, 오엔 공간인데, 간단하게 재귀로 DFS로 해 볼까요?

DFS는 해쉬테이블를 파라메터로 가지는 재귀함수를 정해두고 그 함수를 재귀합니다.

재귀함수는 처음에 입력받은 노드가 해쉬테이블에 있으면 그냥 만들지 않고 그걸 리턴합니다.
입력받은 노드의 값을 가지는 새로운 그래프노드를 만들고 해쉬에 넣습니다.
그리고 입력받은 노드의 이웃들만큼 재귀해서 이웃들로 어펜드처리합니다.
그리고 새로운 그래프노드를 리턴합니다.

----

BFS로 접근한다라고 한다면
큐를 하나 만들어서 노드를 집어넣고,
해쉬테이블에는 카피한 노드를 하나 집어넣습니다.

큐가 차 있으면 하나를 꺼내서 커라고 하면
    커의 이웃들만큼 반복하는데 엔라고 하면
        엔이 해쉬테이블에 이미 들어 있다면
            만들지 않고 그냥 이웃에 엔을 등록
        들어 있지 않다면
            엔카피를 하나만들고
            커의 이웃에 엔투카피를 등록
            엔카피를 해쉬테이블에 등록
            큐에 엔을 등록

이웃들의 처리가 끝났으므로 노트카피를 리턴 

"""
