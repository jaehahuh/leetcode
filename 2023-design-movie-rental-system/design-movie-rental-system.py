class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # movie_id -> SortedList[(price, shop)]
        self.available_by_movie = defaultdict(SortedList)
        # (shop, movie) -> price
        self.price_of = {}
        # SortedList[(price, shop, movie)]
        self.rented = SortedList()

        for shop, movie, price in entries:
            self.available_by_movie[movie].add((price, shop))
            self.price_of[(shop, movie)] = price
    
    def search(self, movie: int) -> List[int]:
        result = []
        n = len(self.available_by_movie[movie])
        for i in range(5):
            if i == n: 
                break
            result.append(self.available_by_movie[movie][i][1]) # [shop]
        return result

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_of[(shop, movie)]
        self.available_by_movie[movie].discard((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_of[(shop, movie)]
        self.available_by_movie[movie].add((price, shop))
        self.rented.discard((price, shop, movie))

    def report(self) -> List[List[int]]:
        result = []
        n = len(self.rented)
        for i in range(5):
            if i == n: break
            result.append([self.rented[i][1], self.rented[i][2]]) #[shop, movie]
        return result


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()