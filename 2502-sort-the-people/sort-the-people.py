class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = []
        # combine names and heights into a list of tuples
        people = list(zip(names, heights))

        # sort the list of tuples by height in descending order
        sorted_people = sorted(people, key=lambda x:-x[1])

        for name, heights in sorted_people:
            result.append(name)
        return result