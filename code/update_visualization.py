import pandas as pd
import plotly.express as px
from pathlib import Path

charts_base_path = Path("charts")

df_targets = pd.read_csv("dataset/target_data.csv")
df_senrors = pd.read_csv("dataset/sensor_data.csv")

# box plot for targets
fig_box_targets = px.box(
    df_targets,
    x="Points",
    color="Title",
)

fig_box_targets.write_json(
    file=charts_base_path / "visualization_box_targets.json"
)

fig_box_sensor = px.box(
    df_senrors,
    x="xi",
    color="Title",
)

fig_box_sensor.write_json(
    file=charts_base_path / "visualization_box_sensors.json"
)