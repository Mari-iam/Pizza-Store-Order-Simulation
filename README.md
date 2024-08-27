# Pizza-Store-Order-Simulation
## Overview
This project simulates the process of receiving pizza orders as a store owner. It generates fake customer and order data using the Faker library and sends these orders to a Kafka topic. The orders are then loaded into Aiven, a managed cloud service, for further processing or storage.
## Project Structure
* main.py: main.py: The main script that integrates the order generation and Kafka producer to send data to Kafka.
* fakeData.py: Responsible for generating fake customer and pizza order details.
* pizzaproducer.py: Contains the PizzaProvider class, which generates specific pizza-related data such as pizza names and toppings.
## Requirements
* Python 3.x
* Faker library
* Kafka and Aiven integration
## Usage
### 1-Run the Simulation:
### python main.py
This script will:
* Generate fake customer details, pizza orders, and optional toppings.
* Send these orders to a Kafka topic.
* Use Aiven to load and manage these messages.
## Kafka and Aiven Integration
* Kafka: The project uses Kafka to simulate a real-time messaging system where each pizza order is treated as a message sent to a topic.
* Aiven: Aiven’s managed Kafka service is utilized to ensure that the messages are securely stored and processed. Aiven provides a scalable and highly available Kafka environment, making it ideal for this simulation.


https://github.com/user-attachments/assets/9d18fdaf-ab69-4f32-9c84-e3c472cc7c98

