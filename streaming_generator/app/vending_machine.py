import random
from typing import Dict, List
from enum import Enum
import time 
random.seed()




""""
    Machine class, simulate the Machine output
    Paramenter:
        - Product Enum Class
        - Capacity of each product on the machine
        id: int = 0, coordinates: List[float] = [0.0,0.0]
        inital_storage: int = 100
"""

class Machine:

    def __init__(self, products: Enum, inital_storage: int = 100) -> None:
        # Read the Product Enum Name and Value
        self._products = [str(product.name) for product in products]
        self._products_weights = [product.value for product  in products]

        # StartUP the Machine internal 
        self._storage = dict([(str(product.name),inital_storage) for product in products])
        self._capacity = inital_storage
        self.refil_flag = False
        self.stopped_flag = True

        # Content-Describition
        self.id = random.randint(0, 89271)
        self.lat = random.uniform(-27.59295,-27.59325) # Coordinates in geojson = [lon , lat] , maps = [lat, lon]
        self.lon = random.uniform(-48.51350,-48.51871)
        self.location = {"type": "Point", "coordinates": [self.lon, self.lat]}
        self.city = 'Florianopolis'
        self.country = 'Brasil'
        self.state = 'Santa Catarina'
        

    # Private get method return the storage
    def _get_storage(self):
        return self._storage

    # Refil a product on the machine
    def _set_product(self, product: str, quantity: int):
        if product in self._products:
            refil_number = self._capacity if quantity > self._capacity else quantity
            self._storage[product] = refil_number

    # Random choice for any possible product 
    def get_product(self) -> str:
        product = random.choices(self._products, weights = self._products_weights, k = 1)[0]
        if self._storage[product] >= 1:
            self._storage[product] = self._storage[product] - 1
            return product

        return None

    # Refil multiples products
    def refil(self, products_refil: Dict[str,int]):
        self.refil_flag = True
        print(f'Refil flag = True, Prodcuts = {products_refil}')
        for product,value in products_refil.items():
            self._set_product(product, value)
        time.sleep(5)
        self.refil_flag = False

    # Implement a function call over the class
    def __call__(self):
        return self._get_storage()


    # This is the string method return the Machine Product probability
    def __str__(self):
        print("Machines Have the products with probability")
        return str([f'Product = {produtct} -> P({round(prob/sum(self._products_weights),3)})' for produtct,prob in zip(self._products, self._products_weights)]).replace('[',' ').replace(']', ' ')



