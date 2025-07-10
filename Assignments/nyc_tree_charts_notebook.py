# NYC Tree Data Extraction and Charting - Notebook Cells
# Copy and paste these cells into your Jupyter notebook

# Cell 1: Extract and Explore Data
"""
# Extract the specific columns we want
print("Extracting key columns...")
tree_data = pluto[['zipcode', 'zip_city', 'tree_dbh', 'status']].copy()

# Display basic info about our extracted data
print(f"Dataset Shape: {tree_data.shape}")
print(f"Columns: {list(tree_data.columns)}")
print("\nFirst 5 rows:")
print(tree_data.head())

# Check for missing values
print("\nMissing Values:")
print(tree_data.isnull().sum())

# Basic statistics
print("\nTree DBH Statistics:")
print(tree_data['tree_dbh'].describe())

print("\nStatus Distribution:")
print(tree_data['status'].value_counts())

print(f"\nNumber of unique zip codes: {tree_data['zipcode'].nunique()}")
print(f"Number of unique cities: {tree_data['zip_city'].nunique()}")
"""

# Cell 2: Main Charts Dashboard
"""
# Create a comprehensive dashboard of charts
import seaborn as sns
import numpy as np

# Set style for better-looking charts
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Chart 1: Tree Status Distribution (Pie Chart)
status_counts = tree_data['status'].value_counts()
colors = ['#2E8B57', '#DC143C', '#8B4513', '#696969', '#FFD700']
axes[0, 0].pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', 
               colors=colors, startangle=90, explode=(0.05, 0, 0, 0, 0))
axes[0, 0].set_title('Tree Status Distribution', fontweight='bold', fontsize=12)

# Chart 2: Tree DBH Distribution (Histogram)
axes[0, 1].hist(tree_data['tree_dbh'].dropna(), bins=30, alpha=0.7, color='green', 
                edgecolor='black', linewidth=0.5)
axes[0, 1].set_xlabel('Tree DBH (inches)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Tree Diameter Distribution', fontweight='bold', fontsize=12)
axes[0, 1].grid(True, alpha=0.3)

# Chart 3: Top 10 Cities by Tree Count (Bar Chart)
top_cities = tree_data['zip_city'].value_counts().head(10)
bars = axes[0, 2].barh(range(len(top_cities)), top_cities.values, color='skyblue')
axes[0, 2].set_yticks(range(len(top_cities)))
axes[0, 2].set_yticklabels(top_cities.index)
axes[0, 2].set_xlabel('Number of Trees')
axes[0, 2].set_title('Top 10 Cities by Tree Count', fontweight='bold', fontsize=12)

# Add value labels on bars
for i, bar in enumerate(bars):
    width = bar.get_width()
    axes[0, 2].text(width + width*0.01, bar.get_y() + bar.get_height()/2, 
                    f'{int(width):,}', ha='left', va='center', fontsize=8)

# Chart 4: Average DBH by City (Top 10) (Bar Chart)
avg_dbh_by_city = tree_data.groupby('zip_city')['tree_dbh'].mean().sort_values(ascending=False).head(10)
bars = axes[1, 0].barh(range(len(avg_dbh_by_city)), avg_dbh_by_city.values, color='lightgreen')
axes[1, 0].set_yticks(range(len(avg_dbh_by_city)))
axes[1, 0].set_yticklabels(avg_dbh_by_city.index)
axes[1, 0].set_xlabel('Average Tree DBH (inches)')
axes[1, 0].set_title('Average Tree DBH by City (Top 10)', fontweight='bold', fontsize=12)

# Add value labels on bars
for i, bar in enumerate(bars):
    width = bar.get_width()
    axes[1, 0].text(width + width*0.01, bar.get_y() + bar.get_height()/2, 
                    f'{width:.1f}', ha='left', va='center', fontsize=8)

# Chart 5: Tree Count by Status (Bar Chart)
bars = axes[1, 1].bar(status_counts.index, status_counts.values, color=colors[:len(status_counts)])
axes[1, 1].set_xlabel('Tree Status')
axes[1, 1].set_ylabel('Number of Trees')
axes[1, 1].set_title('Tree Count by Status', fontweight='bold', fontsize=12)
axes[1, 1].tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'{int(height):,}', ha='center', va='bottom', fontsize=8)

# Chart 6: DBH Box Plot by Status
dbh_data = tree_data[tree_data['tree_dbh'] <= tree_data['tree_dbh'].quantile(0.95)]
sns.boxplot(data=dbh_data, x='status', y='tree_dbh', palette=colors[:len(status_counts)], ax=axes[1, 2])
axes[1, 2].set_xlabel('Tree Status')
axes[1, 2].set_ylabel('Tree DBH (inches)')
axes[1, 2].set_title('Tree DBH Distribution by Status', fontweight='bold', fontsize=12)
axes[1, 2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
"""

