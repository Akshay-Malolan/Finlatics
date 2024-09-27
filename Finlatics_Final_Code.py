import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the dataset
file_path = "PATH"
data = pd.read_csv(file_path)

'''1. What is the overall trend in user engagement throughout the campaign period?'''

# Group by day and user engagement to see the trend
engagement_trend = data.groupby(['month', 'day', 'user_engagement']).size().unstack(fill_value=0)
# Plotting the trend
engagement_trend.plot(kind='line', figsize=(14, 7), title='Question 1: User Engagement Trend')
plt.xlabel('Day')
plt.ylabel('Number of Engagements')
plt.show()

'''2. How does the size of the ad (banner) impact the number of clicks generated?'''

# Group by banner and sum the clicks
banner_clicks = data.groupby('banner')['clicks'].sum()
# Plotting the banner size vs clicks
banner_clicks.plot(kind='bar', figsize=(14, 7), title='Question 2: Clicks by Banner Size')
plt.xlabel('Banner Size')
plt.ylabel('Total Clicks')
plt.show()

'''3. Which publisher spaces (placements) yielded the highest number of displays and clicks?'''

# Group by placement and sum the displays and clicks
placement_performance = data.groupby('placement')[['displays', 'clicks']].sum().sort_values(by='displays', ascending=False)
# Display the top placements
print(f'Question 3:\n {placement_performance.head(10)}')

'''4. Is there a correlation between the cost of serving ads and the revenue generated from clicks?'''

correlation = data[['cost', 'revenue']].corr().iloc[0, 1]
print(f'Question 4:\n {correlation}')

'''5. What is the average revenue generated per click for Company X during the campaign period?'''

avg_revenue_per_click = data['revenue'].sum() / data['clicks'].sum()
print(f'Question 5:\n {avg_revenue_per_click}')

'''6. Which Campaigns Had the Highest Post-Click Conversion Rates?'''

data['day'] = pd.to_datetime(data['day'], format='%d')
# Calculate conversion rate, handling cases where clicks are zero
data['conversion_rate'] = data['post_click_conversions'] / data['clicks'].replace(0, pd.NA)
campaign_conversion_rates = data.groupby('campaign_number')['conversion_rate'].mean().sort_values(ascending=False)
# Replace infinite values and NaNs with 0 for better interpretation
campaign_conversion_rates = campaign_conversion_rates.replace([pd.NA, float('inf')], 0)
# Display the top campaigns by conversion rate
print(f'Question 6:\n {campaign_conversion_rates.head(10)}')

'''7. Are There Specific Trends or Patterns in Post-Click Sales Amounts Over Time?'''

sales_trend = data.groupby(['month', 'day'])['post_click_sales_amount'].sum()
# Plotting the sales trend
sales_trend.plot(kind='line', figsize=(14, 7), title='Question 7: Post-Click Sales Amount Trend')
plt.xlabel('Day')
plt.ylabel('Post-Click Sales Amount')
plt.show()

'''8. How Does the Level of User Engagement Vary Across Different Banner Sizes?'''

engagement_by_banner = data.groupby(['banner', 'user_engagement']).size().unstack(fill_value=0)
# Plotting the engagement levels across banner sizes
engagement_by_banner.plot(kind='bar', stacked=True, figsize=(14, 7), title='Question 8: User Engagement Levels Across Banner Sizes')
plt.xlabel('Banner Size')
plt.ylabel('Number of Engagements')
plt.show()

'''9. Which Placement Types Result in the Highest Post-Click Conversion Rates?'''

data['day'] = pd.to_datetime(data['day'], format='%d')
# Calculate conversion rate, handling cases where clicks are zero
data['conversion_rate'] = data['post_click_conversions'] / data['clicks'].replace(0, pd.NA)
# Group by placement and calculate the mean conversion rate
placement_conversion_rates = data.groupby('placement')['conversion_rate'].mean().sort_values(ascending=False)
# Replace infinite values and NaNs with 0 for better interpretation
placement_conversion_rates = placement_conversion_rates.replace([pd.NA, float('inf')], 0)
# Display the top placements by conversion rate
print(f'Question 9:\n {placement_conversion_rates.head(10)}')

'''10. Can We Identify Seasonal Patterns or Fluctuations in Displays and Clicks?'''

