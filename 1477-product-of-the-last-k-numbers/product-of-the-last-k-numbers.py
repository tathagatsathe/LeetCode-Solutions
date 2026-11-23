class ProductOfNumbers:

    def __init__(self):
        self.products = []
        self.lastZeroIdx = None

    def add(self, num: int) -> None:
        if num == 0:
            self.lastZeroIdx = len(self.products)
        elif len(self.products) == 0:
            self.products.append(num)
        else:
            self.products.append(self.products[-1]*num)

    def getProduct(self, k: int) -> int:
        if self.lastZeroIdx != None and self.lastZeroIdx > len(self.products) - k:
            return 0

        if len(self.products) == k:
            return self.products[-1]

        return self.products[-1]//self.products[-k-1]

