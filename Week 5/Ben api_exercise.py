from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")

# After a request is made, add a header called "Access-Control-Allow-Origin" to the response.
# This will tell the browser that the API can supply data to any URL.

@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

product = [
            {
            "id": 1,
            "name": "Tea",
            "price": 1.2,
            "imageUrl":
            "https://i.guim.co.uk/img/media/f94ed0f2082748d2fad4fcab457fd5bc965ea385/0_0_1600_960/master/1600.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=d9bef5b4c4a1d5f22b2cc336d189f90a"
            },
            {
            "id": 2,
            "name": "Coffee",
            "price": 3.5,
            "imageUrl":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHm0-W876ppWBpCak_UzC9eRz8X5CeI1KPYw&usqp=CAU"
            }
        ]

@app.route("/product", methods=["GET"])
def products():

    return json.dumps(product)

@app.route("/product/<int:product_id>/ingredients", methods=["GET", "POST"])
def ingredients(product_id):
    ingredients = [
        [{"name": "Water", "content": 95, "isCommonAllergen": False}, {"name": "Tea", "content": 5, "isCommonAllergen": True}],
        [{"name": "Water", "content": 90, "isCommonAllergen": False} , {"name": "Coffee", "content": 10, "isCommonAllergen": False}]
    ]
    product_ingredients = ingredients[product_id - 1]
    return json.dumps(product_ingredients)

@app.route("/order", methods=["POST"])
def add_order():
    request_body = json.loads(request.data)
    total_price = 0
    for item in request_body:
        for prod in product:
            quantity = float(item["quantity"])
            product_id = int(item["productId"])
            if int(prod["id"]) == product_id:
                price = prod["price"]
                total_price += quantity * price
    order = {"orderId": 123, "totalPrice": total_price}
    return json.dumps(order)