# Group by month and day to see the seasonal patterns
seasonal_displays_clicks = data.groupby(['month', 'day'])[['displays', 'clicks']].sum()
# Plotting the displays and clicks trend
seasonal_displays_clicks.plot(kind='line', figsize=(14, 7), title='Question 10: Displays and Clicks Trend')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

'''11. Is There a Correlation Between User Engagement Levels and Revenue Generated?'''

# Group by user engagement and sum the revenue
engagement_revenue = data.groupby('user_engagement')['revenue'].sum()
# Plotting the revenue by user engagement levels
engagement_revenue.plot(kind='bar', figsize=(14, 7), title='Question 11: Revenue by User Engagement Levels')
plt.xlabel('User Engagement Level')
plt.ylabel('Total Revenue')
plt.show()
# Calculate the correlation between engagement and revenue
engagement_revenue_corr = data.groupby('user_engagement')['revenue'].mean().corr(data.groupby('user_engagement')['user_engagement'].count())
print(f'Question 11:\n {engagement_revenue_corr}')

'''12. Are There Any Outliers in Terms of Cost, Clicks, or Revenue That Warrant Further Investigation?'''

# Plotting boxplots to identify outliers in cost, clicks, and revenue
fig, axes = plt.subplots(1, 3, figsize=(21, 7))
data.boxplot(column='cost', ax=axes[0])
axes[0].set_title('Question 12.1: Cost Outliers')
data.boxplot(column='clicks', ax=axes[1])
axes[1].set_title('Question 12.2: Clicks Outliers')
data.boxplot(column='revenue', ax=axes[2])
axes[2].set_title('Question 12.3: Revenue Outliers')
plt.show()

'''13. How does the effectiveness of campaigns vary based on the size of the ad and placement type?'''

# Convert 'day' column to datetime
data['day'] = pd.to_datetime(data['day'], format='%d')
# Group by banner and placement, then calculate the sum of clicks and post_click_conversions
campaign_effectiveness = data.groupby(['banner', 'placement'])[['clicks', 'post_click_conversions']].sum()
# Calculate the conversion rate, handling cases where clicks are zero
campaign_effectiveness['conversion_rate'] = campaign_effectiveness['post_click_conversions'] / campaign_effectiveness['clicks'].replace(0, pd.NA)
# Replace infinite values and NaNs with 0 for better interpretation
campaign_effectiveness['conversion_rate'] = campaign_effectiveness['conversion_rate'].replace([pd.NA, float('inf')], 0)
# Display the top results
print(f"Question 13:\n {campaign_effectiveness.sort_values(by='conversion_rate', ascending=False).head(10)}")

'''14. Are there any specific campaigns or banner sizes that consistently outperform others in terms of ROI?'''

# Calculate ROI for each campaign, handling cases where cost is zero
data['roi'] = data['revenue'] / data['cost'].replace(0, pd.NA)
# Replace infinite values and NaNs with 0 for better interpretation
data['roi'] = data['roi'].replace([pd.NA, float('inf')], 0)
# Group by campaign_number and banner to get the mean ROI
roi_performance = data.groupby(['campaign_number', 'banner'])['roi'].mean().sort_values(ascending=False)
# Display the top performing campaigns and banner sizes by ROI
print(f'Question 14:\n {roi_performance.head(10)}')

'''15. What is the distribution of post-click conversions across different placement types?'''

# Group by placement and sum the post-click conversions
placement_post_click_conversions = data.groupby('placement')['post_click_conversions'].sum()
# Plotting the distribution of post-click conversions across placements
placement_post_click_conversions.plot(kind='bar', figsize=(14, 7), title='Question 15: Post-Click Conversions Across Placement Types')
plt.xlabel('Placement')
plt.ylabel('Total Post-Click Conversions')
plt.show()

'''16. Are there any noticeable differences in user engagement levels between weekdays and weekends?'''

# If the 'month' column has full month names, map them to their numerical values
month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}
data['month'] = data['month'].map(month_map)

# Convert 'day' column to integer
data['day'] = data['day'].astype('int64').astype(int)

# Create a 'date' column
data['date'] = pd.to_datetime(data.apply(lambda row: f"2020-{row['month']:02d}-{row['day']:02d}", axis=1), format='%Y-%m-%d', errors='coerce')

