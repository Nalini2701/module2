import argparse
import csv
from utils import knapsack, calculate_risk, plot_frontier

def read_assets(csv_file):
    assets = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            assets.append({
                'Ticker': row['Ticker'],
                'ExpectedReturn': float(row['ExpectedReturn(%)']),
                'RiskScore': int(row['RiskScore(0-100)']),
                'Price': int(row['Price'])
            })
    return assets

def main():
    parser = argparse.ArgumentParser(description='Portfolio Optimizer')
    parser.add_argument('--capital', type=int, required=True, help='Total capital to invest')
    parser.add_argument('--risk', type=int, required=True, help='Maximum acceptable risk score')
    parser.add_argument('--csv', type=str, required=True, help='Path to assets CSV file')
    parser.add_argument('--plot', action='store_true', help='Plot efficient frontier')
    args = parser.parse_args()

    assets = read_assets(args.csv)
    prices = [asset['Price'] for asset in assets]
    returns = [asset['ExpectedReturn'] for asset in assets]
    capacity = args.capital

    dp = knapsack(prices, returns, capacity)
    selected_assets = []  # Implement backtracking to find selected assets
    total_cost = sum(asset['Price'] for asset in selected_assets)
    total_return = sum(asset['ExpectedReturn'] for asset in selected_assets)
    total_risk = calculate_risk(selected_assets)

    print("Selected assets:")
    for asset in selected_assets:
        print(asset['Ticker'])
    print(f"Total Cost : ₹{total_cost}")
    print(f"Expected Return : {total_return} %")
    print(f"Risk Score : {total_risk}")

    if args.plot:
        plot_frontier(assets, capacity)

if __name__ == '__main__':
    main()
