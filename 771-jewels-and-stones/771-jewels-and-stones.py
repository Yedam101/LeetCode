class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        st = collections.Counter(stones)
        j = list(set(jewels))

        count = 0

        for i in j:
            count += st.get(i, 0)

        return count
        