# Individual_Data_Science_Project

# Introduction

The purpose of this project is primarily to practice my skills working with data with the tools python has to offer (such as Pandas, NumPy, and Matplotlib). The secondary objective is to understand just how safe traveling by air is. I've always heard that flying is very safe, but I was curious just how safe it is. This would include the chance of death from a flight, comparing airlines by total number of fatalities, comparing fatalities vs year, and other metrics.

# Selection of Data

The data selected was found on kaggle.com and is available [here](https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908). A copy of the csv is included in this repository.

This dataset contains information on airplane crashes since 1908 until 2009. In total, that is 5,267 data points with information on the date, time, location, operator, flight number, route, plane type, registration, construction or serial number/line or fuselage number, number of people aboard, number of fatalities, number of fatalities on the ground, and a short summary of the incident. This is a lot of information, and I luckily only had to do minimal cleaning with turning the date column from a string into a Pnadas Date-Time object.

For my project I primarily focused on the columns date, operator, number of people aboard, number of fatalities, and number of fatalities on the ground.

# Methods

The following libraries were utilized:
 - NumPy
 - Pandas
 - Matplotlib

Of these, Pandas was used the most extensively, primarily for its data frames and data manipulation. Matplotlib was used for any visualizations created, and Numpy was used for its NaN value.

# Results

# Discussion

# Summary

# References

[1] https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908

[2] https://www.statista.com/statistics/564717/airline-industry-passenger-traffic-globally/
