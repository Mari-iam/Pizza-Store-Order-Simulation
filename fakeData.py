from faker import Faker
from pizzaproducer import PizzaProvider

fake = Faker()

fake.add_provider(PizzaProvider)

for i in range(0, 10):
    customer_id = fake.customer_id()
    customer_name = fake.customer_name()
    customer_phone = fake.customer_phone()
    customer_address = fake.customer_address()
    pizza_ordered = fake.pizza_name()
    toppings = fake.pizza_toppings()
    order_datetime = fake.order_datetime()

    # Print output in the desired format
    print(f"Customer ID: {customer_id}")
    print(f"Customer Name: {customer_name}")
    print(f"Phone: {customer_phone}")
    print(f"Address: {customer_address}")
    print(f"Pizza Ordered: {pizza_ordered}")
    print(f"Toppings: {', '.join(toppings) if toppings else 'No extra toppings'}")
    print(f"Order Date & Time: {order_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

