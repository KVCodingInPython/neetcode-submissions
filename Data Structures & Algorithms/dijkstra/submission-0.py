class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        # Create adjacency list
        adj = {i: [] for i in range(n)}

        for s, d, w in edges:
            adj[s].append((d, w))

        # Map of shortest paths from source to node
        # More correct Dijkstras approach: Initialize with inf
        shortest = {i: float('inf') for i in range(n)}
        shortest[src] = 0        


        # Priority queue to explore nodes, starting from source
        minHeap = [(0, src)] # (weight, node)
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            # Only proceed if the current path is still relevant
            if w1 > shortest[n1]:
                continue
            
            for n2, w2 in adj[n1]:
                new_dist = w1 + w2
                if new_dist < shortest[n2]:
                    shortest[n2] = new_dist
                    heapq.heappush(minHeap, (new_dist, n2))
            
            
        # Check for any nodes that were not reachable
        for i in range(n):
            if shortest[i] == float("inf"):
                shortest[i] = -1


        return shortest


