import json

def result():
    with open("products.txt") as products, open("listings.txt") as listings, open("results.txt","w") as results:

        products = [json.loads(product) for product in products.readlines()]
        listings = [json.loads(listing) for listing in listings.readlines()]

        for product in products:

            matches = list()

            for listing in listings:
                if (product["manufacturer"] == listing["manufacturer"]) and ("family" in product and product["family"] in listing["title"]) and (product["model"] in listing["title"]):
                    matches.append(listing)

            results.write("%s\n" % str({"product_name":product["product_name"], "listings":matches}))

if __name__ == "__main__":
    result()
