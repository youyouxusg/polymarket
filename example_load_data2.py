# example_load_data2.py
import pmxt

api = pmxt.Exchange(exchange_name='Polymarket')

# 1. Search for the broad Event
events = api.fetch_events(query='Who will Trump nominate as Fed Chair?')
fed_event = events[0]

# 2. Find the specific Market within that event
warsh = fed_event.markets.match('Kevin Warsh')

print(f"Price: {warsh.yes.price}")