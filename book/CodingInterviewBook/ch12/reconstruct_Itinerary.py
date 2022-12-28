class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        result = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            result.append(start)

        dfs("JFK")
        return result[::-1]