# Cell 3: Zip Code Analysis Charts
"""
# Create charts focused on zip code analysis
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Chart 1: Tree Count by Zip Code (Top 15)
top_zips = tree_data['zipcode'].value_counts().head(15)
bars = axes[0, 0].bar(range(len(top_zips)), top_zips.values, color='coral')
axes[0, 0].set_xlabel('Zip Code')
axes[0, 0].set_ylabel('Number of Trees')
axes[0, 0].set_title('Tree Count by Zip Code (Top 15)', fontweight='bold', fontsize=14)
axes[0, 0].set_xticks(range(len(top_zips)))
axes[0, 0].set_xticklabels(top_zips.index, rotation=45)

# Add value labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    axes[0, 0].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'{int(height):,}', ha='center', va='bottom', fontsize=8)

# Chart 2: Average DBH by Zip Code (Top 15)
avg_dbh_by_zip = tree_data.groupby('zipcode')['tree_dbh'].mean().sort_values(ascending=False).head(15)
bars = axes[0, 1].bar(range(len(avg_dbh_by_zip)), avg_dbh_by_zip.values, color='gold')
axes[0, 1].set_xlabel('Zip Code')
axes[0, 1].set_ylabel('Average Tree DBH (inches)')
axes[0, 1].set_title('Average Tree DBH by Zip Code (Top 15)', fontweight='bold', fontsize=14)
axes[0, 1].set_xticks(range(len(avg_dbh_by_zip)))
axes[0, 1].set_xticklabels(avg_dbh_by_zip.index, rotation=45)

# Add value labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=8)

# Chart 3: Status Distribution by Zip Code (Top 10)
status_by_zip = pd.crosstab(tree_data['zipcode'], tree_data['status'])
top_zips_for_status = tree_data['zipcode'].value_counts().head(10).index
status_by_zip_top = status_by_zip.loc[top_zips_for_status]

sns.heatmap(status_by_zip_top, annot=True, fmt='d', cmap='YlOrRd', 
            cbar_kws={'label': 'Number of Trees'}, ax=axes[1, 0])
axes[1, 0].set_title('Tree Status by Zip Code (Top 10)', fontweight='bold', fontsize=14)
axes[1, 0].set_xlabel('Tree Status')
axes[1, 0].set_ylabel('Zip Code')

# Chart 4: DBH Distribution by Zip Code (Top 10)
dbh_by_zip = tree_data[tree_data['zipcode'].isin(top_zips_for_status)]
dbh_filtered = dbh_by_zip[dbh_by_zip['tree_dbh'] <= dbh_by_zip['tree_dbh'].quantile(0.9)]
sns.boxplot(data=dbh_filtered, x='zipcode', y='tree_dbh', ax=axes[1, 1])
axes[1, 1].set_xlabel('Zip Code')
axes[1, 1].set_ylabel('Tree DBH (inches)')
axes[1, 1].set_title('Tree DBH Distribution by Zip Code (Top 10)', fontweight='bold', fontsize=14)
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
"""

# Cell 4: Status Analysis Charts
"""
# Create charts focused on status analysis
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Chart 1: Status Distribution by City (Heatmap - Top 10 cities)
status_by_city = pd.crosstab(tree_data['zip_city'], tree_data['status'])
top_cities = tree_data['zip_city'].value_counts().head(10).index
status_by_city_top = status_by_city.loc[top_cities]

sns.heatmap(status_by_city_top, annot=True, fmt='d', cmap='YlOrRd', 
            cbar_kws={'label': 'Number of Trees'}, ax=axes[0, 0])
axes[0, 0].set_title('Tree Status by City (Top 10)', fontweight='bold', fontsize=14)
axes[0, 0].set_xlabel('Tree Status')
axes[0, 0].set_ylabel('City')

# Chart 2: DBH Distribution by Status (Violin Plot)
dbh_filtered = tree_data[tree_data['tree_dbh'] <= tree_data['tree_dbh'].quantile(0.9)]
sns.violinplot(data=dbh_filtered, x='status', y='tree_dbh', 
               palette=colors[:len(status_counts)], ax=axes[0, 1])
axes[0, 1].set_xlabel('Tree Status')
axes[0, 1].set_ylabel('Tree DBH (inches)')
axes[0, 1].set_title('Tree DBH Distribution by Status', fontweight='bold', fontsize=14)
axes[0, 1].tick_params(axis='x', rotation=45)

# Chart 3: Status Count by Zip Code (Stacked Bar)
status_by_zip_top = status_by_zip.loc[top_zips_for_status]
status_by_zip_top.plot(kind='bar', stacked=True, ax=axes[1, 0], colormap='Set3')
axes[1, 0].set_xlabel('Zip Code')
axes[1, 0].set_ylabel('Number of Trees')
axes[1, 0].set_title('Tree Status by Zip Code (Top 10)', fontweight='bold', fontsize=14)
axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].legend(title='Status', bbox_to_anchor=(1.05, 1), loc='upper left')

# Chart 4: Average DBH by Status
avg_dbh_by_status = tree_data.groupby('status')['tree_dbh'].mean().sort_values(ascending=False)
bars = axes[1, 1].bar(range(len(avg_dbh_by_status)), avg_dbh_by_status.values, 
                      color=colors[:len(avg_dbh_by_status)])
axes[1, 1].set_xlabel('Tree Status')
axes[1, 1].set_ylabel('Average Tree DBH (inches)')
axes[1, 1].set_title('Average Tree DBH by Status', fontweight='bold', fontsize=14)
axes[1, 1].set_xticks(range(len(avg_dbh_by_status)))
axes[1, 1].set_xticklabels(avg_dbh_by_status.index, rotation=45)

# Add value labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
"""

