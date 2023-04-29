python
import time
import random
import pandas as pd

# Define function to generate random data
def generate_data():
    timestamp = int(time.time())
    value = random.uniform(0, 1)
    return (timestamp, value)

# Define function to continuously stream data and save to CSV file
def stream_data():
    while True:
        # Generate random data
        data = generate_data()
        # Append data to CSV file
        with open('data/streaming_data.csv', 'a') as f:
            f.write(f"{data[0]},{data[1]}\n")
        # Sleep for one second before generating more data
        time.sleep(1)

# Call the stream_data function to begin streaming data
if __name__ == '__main__':
    stream_data()
