class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [0] * len(T)

        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer
