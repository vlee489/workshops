import matplotlib.pyplot as plt
import csv

time_period = []
temperature = []

with open("data.csv", "r") as file:
    data = csv.DictReader(file)
    for row in data:
        time_period.append(row["time (seconds)"])
        temperature.append(row["temperature"])

print(time_period)
print(temperature)

plt.plot(time_period, temperature)
plt.title("Temperature")
plt.xlabel("Time / Seconds")
plt.ylabel("Temperature / *C")

plt.show()
