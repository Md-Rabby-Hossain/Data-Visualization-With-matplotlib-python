import pandas as pd
import matplotlib.pyplot as plt

daily_data = pd.read_csv('full_year_sales_data.csv')

#To convert the 'Date' column to datetime format
daily_data['Date'] = pd.to_datetime(daily_data['Date'], format='%m/%d/%Y')

#To group by month and sum the sales
daily_data['Month'] = daily_data['Date'].dt.to_period('M')                                                # Extract month from the date
monthly_sales = daily_data.groupby('Month')['Sales (Units)'].sum().reset_index()

plt.figure(figsize=(10, 8)) 
bars = plt.barh(monthly_sales['Month'].astype(str), monthly_sales['Sales (Units)'], color='darkgreen')

# Add sales numbers at the end of each bar
for bar in bars:
    width = bar.get_width()                                                                               # Get the length of the bar
    plt.text(width,                                                                                       # x-position of the text (end of the bar)
             bar.get_y() + bar.get_height() / 2,                                                          # y-position of the text (middle of the bar)
             f'{int(width)}',                                                                             # Text to display (sales number)
             va='center',                                                                                 # Vertical alignment
             ha='left',                                                                                   # Horizontal alignment
             fontsize=10)

plt.xlabel('Total Sales (Units)')
plt.ylabel('Month')
plt.title('Monthly Sales for 2024')
plt.tight_layout()                                                                                        # Adjust layout to prevent overlapping
plt.show()
