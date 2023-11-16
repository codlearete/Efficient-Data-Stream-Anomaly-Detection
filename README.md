# Efficient-Data-Stream-Anomaly-Detection
This a Python script capable of detecting anomalies in a continuous data stream.

Objectives of the Project:

1.Algorithm Selection: Identify and implement a suitable algorithm for anomaly detection, capable of adapting to concept drift and seasonal variations.
2.Data Stream Simulation: Design a function to emulate a data stream, incorporating regular patterns, seasonal elements, and random noise.
3.Anomaly Detection: Develop a real-time mechanism to accurately flag anomalies as the data is streamed.
4.Optimization: Ensure the algorithm is optimized for both speed and efficiency.
5.Visualization: Create a straightforward real-time visualization tool to display both the data stream and any detected anomalies.

# 1. Algorithm Selection: 
  In this implementation, Z-Score thresholding is used for anomaly detection. 
  It is a simple algorithm that calculates the standard score (Z-Score) of each data point 
  and flags it as an anomaly if the absolute Z-Score is above a predefined threshold.

# 2. Data Stream Simulation:
  The add_data_point function generates synthetic sensor data that includes a pattern, seasonal variation, 
  and random noise. Anomalies are introduced with a 7% probability, simulating unexpected spikes in the sensor readings.
  The generated data points are stored in time_points and sensor_values deques.

# 3. Anomaly Detection:
  Anomaly detection is performed in the update_graph callback function. It calculates the mean and standard deviation 
  of the stored sensor values and determines anomalies based on the Z-Score threshold. Anomalies are then highlighted 
  in the real-time graph using different colors and marker sizes.

# 4. Optimization:
  The code uses efficient data structures like deques to store a fixed-size sequence of data. 
  Additionally, the algorithm calculates the mean and standard deviation in a way that minimizes computational complexity.

# 5. Visualization:
# The visualization is achieved using Plotly and Dash. The real-time graph is updated at regular intervals, 
# displaying the sensor data points, a line plot, and highlighted anomalies. The visualization provides a clear 
# representation of the data stream and detected anomalies, facilitating easy interpretation.



