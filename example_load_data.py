# example_load_data.py
import pmxt

def main():
    # Example: fetch Polymarket markets about Bitcoin
    api = pmxt.Polymarket()
    markets = api.fetch_markets(query="Bitcoin price")

    if markets:
        print("Found markets:")
        for m in markets[:3]:  # just show top 3
            print(f"{m.title} - Outcomes: {[o.title for o in m.outcomes]}")
    else:
        print("No markets found")

if __name__ == "__main__":
    main()