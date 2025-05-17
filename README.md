Portfolio Optimizer (0/1 Knapsack):::


A command-line tool to optimize investment portfolios using the 0/1 Knapsack algorithm, considering capital and risk constraints. It also visualizes the efficient frontier to aid in decision-making.



 Features:::

 
✅ Dynamic Programming-based 0/1 Knapsack: Selects the optimal subset of assets to maximize expected returns within the given capital.

⚖️ Risk Filtering: Applies a risk threshold to ensure the portfolio's total risk score does not exceed the specified limit.

📈 Efficient Frontier Visualization: Plots risk vs. return to illustrate optimal trade-offs.

🧪 Unit Testing: Validates the optimizer's behavior with test cases.

💻 Command-Line Interface: Easy-to-use CLI for input parameters and options.


Arguments::


--capital: Total investment capital (e.g., 75000)

--risk: Maximum acceptable risk score (0–100)

--csv: Path to the assets CSV file (e.g., assets.csv)

--plot: Optional flag to generate and save the efficient frontier plot as frontier.png

Algorithm Overview::


0/1 Knapsack via Dynamic Programming

Maximizes total expected return without exceeding the capital.

DP table size: (n+1) × (capital+1)

Time complexity: O(n × capital)

⚖️ Risk Filtering (Greedy Approach)


If the total risk exceeds the specified threshold::


Iteratively remove the asset with the lowest return until the total risk is within the limit.


📈 Efficient Frontier::


Runs multiple optimizations by sweeping risk tolerance from 0 to 100 in steps of 5.

Plots return vs. risk to visualize optimal trade-offs.

Tests include::


Asset selection optimization

Risk threshold filtering

Cost and return accuracy

 Future Improvements::

 
Support for fractional (continuous) knapsack

Interactive plots using Plotly or Dash

Integration with live market APIs for real-time data

Web-based UI using Flask or Django