# Cell 5: Summary Statistics
"""
# Create comprehensive summary statistics
print("="*80)
print("SUMMARY STATISTICS BY CITY")
print("="*80)

# Create comprehensive summary
summary_stats = tree_data.groupby('zip_city').agg({
    'tree_dbh': ['count', 'mean', 'std', 'min', 'max'],
    'status': lambda x: x.value_counts().index[0] if len(x) > 0 else 'Unknown'
}).round(2)

# Flatten column names
summary_stats.columns = ['tree_count', 'avg_dbh', 'std_dbh', 'min_dbh', 'max_dbh', 'most_common_status']

# Sort by tree count
summary_stats = summary_stats.sort_values('tree_count', ascending=False)

print(summary_stats.head(15))

# Save summary to CSV
summary_stats.to_csv('nyc_tree_summary_by_city.csv')
print(f"\nSummary saved to 'nyc_tree_summary_by_city.csv'")
"""

# Cell 6: Zip Code Analysis
"""
print("="*80)
print("ZIP CODE ANALYSIS")
print("="*80)

zip_summary = tree_data.groupby('zipcode').agg({
    'tree_dbh': ['count', 'mean', 'std'],
    'status': lambda x: x.value_counts().index[0] if len(x) > 0 else 'Unknown'
}).round(2)

zip_summary.columns = ['tree_count', 'avg_dbh', 'std_dbh', 'most_common_status']
zip_summary = zip_summary.sort_values('tree_count', ascending=False)

print("Top 15 Zip Codes by Tree Count:")
print(zip_summary.head(15))

# Save zip code summary
zip_summary.to_csv('nyc_tree_summary_by_zipcode.csv')
print(f"\nZip code summary saved to 'nyc_tree_summary_by_zipcode.csv'")
"""

# Cell 7: Status Analysis
"""
print("="*80)
print("STATUS ANALYSIS")
print("="*80)

status_summary = tree_data.groupby('status').agg({
    'tree_dbh': ['count', 'mean', 'std', 'min', 'max'],
    'zip_city': 'nunique'
}).round(2)

status_summary.columns = ['tree_count', 'avg_dbh', 'std_dbh', 'min_dbh', 'max_dbh', 'cities_present']
print(status_summary)

# Save status summary
status_summary.to_csv('nyc_tree_summary_by_status.csv')
print(f"\nStatus summary saved to 'nyc_tree_summary_by_status.csv'")
"""

# Cell 8: Interactive Filtering
"""
# Interactive filtering - you can modify these values
min_dbh = 10  # minimum tree diameter
max_dbh = 50  # maximum tree diameter
selected_status = 'Alive'  # or 'Dead', 'Stump', etc.
selected_city = 'Brooklyn'  # or any other city

# Filter the data
filtered_data = tree_data[
    (tree_data['tree_dbh'] >= min_dbh) & 
    (tree_data['tree_dbh'] <= max_dbh) & 
    (tree_data['status'] == selected_status) &
    (tree_data['zip_city'] == selected_city)
]

print(f"Trees in {selected_city} with DBH between {min_dbh} and {max_dbh} inches and status '{selected_status}':")
print(f"Total count: {len(filtered_data)}")
print(f"\nBy zip code:")
print(filtered_data['zipcode'].value_counts().head(10))

# Create a chart for the filtered data
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Chart 1: DBH distribution of filtered data
ax1.hist(filtered_data['tree_dbh'], bins=20, alpha=0.7, color='green', edgecolor='black')
ax1.set_xlabel('Tree DBH (inches)')
ax1.set_ylabel('Frequency')
ax1.set_title(f'DBH Distribution - {selected_city}, {selected_status}')
ax1.grid(True, alpha=0.3)

# Chart 2: Tree count by zip code for filtered data
zip_counts = filtered_data['zipcode'].value_counts().head(10)
bars = ax2.bar(range(len(zip_counts)), zip_counts.values, color='skyblue')
ax2.set_xlabel('Zip Code')
ax2.set_ylabel('Number of Trees')
ax2.set_title(f'Tree Count by Zip Code - {selected_city}, {selected_status}')
ax2.set_xticks(range(len(zip_counts)))
ax2.set_xticklabels(zip_counts.index, rotation=45)

# Add value labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'{int(height)}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()
""" 