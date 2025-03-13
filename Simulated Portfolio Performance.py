import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def generate_sample_data(num_days=252):
    """
    Generate simulated daily return data for a portfolio.
    """
    dates = pd.date_range(end=datetime.today(), periods=num_days, freq='B')  # Business days
    returns = np.random.normal(0.0005, 0.01, num_days)  # Simulated daily returns
    df = pd.DataFrame(data={'Return': returns}, index=dates)
    df['Cumulative'] = (1 + df['Return']).cumprod() - 1
    return df

def calculate_performance_metrics(df):
    """
    Calculate key performance metrics.
    """
    cumulative_return = df['Cumulative'].iloc[-1]
    annual_volatility = df['Return'].std() * np.sqrt(252)
    sharpe_ratio = (df['Return'].mean() * 252) / (df['Return'].std() * np.sqrt(252))
    
    metrics = {
        'Cumulative Return': cumulative_return,
        'Annual Volatility': annual_volatility,
        'Sharpe Ratio': sharpe_ratio
    }
    return metrics

def plot_performance(df):
    """
    Generate and display a performance chart interactively.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Cumulative'], label='Cumulative Return')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.title('Portfolio Performance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    print("Generating sample performance data...")
    df = generate_sample_data(252)
    
    print("Calculating performance metrics...")
    metrics = calculate_performance_metrics(df)
    
    print("Performance metrics:")
    for key, value in metrics.items():
        if key == 'Sharpe Ratio':
            print(f"  {key}: {value:.2f}")
        else:
            print(f"  {key}: {value:.2%}")
    
    print("Displaying performance chart...")
    plot_performance(df)

if __name__ == '__main__':
    main()

