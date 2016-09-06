import json
from collections import OrderedDict

def result():
    with open("products.txt") as products, open("listings.txt", encoding="utf-8") as listings, open("results.txt","w") as results:
        '''
        for listing in listings:
            if "Digital IXUS 310 HS - 1/2.3 ?MOS" in listing:
                results.write("%s\n" % listing)
        exit()
        '''
        products = [json.loads(product) for product in products.readlines()]
        #listings = [(json.loads(listing)["title"],json.loads(listing)["manufacturer"], json.loads(listing, object_pairs_hook=collections.OrderedDict)) for listing in listings.readlines()]
        listings = [json.loads(listing, object_pairs_hook=OrderedDict) for listing in listings.readlines()]

        for product in products:

            matches = list()

            for listing in listings:
                if (product["manufacturer"] == listing["manufacturer"]) and ("family" in product and product["family"] in listing["title"]) and (product["model"] in listing["title"]):
                #if (product["manufacturer"] in listing[0] or product["manufacturer"] == listing[1]) and ("family" in product and product["family"] in listing[0]) and (product["model"] in listing[0]):
                    matches.append(listing)

            #json.dump(str({"product_name":product["product_name"], "listings":matches})+"\n", results)

            results.write("%s\n" % json.JSONEncoder(ensure_ascii=False).encode({"product_name":product["product_name"],"listings":matches}))

if __name__ == "__main__":
    result()
