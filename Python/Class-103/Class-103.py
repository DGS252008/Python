import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

#df = pd.read_csv("line_chart.csv")
#fig = px.line(df, x="Year", y="Per capita income", color="Country", title="Per Capita Income by Countries")

#df = pd.read_csv("data.csv")
#fig = px.bar(df, x="Country", y="InternetUsers", color="Country", title="Internet Users Per Country")

fig = px.scatter(df, x="Country", y="InternetUsers", size="Percentage", color="Country", title="Internet Users Per Country", size_max=60)
fig.show()