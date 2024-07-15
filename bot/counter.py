import json
import os

COUNTER_FILE = 'counter.json'

def load_counter():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {'count': 0}
    return data

def save_counter(data):
    with open(COUNTER_FILE, 'w') as f:
        json.dump(data, f)

def increment_counter():
    data = load_counter()
    data['count'] += 1
    save_counter(data)

def get_counter():
    data = load_counter()
    return data['count']
