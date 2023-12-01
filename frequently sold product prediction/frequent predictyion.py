import pandas as pd
import matplotlib.pyplot as plt

# Sample data generation (replace this with your actual dataset)
data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'ProductA_Sales': [30, 45, 60, 80, 75, 90, 100, 120, 110, 95, 85, 70],
    'ProductB_Sales': [20, 25, 40, 55, 60, 75, 80, 90, 100, 110, 95, 80],
}

# Ensure all arrays have the same length
length = min(len(data['Date']), len(data['ProductA_Sales']), len(data['ProductB_Sales']))
data['Date'] = data['Date'][:length]
data['ProductA_Sales'] = data['ProductA_Sales'][:length]
data['ProductB_Sales'] = data['ProductB_Sales'][:length]

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

# Plotting sales for Product A
plt.plot(df['Date'], df['ProductA_Sales'], label='Product A', marker='o')

# Plotting sales for Product B
plt.plot(df['Date'], df['ProductB_Sales'], label='Product B', marker='o')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Frequently Sold Product Prediction')
plt.legend()

# Show the plot
plt.show()


