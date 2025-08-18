import pandas as pd
import random
from datetime import datetime, timedelta

def generate_mock_orders(num_orders12, users12_df, products12_df):
    """
    Generates a mock orders dataset.

    Args:
        num_orders (int): The number of orders to generate.
        users_df (pd.DataFrame): The DataFrame of scraped users.
        products_df (pd.DataFrame): The DataFrame of scraped products.

    Returns:
        pd.DataFrame: The generated orders DataFrame.
    """
    
    # Define a list of cities from your project description
    cities = ['Nairobi', 'Mombasa', 'Kisumu', 'Eldoret', 'Nakuru']

    # Get a list of IDs from your existing datasets
    user_ids = users12_df['user_id'].tolist()
    product_ids = products12_df['product_id'].tolist()

    orders_list = []
    start_date = datetime(2025, 1, 1)

    for i in range(1, num_orders12 + 1):
        order = {
            'order_id': i,
            'user_id': random.choice(user_ids),
            'product_id': random.choice(product_ids),
            'city': random.choice(cities),
            'order_date': (start_date + timedelta(days=random.randint(1, 100))).strftime('%Y-%m-%d'),
            'delivery_time_minutes': random.randint(30, 240),  # Simulate delivery time
            'is_cancelled': random.choice([0, 1])  # 0 for no, 1 for yes
        }
        orders_list.append(order)

    return pd.DataFrame(orders_list)

# Load your scraped data (assuming you have 'user_id' and 'product_id' columns)
try:
    users_df = pd.read_csv('users12.csv')
    products_df = pd.read_csv('products12.csv')
except FileNotFoundError:
    # If the files don't exist, create mock data for them
    users_df = pd.DataFrame({'user_id': range(1, 201)})
    products_df = pd.DataFrame({'product_id': range(1, 15)})

# Generate 200 mock orders
orders_df = generate_mock_orders(200, users_df, products_df)

# Save the new DataFrame to a CSV file
orders_df.to_csv('orders12.csv', index=False)

print("orders12.csv has been successfully generated!")
print(orders_df.head())

