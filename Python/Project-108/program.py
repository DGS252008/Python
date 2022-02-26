import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")

company_df = df.loc[df["Mobile Brand"] == "Apple"]

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["company_df"])
fig.show()