import pandas as pd
import matplotlib.pyplot as plt

daily_data = pd.read_csv('full_year_sales_data.csv')

# Convert the 'Date' column to datetime format
daily_data['Date'] = pd.to_datetime(daily_data['Date'], format='%m/%d/%Y')

# Group by month and sum the sales
daily_data['Month'] = daily_data['Date'].dt.to_period('M')                                            # Extract month from the date
monthly_sales = daily_data.groupby('Month')['Sales (Units)'].sum().reset_index()

plt.figure(figsize=(10, 8)) 
bars = plt.bar(monthly_sales['Month'].astype(str), monthly_sales['Sales (Units)'], color='skyblue')

# Add sales numbers at the top of each bar
for bar in bars:
    height = bar.get_height()                                                                         # Get the height of the bar
    plt.text(bar.get_x() + bar.get_width() / 2,                                                       # x-position (center of the bar)
             height,                                                                                  # y-position (top of the bar)
             f'{int(height)}',                                                                        # Text to display (sales number)
             va='bottom',                                                                             # Vertical alignment (above the bar)
             ha='center',                                                                             # Horizontal alignment (center of the bar)
             fontsize=10)                                                                             # Font size of the text

plt.xlabel('Month')
plt.ylabel('Total Sales (Units)')
plt.title('Monthly Sales for 2024')
plt.xticks(rotation=45)
plt.tight_layout()                                                                                    # Adjust layout to prevent overlapping
plt.show()
