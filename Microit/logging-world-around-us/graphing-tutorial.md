# Graphics data from the Micro: bit

### Note!

This is part to the Logging the World Around US workshop. You should have completed the logging tutorial in Makecode and uploaded it to your Micro:bit prior to starting this workshop.

## Getting Started

To get started with writing some Python 3, launch Mu or Thonny. This guide will assume you're using Mu.

## Copying your data

Before we start writing more code, we're going to move the data that you've captured from the Micro:bit to the computer.

1. Start off by plugging in your Micro:bit, if you've not done so already
2. On the drive that shows up, find the file that ends in `.csv` and then copy this file over to Mu.
3. Finally rename the file to something like `data.csv` so it's easier to work with.

## Basic graph with temperature

1. To start, let's import all the packages we will be using to make our graph.

    ```python
    import matplotlib.pyplot as plt
    import csv
    ```

2. Now let's get some lists made.
   
   Lists are collections of data. We can add, delete or change the data in them as we wish.
   The following code will set up the 2 lists we need. One is for holding the temperature data, and the other is to hold the time the data was taken. This is done by adding ` = []` after the the variable name.

    ```python
    temperature = []
    time_period = []
    ```

3. Now we'll open the file that contains the data, then add the data to the two lists we just created. We need to do this in a single step as we can only read the file while we have it open.

    1. First of all we'll open the file with the first line shown below.
    2. Then we'll load the file in using `csv.DictReader()`
    3. Then we'll go over each row using a `for` loop
    4. Finally for each row we'll add the `time_period` and `temperature`

    ```python
    with open("data.csv", "r") as file:
        data = csv.DictReader(file)
        for row in data:
            time_period.append(row["time (seconds)"])
            temperature.append(row["temperature"])
    ```

4. Now let's add the code that will create the graph itself.

   First we need to pass the the data to graph, to do this we can use `plt.plot()` passing in the `time_period` and `temperature`. This will put the time on the X axis, and temperature on the Y axis.

    ```python
    plt.plot(time_period, temperature)
    ```

5. Then let's give out graph a title and label the axes.

    ```python
    plt.title("Temperature")
    plt.xlabel("Time / Seconds")
    plt.ylabel("Temperature / *C")
    ```

6. Finally we need to show the graph.

    ```python
    plt.show()
    ```

7. Now run the code and you should see the graph.

## Now try
Now you've graphed the temperature, try to graph

- heading
- light
- acceleration

## Example program
```python
# Import everything
import matplotlib.pyplot as plt
import csv

# Setup Lists
time_period = []
temperature = []

# Open file and load time_period and temperature
with open("data.csv", "r") as file:
    data = csv.DictReader(file)
    for row in data:
        time_period.append(row["time (seconds)"])
        temperature.append(row["temperature"])

# Create Graph
plt.plot(time_period, temperature)
plt.title("Temperature")
plt.xlabel("Time / Seconds")
plt.ylabel("Temperature / *C")

# Show Graph
plt.show()
```