# Check for any parsing errors
if data['date'].isnull().any():
    print("There are parsing errors in the date column.")
    print(data[data['date'].isnull()])

# Create a 'day_of_week' column to identify weekdays and weekends
data['day_of_week'] = data['date'].dt.dayofweek

# Map day_of_week to 'Weekday' or 'Weekend'
data['day_type'] = data['day_of_week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

# Group by 'day_type' and calculate the average user engagement levels
engagement_summary = data.groupby('day_type')['user_engagement'].value_counts(normalize=True).unstack().fillna(0)

# Display the summary
print(engagement_summary)
'''17. How does the cost per click (CPC) vary across different campaigns and banner sizes?'''

# Filter out rows where clicks are zero
data_filtered_clicks = data[data['clicks'] > 0]

# Calculate cost per click (CPC)
data_filtered_clicks['cpc'] = data_filtered_clicks['cost'] / data_filtered_clicks['clicks']

# Group by campaign_number and banner to get the mean CPC
cpc_performance = data_filtered_clicks.groupby(['campaign_number', 'banner'])['cpc'].mean().sort_values(ascending=False)

# Display the CPC across campaigns and banner sizes
print(f'Question 17: {cpc_performance.head(10)}')

'''18. Are there any campaigns or placements that are particularly cost-effective in terms of generating post-click conversions?'''

# Filter out rows where post_click_conversions are zero
data_filtered_conversions = data[data['post_click_conversions'] > 0]
# Calculate cost per conversion (CPC)
data_filtered_conversions['cost_per_conversion'] = data_filtered_conversions['cost'] / data_filtered_conversions['post_click_conversions']
# Group by campaign_number and placement to get the mean cost per conversion
cost_per_conversion_performance = data_filtered_conversions.groupby(['campaign_number', 'placement'])['cost_per_conversion'].mean().sort_values(ascending=True)
# Display the most cost-effective campaigns and placements
print(f'Question 18: {cost_per_conversion_performance.head(10)}')

'''19. Can we identify any trends or patterns in post-click conversion rates based on the day of the week?'''

month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}
# Map the 'month' column
data['month'] = data['month'].map(month_map)
# Handle NaN values in 'month' and 'day' columns
data['month'] = data['month'].fillna(1)  # Default to January if month is NaN
data['day'] = data['day'].fillna(15)     # Default to 15 if day is NaN
# Fix the 'day' column: replace invalid negative values with a median day (15)
data['day'] = data['day'].apply(lambda x: 15 if x < 1 or x > 31 else x).astype(int)
# Create a 'date' column
data['date'] = data.apply(lambda row: datetime(2020, int(row['month']), int(row['day'])), axis=1)
# Check for any parsing errors
parsing_errors = data[data['date'].isnull()]
if not parsing_errors.empty:
    print("There are parsing errors in the date column.")
    print(parsing_errors)
# Create a 'day_of_week' column to identify weekdays and weekends
data['day_of_week'] = data['date'].dt.dayofweek
# Map day_of_week to 'Weekday' or 'Weekend'
data['day_type'] = data['day_of_week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
# Calculate the average post-click conversion rate for each day type
conversion_rate_summary = data.groupby('day_type')['post_click_conversions'].mean()
# Display the summary for weekdays and weekends separately
print("Average post-click conversion rates:")
for day_type, conversion_rate in conversion_rate_summary.items():
    print(f"{day_type}: {conversion_rate}")
# Check if both Weekday and Weekend are present in the summary
if 'Weekday' not in conversion_rate_summary.index:
    print("No data available for Weekdays.")
if 'Weekend' not in conversion_rate_summary.index:
    print("No data available for Weekends.")

'''20. How does the effectiveness of campaigns vary throughout different user engagement types in terms of post-click conversions?'''

# Group by user engagement and calculate the sum of post-click conversions
engagement_effectiveness = data.groupby('user_engagement')['post_click_conversions'].sum()
# Plotting the post-click conversions across user engagement types
engagement_effectiveness.plot(kind='bar', figsize=(14, 7), title='Question 20: Post-Click Conversions by User Engagement Types')
plt.xlabel('User Engagement Type')
plt.ylabel('Total Post-Click Conversions')
plt.show()
