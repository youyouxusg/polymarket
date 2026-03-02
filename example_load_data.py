# example_load_data.py
import pmxt

def main():
    api = pmxt.Polymarket()
    markets = api.fetch_markets(query="Bitcoin price")

    if markets:
        print("Found markets:")
        for m in markets[:3]:  # show top 3
            outcome_labels = [o.label for o in m.outcomes]
            print(f"Outcomes: {outcome_labels}")
    else:
        print("No markets found")

if __name__ == "__main__":
    main()