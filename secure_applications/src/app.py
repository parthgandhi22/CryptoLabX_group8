from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


def get_db():
    db = sqlite3.connect("ecommerce.db")
    db.row_factory = sqlite3.Row
    return db


def init_db():
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT NOT NULL
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            total REAL NOT NULL
        )
    """)

    if db.execute("SELECT COUNT(*) FROM products").fetchone()[0] == 0:
        products = [
            (1, "Laptop", 60000, "Powerful laptop for students"),
            (2, "Headphones", 2000, "Wireless headphones"),
            (3, "Keyboard", 1500, "Mechanical keyboard"),
            (4, "Mouse", 800, "Wireless gaming mouse")
        ]

        db.executemany(
            "INSERT INTO products VALUES (?, ?, ?, ?)",
            products
        )

    db.commit()
    db.close()


@app.route("/")
def products():
    search = request.args.get("search", "")

    db = get_db()

    # INTENTIONAL VULNERABILITY 1: SQL INJECTION
    query = "SELECT * FROM products WHERE name LIKE '%" + search + "%'"

    products = db.execute(query).fetchall()

    db.close()

    return render_template(
        "products.html",
        products=products,
        search=search
    )


@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])

    total = 0

    for item in cart_items:
        total += item["price"]

    return render_template(
        "cart.html",
        cart=cart_items,
        total=total
    )


@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    db = get_db()

    product = db.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    db.close()

    if product:
        cart = session.get("cart", [])

        cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"]
        })

        session["cart"] = cart

    return redirect("/cart")


@app.route("/remove/<int:index>")
def remove_from_cart(index):
    cart = session.get("cart", [])

    if 0 <= index < len(cart):
        cart.pop(index)

    session["cart"] = cart

    return redirect("/cart")


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get("cart", [])

    if not cart:
        return redirect("/cart")

    if request.method == "POST":

        for item in cart:

            # INTENTIONAL VULNERABILITY 2: PRICE MANIPULATION
            price = float(
                request.form.get(
                    f"price_{item['id']}",
                    item["price"]
                )
            )

            quantity = int(
                request.form.get(
                    f"quantity_{item['id']}",
                    1
                )
            )

            total = price * quantity

            db = get_db()

            db.execute(
                """
                INSERT INTO orders
                (product, price, quantity, total)
                VALUES (?, ?, ?, ?)
                """,
                (
                    item["name"],
                    price,
                    quantity,
                    total
                )
            )

            db.commit()
            db.close()

        session["cart"] = []

        return redirect("/orders")

    return render_template(
        "checkout.html",
        cart=cart
    )


@app.route("/orders")
def orders():
    db = get_db()

    orders = db.execute(
        "SELECT * FROM orders ORDER BY id DESC"
    ).fetchall()

    db.close()

    return render_template(
        "orders.html",
        orders=orders
    )


@app.route("/review", methods=["POST"])
def review():

    # INTENTIONAL VULNERABILITY 3: XSS
    review = request.form.get("review", "")

    return f"""
    <html>
    <head>
        <title>Customer Review</title>
    </head>

    <body>

        <h1>Customer Review</h1>

        <p>{review}</p>

        <br>

        <a href="/">Back to Store</a>

    </body>
    </html>
    """


if __name__ == "__main__":
    init_db()

    app.run(
        debug=True
    )