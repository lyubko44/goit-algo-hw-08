import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    
    total_cost = 0
    while len(cables) > 1:
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        
        combined_cable = shortest1 + shortest2
        total_cost += combined_cable
        
        heapq.heappush(cables, combined_cable)
    
    return total_cost

cable_lengths = [10, 20, 30, 40, 50]
result = min_cost_to_connect_cables(cable_lengths)
print("Total cost:", result)