# %%
import pandas as pd
import plotly.express as px
from pathlib import Path
import numpy as np

# %%
charts_base_path = Path("charts")

df_targets = pd.read_csv("dataset/target_data.csv")
df_senrors = pd.read_csv("dataset/sensor_data.csv")

# %%
# box plot for targets
fig_box_targets = px.box(
    df_targets,
    x="Points",
    color="Title",
)

fig_box_targets.write_json(
    file=charts_base_path / "visualization_box_targets.json"
)

# %%
# sensor data
fig_box_sensor = px.box(
    df_senrors,
    x="xi",
    color="Title",
)

fig_box_sensor.write_json(
    file=charts_base_path / "visualization_box_sensors.json"
)

# %%
def cart2pol(x, y):
    theta = np.arctan2(y, x) / 2 / np.pi * 360
    rho = np.hypot(x, y)
    return theta, rho

df_targets[["theta", "rho"]] = list(df_targets.apply(lambda x: cart2pol(x.x, x.y), axis=1))

fig_polar = px.scatter_polar(
    df_targets,
    r="rho", theta="theta",
    color="Title",
    color_discrete_sequence=px.colors.sequential.Plasma_r
)

fig_polar.update_layout(
    polar = dict(
        radialaxis = dict(
            tickvals=[],
            ticktext=[]
        ),
        angularaxis = dict(
            tickmode="array",
            tickvals=[],
            ticktext=[]
            )
    ),
    legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.4,
    xanchor="right",
    x=1
)
)

fig_polar.write_json(
    file=charts_base_path / "visualization_polar_targets.json"
)
# %%
