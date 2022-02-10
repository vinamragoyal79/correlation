import plotly.express as px
import csv
import numpy as np

def plot_figure():
    with open("data2.csv") as file:
        df = csv.DictReader(file)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()

def get_data_source():
    coffee = []
    sleep = []
    with open("data2.csv") as file:
        df = csv.DictReader(file)
        for i in df:
            coffee.append(float(i["Coffee in ml"]))
            sleep.append(float(i["sleep in hours"]))
    return {"x":coffee, "y":sleep}

def find_correlation(data):
    correlation = np.corrcoef(data["x"], data["y"])
    print("corrlation is : \n ---->", correlation[0,1])


def setup():
    value = get_data_source()
    find_correlation(value)
    plot_figure()

setup()