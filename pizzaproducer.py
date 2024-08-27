import random
from datetime import datetime, timedelta
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def pizza_name(self):
        validPizzaNames= ['Margherita',
                        'Pepperoni',
                        'Hawaiian',
                        'BBQ Chicken',
                        'Veggie Delight',
                        'Meat Lovers',
                        'Four Cheese',
                        'Supreme'
                        ]
        return random.choice(validPizzaNames)

    def pizza_toppings(self):
        validToppings = [
            'Extra Cheese',
            'Mushrooms',
            'Onions',
            'Pepperoni',
            'Sausage',
            'Bacon',
            'Black Olives',
            'Green Peppers',
            'Pineapple',
            'Spinach'
        ]
        # Randomly select some toppings
        return random.sample(validToppings, k=random.randint(0, 4))

    def customer_name(self):
        return self.generator.name()

    def customer_phone(self):
        return self.generator.phone_number()

    def customer_address(self):
        return self.generator.address()
    
    def customer_id(self):
        return self.generator.uuid4()
    
    def order_datetime(self):
        # Generate a random date and time within the last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        return self.generator.date_time_between(start_date=start_date, end_date=end_date)
    
