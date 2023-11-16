# Import necessary libraries
from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objs as go
import numpy as np
from collections import deque

# Queues to store a maximum of 100 values for the data
# Older data is discarded to calculate anomalies
time_points = deque(maxlen=100)
sensor_values = deque(maxlen=100)
time = 0
app = Dash(__name__)

# Dash app to render the plot on a web page
app.layout = html.Div([
    html.H1(
        "Real-time Anomaly Detection",
        style={
            "textAlign": "center",
            "color": "#1F456E",  # Green text color
            "margin-bottom": "20px",
            "font-family": "'Arial', sans-serif",
        }
    ),
    dcc.Graph(
        id="real-time-graph",
        animate=True,
        config={'displayModeBar': False}  # Hide the mode bar
    ),
    dcc.Interval(id="graph-interval", interval=500, n_intervals=0),
])

def add_data_point():
    """
    Generates a new data point and appends it to the time_points and sensor_values deques.
    The data point consists of a pattern, seasonal variation, and random noise.
    Anomalies are introduced with a 7% probability.
    """
    global time
    time += 1
    time_points.append(time)

    pattern = np.cos(time * 0.1)
    seasonal = np.sin(time * 0.5)
    noise = np.random.normal(0, 0.1)

    # Data Point consisting of pattern data, seasonal data, and random noise
    data_point = pattern + seasonal + noise

    # Adding random anomaly with a probability of 7%
    if np.random.rand() < 0.07:
        data_point += np.random.normal(0, 10)

    sensor_values.append(data_point)

# Callback function for rendering graph every 20 milliseconds
@app.callback(
    Output("real-time-graph", "figure"),
    [Input("graph-interval", "n_intervals")]
)
def update_graph(value):
    """
    Callback function to update the graph with new data points and highlight anomalies.
    """
    # Adding a data point on every call to the callback function
    add_data_point()

    # Calculate mean and standard deviation
    mean_value = np.mean(sensor_values)
    std_dev = np.std(sensor_values)

    # Define Z-Score threshold for anomalies (e.g., 2.5)
    z_score_threshold = 2.5

    # Check if std_dev is not close to zero before division
    if std_dev > 1e-6:
        anomalies = [True if np.abs((value - mean_value) / std_dev) > z_score_threshold else False for value in sensor_values]
    else:
        # Handle the case when std_dev is close to zero (e.g., set anomalies to False)
        anomalies = [False] * len(sensor_values)

    # Specify colors for anomalies and non-anomalies
    anomaly_color = "#FF5733"  # Orange color for anomalies
    non_anomaly_color = "#3498DB"  # Blue color for non-anomalies

    # Scatter Plot and Line Plot to be rendered on Web Page
    dots_graph = go.Scatter(
        x=list(time_points),
        y=list(sensor_values),
        mode="markers",
        marker=dict(
            color=[anomaly_color if anomaly else non_anomaly_color for anomaly in anomalies],
            size=8,
            opacity=0.8,
            line=dict(color='#000000', width=0.5),
            symbol="circle"
        ),
        name="Sensor Data",
    )

    # Line Plot to be rendered on the web page
    line_graph = go.Scatter(
        x=list(time_points),
        y=list(sensor_values),
        mode="lines",
        line=dict(color="#4CAF50", width=2),  # Green color for the line
        name="Sensor Data (Line)",
    )

    # Anomaly Circle to highlight anomalies
    anomaly_circle = go.Scatter(
        x=[time_points[i] for i in range(len(time_points)) if anomalies[i]],
        y=[sensor_values[i] for i in range(len(sensor_values)) if anomalies[i]],
        mode="markers",
        marker=dict(
            size=20,
            color='rgba(255, 0, 0, 0.5)',  # Transparent red color for the circle
            line=dict(color='rgba(255, 0, 0, 1)', width=2),  # Solid red border for the circle
            symbol="circle"
        ),
        name="Anomaly",
    )

    # Layout settings for the graph
    layout = go.Layout(
        xaxis=dict(
            range=[max(0, time - 100), time],
            title="Time",
            showline=True,
            showgrid=False,
        ),
        yaxis=dict(
            range=[min(sensor_values) - 2, max(sensor_values) + 2],  # Adjusted y-axis range for better visibility
            title="Sensor Value",
            showgrid=False,
            zeroline=False,
        ),
        paper_bgcolor="#fff",  # Light gray background color
        plot_bgcolor="#fff",   # Light gray plot area color
    )

    return {"data": [dots_graph, line_graph, anomaly_circle], "layout": layout}

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)  # Use a different port, e.g., 8051, 8052, ...
