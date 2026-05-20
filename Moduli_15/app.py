import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# READ DATASET
# =====================================================

df = pd.read_csv("weather_data.csv")

# =====================================================
# CLEAN DATA
# =====================================================

# Remove spaces from column names
df.columns = df.columns.str.strip()

# Fix negative temperature values like (0.3)
df['temperature'] = df['temperature'].astype(str)
df['temperature'] = df['temperature'].str.replace('(', '-', regex=False)
df['temperature'] = df['temperature'].str.replace(')', '', regex=False)

# Convert temperature to float
df['temperature'] = df['temperature'].astype(float)

# Create full date
df['date'] = pd.to_datetime(
    df['year'].astype(str) + '/' + df['day']
)

# =====================================================
# 1. TEMPERATURE OVERVIEW
# =====================================================

print("\n========== TEMPERATURE OVERVIEW ==========")

average_temperature = df['temperature'].mean()

print(f"Average Temperature: {average_temperature:.2f} °C")

# =====================================================
# 2. MONTHLY TEMPERATURE
# =====================================================

print("\n========== MONTHLY TEMPERATURE ==========")

# Create month column
df['month'] = df['date'].dt.month

# Calculate monthly average temperature
monthly_temperature = df.groupby('month')['temperature'].mean()

print(monthly_temperature)

# Bar Plot
plt.figure(figsize=(10,5))

monthly_temperature.plot(
    kind='bar',
    color='skyblue'
)

plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.grid(True)

plt.show()

# =====================================================
# 3. HIGHS AND LOWS
# =====================================================

print("\n========== HIGHS AND LOWS ==========")

# Hottest day
hottest_day = df.loc[df['temperature'].idxmax()]

# Coldest day
coldest_day = df.loc[df['temperature'].idxmin()]

print("\nHottest Day:")
print(hottest_day)

print("\nColdest Day:")
print(coldest_day)

# =====================================================
# 4. TEMPERATURE TRENDS
# =====================================================

print("\n========== TEMPERATURE TRENDS ==========")

plt.figure(figsize=(12,5))

plt.plot(
    df['date'],
    df['temperature'],
    color='red'
)

plt.title("Temperature Changes Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.grid(True)

plt.show()

# =====================================================
# 5. SEASONAL AVERAGE TEMPERATURE
# =====================================================

print("\n========== SEASONAL AVERAGE TEMPERATURE ==========")

# Define seasons
def get_season(month):

    if month in [12, 1, 2]:
        return "Winter"

    elif month in [3, 4, 5]:
        return "Spring"

    elif month in [6, 7, 8]:
        return "Summer"

    else:
        return "Fall"

# Create season column
df['season'] = df['month'].apply(get_season)

# Calculate seasonal average temperature
seasonal_temperature = df.groupby('season')['temperature'].mean()

print(seasonal_temperature)

# Line Plot
plt.figure(figsize=(8,5))

seasonal_temperature.plot(
    kind='line',
    marker='o',
    linewidth=3
)

plt.title("Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Temperature")
plt.grid(True)

plt.show()