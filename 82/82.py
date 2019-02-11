# Copyright 2019 fssqawj Holding Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import codecs
import queue


def add_edge(s, t, edge_map):
    if s not in edge_map:
        edge_map[s] = []
    edge_map[s].append(t)


def make_node(x, y, n):
    return x * n + y


class Node:
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


if __name__ == '__main__':
    dis = []
    n = 80
    with codecs.open('p082_matrix.txt', 'r', encoding='utf-8') as fin:
        for line in fin:
            dis.extend([int(x) for x in line.strip().split(',')])
        # print(dis)
        dis.extend([0, 0])
        edge_map = {}
        start = n * n
        end = start + 1
        edge_map[start] = [i * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i > 0:
                    add_edge(make_node(i, j, n), make_node(i - 1, j, n), edge_map)
                if i < n - 1:
                    add_edge(make_node(i, j, n), make_node(i + 1, j, n), edge_map)
                if j < n - 1:
                    add_edge(make_node(i, j, n), make_node(i, j + 1, n), edge_map)
        # print(edge_map)

        for i in range(1, n + 1):
            edge_map[i * n - 1] = [end]

        que = queue.PriorityQueue()
        que.put(Node(start, 0))
        vis = [False] * (n * n + 3)
        vis[start] = True
        while not que.empty():
            node = que.get()
            vis[node.idx] = False
            if node.idx == end:
                print(node.value)
                break
            for idx in edge_map[node.idx]:
                if not vis[idx]:
                    que.put(Node(idx, node.value + dis[idx]))
                    vis[idx] = True


