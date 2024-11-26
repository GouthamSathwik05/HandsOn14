# -*- coding: utf-8 -*-
"""HandsOn14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/121vC81Fy6GeK0LksrsefTbyih8vLn3aP
"""

import heapq
def dijkstra(graph, start):
  distances={vertex: float('infinity') for vertex in graph}
  distances[start]=0
  pq=[(0, start)]
  while pq:
    current_distance, current_vertex=heapq.heappop(pq)
    if current_distance>distances[current_vertex]:
      continue
    for neighbor, weight in graph[current_vertex].items():
      distance=current_distance+weight
      if distance<distances[neighbor]:
        distances[neighbor]=distance
        heapq.heappush(pq, (distance, neighbor))
  return distances
graph={
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(graph, 'A'))

def bellman_ford(graph, vertices, start):
  distances={vertex: float('infinity') for vertex in vertices}
  distances[start]=0
  for _ in range(len(vertices) - 1):
    for u in graph:
      for v, weight in graph[u].items():
        if distances[u]+weight<distances[v]:
          distances[v]=distances[u]+weight
    for u in graph:
      for v, weight in graph[u].items():
        if distances[u]+weight<distances[v]:
          raise ValueError("Graph contains negative weight cycle")
  return distances
graph={
    'A': {'B': 1, 'C': 4},
    'B': {'C': -2, 'D': 1},
    'C': {'D': 3},
    'D': {'A': -1}
}
vertices=['A', 'B', 'C', 'D']
print(bellman_ford(graph, vertices, 'A'))

def floyd_warshall(graph):
  vertices=list(graph.keys())
  dist={vertex: {v: float('infinity') for v in vertices} for vertex in vertices}
  for u in vertices:
    dist[u][u]=0
    for v, weight in graph.get(u, {}).items():
      dist[u][v]=weight
  for k in vertices:
    for i in vertices:
      for j in vertices:
        if dist[i][j]>dist[i][k]+dist[k][j]:
          dist[i][j]=dist[i][k]+dist[k][j]
  return dist
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(floyd_warshall(graph))