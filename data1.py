import plotly.express as px
import csv
import numpy as np

def plot_figure():
    with open("data1.csv") as file:
        df = csv.DictReader(file)
        fig = px.scatter(df, x = "Roll No", y = "Days Present")
        #Switch between "Days Present" and "Marks In Percentage" to see a scatter graph of each one
        fig.show()

def get_data_source():
    rollno = []
    marks = []
    dayspresent = []
    with open("data1.csv") as file:
        df = csv.DictReader(file)
        for i in df:
            rollno.append(float(i["Roll No"]))
            marks.append(float(i["Marks In Percentage"]))
            dayspresent.append(float(i["Days Present"]))
    return {"x":rollno, "y":dayspresent}
    #Switch between dayspresent and marks to get correlation value of each

def find_correlation(data):
    correlation = np.corrcoef(data["x"], data["y"])
    print("corrlation is : \n ---->", correlation[0,1])


def setup():
    value = get_data_source()
    find_correlation(value)
    plot_figure()

setup()