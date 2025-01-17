import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')
fig = px.histogram(car_data, x="odometer")
fig.show()