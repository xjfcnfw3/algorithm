import collections

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        result = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            result.append(start)

        dfs("JFK")
        return result[::-1]