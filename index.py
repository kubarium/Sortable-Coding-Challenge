import json

def result():


    with open("products.txt") as products, open("listings.txt") as listings:

        results = {}

        products = [json.loads(product) for product in products.readlines()]
        listings = [json.loads(listing) for listing in listings.readlines()]

        for product in products:
            print(product["product_name"])

        print(count("family", products))
        print(count("manufacturer", products))
        print(count("model", products))



def count(key, products):
    occurrence = 0
    for product in products:
        if key in product:
            occurrence+=1
    return occurrence

if __name__ == "__main__":
    result()