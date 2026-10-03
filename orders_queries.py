import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

print("Customer orders (joined):")
cur.execute("""
SELECT c.name, o.amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_id, o.order_id
""")
for row in cur.fetchall():
    print(row)

print("\nTotal spend per customer:")
cur.execute("""
SELECT c.name, SUM(o.amount) AS total_spent
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
""")
for row in cur.fetchall():
    print(row)

conn.close()
