class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    

        norm = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        
        words = norm.split()

        count = defaultdict(int)
        banned = set(banned)

       
        for word in words:
            if word not in banned:
                count[word] += 1


        return max(count.items(), key=operator.itemgetter(1))[0]