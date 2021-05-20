import pandas as pd
import plotly.express as px

df = pd.read_csv("p103(2).csv")
fig = px.scatter(df, x="date", y="cases",
	          size="Percentage",color="Country",)
fig.show()