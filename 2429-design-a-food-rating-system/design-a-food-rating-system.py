class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        self.cuisines_heap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)
            if cuisine not in self.cuisines_heap:
                self.cuisines_heap[cuisine] = []
            heapq.heappush(self.cuisines_heap[cuisine], [-rating, food]) # -rating for max_heap
        
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.food_info[food]
        self.food_info[food] = (cuisine, newRating) # Update map
        heapq.heappush(self.cuisines_heap[cuisine], [-newRating, food]) # Push new update into heap

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines_heap[cuisine]
        while heap:
            rating, food = heap[0]
            curr_cuisine, curr_rating = self.food_info[food]
            # Lazty deletion
            if curr_cuisine != cuisine or -rating != curr_rating:
                heapq.heappop(heap)
                continue
            return food
        return ''
        
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)