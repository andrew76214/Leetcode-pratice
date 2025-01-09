class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatest_candies = max(candies)
        kids_note = []

        for i in range(len(candies)):
            kids_note.append(candies[i] + extraCandies >= greatest_candies)

        return kids_note
