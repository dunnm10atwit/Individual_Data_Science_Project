import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Read in csv data set as data frame
crashes = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv")

# Convert date data to pandas date, create a year column, and remove index column
crashes["Date"] = pd.to_datetime(crashes.Date)
del crashes["index"]
crashes["Year"] = pd.DatetimeIndex(crashes['Date']).year
# print(crashes)  # Uncomment to view in terminal


# Statistics of data
basic_numerical_stats = crashes.dropna().describe()
print(f"Basis Stats: \n{basic_numerical_stats}\n")


# Average percentage of fatailties over aboard for all crashes
f_over_a = crashes["Fatalities"].mean() / crashes["Aboard"].mean()
print(f"Average percentage of fatailties over aboard: {f_over_a}\n")


# Percentage of crashes with zero fatalities
num_no_fatal = len(crashes.loc[crashes["Fatalities"] == 0])
percent_no_fatal = num_no_fatal / len(crashes)
print(f"Percentage of crashes with zero fatalities: {percent_no_fatal}\n")


# Percentage of crashes that had fatalities on the ground (NaN of ground doesn't count)
num_with_ground_fatal = len(crashes.loc[crashes["Ground"] != 0].dropna(subset=["Ground"]))
percent_with_ground = num_with_ground_fatal / len(crashes)
print(f"Percentage of crashes that had fatalities on the ground: {percent_with_ground}\n")


# Average fatalities per year if the plane crashed
f_per_year = crashes.groupby("Year")["Fatalities"].mean()
# print(f"Average fatalities per year: \n{f_per_year}\n")  # Uncomment to view in terminal

# Outptut to CSV file
f_per_year.to_csv("Outputted_Data\\Fatalities_Per_Year.csv")

# Chart of average fatalities vs year
f_per_year.plot()
plt.ylabel("Average Fatalities")
plt.title("Average Fatalities vs Year")
plt.savefig("Outputted_Data\\FatalitiesByYear.png")
# plt.show()


# Total fatalities per Operator
f_per_op = crashes.groupby("Operator")["Fatalities"].sum()
# print(f"Total fatalities per operator: \n{f_per_op}\n")  # Uncomment to view in terminal

# Output to CSV
f_per_op = pd.DataFrame({'Operator':f_per_op.index, 'Fatalities':f_per_op.values})
f_per_op.to_csv("Outputted_Data\\Fatalities_by_Operator.csv")

# Create chart of who was in charge of operating the plane (pie chart?); Need to simplify number of ops
simple_f_per_op = pd.DataFrame({'Operator': ["Alaska Airlines", "American Airlines", "Delta Airlines", "Frontier Airlines", "Hawaiian Airlines", "Southwest Airlines", "Spirit Airlines", "United Airlines"], 'Fatalities':[0, 0, 0, 0, 0, 0, 0, 0]})

# Count the number of fatallities that match the string in the operator field, should make sure it ignores previously counted
simple_f_per_op.at[0, "Fatalities"] = f_per_op.loc[f_per_op["Operator"].str.contains("Alaska", case=False)].sum(numeric_only=True)
simple_f_per_op.at[1, "Fatalities"] = f_per_op.loc[f_per_op["Operator"].str.contains("American Air", case=False)].sum(numeric_only=True)
simple_f_per_op.at[2, "Fatalities"] = f_per_op.loc[f_per_op["Operator"].str.contains("Delta", case=False)].sum(numeric_only=True)
simple_f_per_op.at[3, "Fatalities"] = f_per_op.loc[f_per_op["Operator"].str.contains("Frontier", case=False)].sum(numeric_only=True)
simple_f_per_op.at[4, "Fatalities"] = f_per_op.loc[f_per_op["Operator"].str.contains("Hawaiian", case=False)].sum(numeric_only=True)
simple_f_per_op.at[5, "Fatalities"] = f_per_op.loc[f_per_op["Operator"].str.contains("Southwest", case=False)].sum(numeric_only=True)
simple_f_per_op.at[6, "Fatalities"] = f_per_op.loc[f_per_op["Operator"].str.contains("Spirit", case=False)].sum(numeric_only=True)
simple_f_per_op.at[7, "Fatalities"] = f_per_op.loc[f_per_op["Operator"].str.contains("United Air Lines", case=False)].sum(numeric_only=True)

# Find all of the fatallities that didn't match anything
# f_per_op.loc[f_per_op["Operator"].str.contains("Military", case=False) | f_per_op["Operator"].str.contains("Alaskan Air", case=False) | f_per_op["Operator"].str.contains("American Air", case=False) | f_per_op["Operator"].str.contains("Delta", case=False) | f_per_op["Operator"].str.contains("Frontier", case=False) | f_per_op["Operator"].str.contains("Hawaiian", case=False) | f_per_op["Operator"].str.contains("Southwest", case=False) | f_per_op["Operator"].str.contains("Spirit", case=False) | f_per_op["Operator"].str.contains("United Air Lines", case=False)] = np.NaN
# simple_f_per_op.at[8, "Fatalities"] = f_per_op["Fatalities"].sum()

# Display simple op list to terminal
print(f"{simple_f_per_op}\n")

# Create pie chart
fig = plt.figure(figsize=(8, 5))
plt.pie(simple_f_per_op["Fatalities"], startangle=90)
plt.legend(labels=simple_f_per_op["Operator"], bbox_to_anchor=(1,1))
plt.title("Fatalities by Major American Airlines")
plt.savefig("Outputted_Data\\Airline_Pie_Chart.png")
# plt.show()


# https://financesonline.com/number-of-flights-worldwide/
# This website gives a breakdwon of the total flights per year from 2004 - 2021
# https://www.statista.com/statistics/564717/airline-industry-passenger-traffic-globally/
# This website breaks down the total number of passengers that flew per year

# Calculate the average chance of death from a flight
# Our data is from 1908 - 2009 (or 36,789 total days of data)
total_fatal = crashes["Fatalities"].sum() + crashes["Ground"].sum()
print(f"Total Fatalities {int(total_fatal)}\n")
fatal_per_day = total_fatal / 36789
print(f"Fatalities per Day: {fatal_per_day}\n")

total_num_passenger_2019 = 4543 * 1000000
num_pass_per_day = total_num_passenger_2019 / 365

print(f"Chance of Death from Flight: {fatal_per_day / num_pass_per_day * 100}%\n")
