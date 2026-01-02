class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        neighbor = collections.defaultdict(list)

        if not beginWord or not endWord or endWord not in wordList or not wordList:
            return 0

        for word in wordList:
            for i in range(len(word)):
                adj_word = word[:i] + "#" + word[i + 1:]
                neighbor[adj_word].append(word)

        q, visit, res = collections.deque([beginWord]), set([beginWord]), 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    adj_word = word[:j] + "#" + word[j + 1:]
                    for nei in neighbor[adj_word]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

            res += 1

        return 0
