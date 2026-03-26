import pandas as pd
from datetime import datetime
import os

def log_order(customer_name, order_details):
    file_name = 'whatsapp_orders.csv'
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the data structure
    new_order = {
        'Timestamp': [timestamp],
        'Customer': [customer_name],
        'Order': [order_details],
        'Status': ['Pending']
    }
    df_new = pd.DataFrame(new_order)

    # If file doesn't exist, create it. If it does, append to it.
    if not os.path.isfile(file_name):
        df_new.to_csv(file_name, index=False)
    else:
        df_new.to_csv(file_name, mode='a', header=False, index=False)
    
    print(f"✅ Order logged for {customer_name}!")

# Simulating an incoming WhatsApp message
if __name__ == "__main__":
    print("--- WhatsApp Order Tracker (Simulation) ---")
    name = input("Enter Customer Name: ")
    item = input("Enter Order Details: ")
    log_order(name, item)