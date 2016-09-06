import json

def result():
    with open("products.txt") as products, open("listings.txt") as listings, open("results.txt","w") as results:

        products = [json.loads(product) for product in products.readlines()]
        listings = [(json.loads(listing),str(listing)) for listing in listings.readlines()]

        for product in products:

            matches = list()

            for listing in listings:
                if (product["manufacturer"] == listing[0]["manufacturer"]) and ("family" in product and product["family"] in listing[0]["title"]) and (product["model"] in listing[0]["title"]):
                    matches.append(listing[1])


            results.write("%s\n" % json.JSONEncoder().encode({"product_name":product["product_name"], "listings":matches}))

if __name__ == "__main__":
    result()
