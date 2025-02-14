class ProductOfNumbers:
    def __init__(self):
        self.products = [1]
        self.last_zero_index = -1 # Index of the last zero
        
    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero_index = len(self.products)  # Save the current index as the last zero index
            self.products.append(1)  # After adding zero, initialize the product to 1
        else:
            last_product = self.products[-1]
            self.products.append(last_product * num)  # Add the current product
 
    def getProduct(self, k: int) -> int:
        if self.last_zero_index >= len(self.products) - k:
            return 0   # Return 0 if a zero is included
        return self.products[-1] // self.products[-(k + 1)]  # Calculate the product of the last k elements

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)