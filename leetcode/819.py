import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub('[^\w]', ' ', paragraph)
        .lower().split()
                 if word not in banned]
        result = Counter(words)
        return result.most_common(1)[0][0]
