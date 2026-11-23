class ProductOfNumbers:

    def __init__(self):
        self.stream = []

    def add(self, num: int) -> None:
        self.stream.append(num)

    def getProduct(self, k: int) -> int:
        
        product = 1
        for c in self.stream[-k:]:
            product*=c

        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)