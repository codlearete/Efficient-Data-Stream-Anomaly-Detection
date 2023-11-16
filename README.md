I am Jir Et Katharpi
(20IM10015)

# Efficient-Data-Stream-Anomaly-Detection
This a Python script capable of detecting anomalies in a continuous data stream.

# Objectives of the Project:

# 1. Algorithm Selection: 
  In this implementation, Z-Score thresholding is used for anomaly detection. 
  It is a simple algorithm that calculates the standard score (Z-Score) of each data point 
  and flags it as an anomaly if the absolute Z-Score is above a predefined threshold.

# 2. Data Stream Simulation:
  The add_data_point function generates synthetic sensor data that includes a pattern, seasonal variation, 
  and random noise. Anomalies are introduced with a 8% probability, simulating unexpected spikes in the sensor readings.
  The generated data points are stored in time_points and sensor_values deques.

# 3. Anomaly Detection:
  Anomaly detection is performed in the update_graph callback function. It calculates the mean and standard deviation 
  of the stored sensor values and determines anomalies based on the Z-Score threshold. Anomalies are then highlighted 
  in the real-time graph using different colors and marker sizes.

# 4. Optimization:
  The code uses efficient data structures like deques to store a fixed-size sequence of data. 
  Additionally, the algorithm calculates the mean and standard deviation in a way that minimizes computational complexity.

# 5. Visualization:
  The visualization is achieved using Plotly and Dash. The real-time graph is updated at regular intervals, 
  displaying the sensor data points, a line plot, and highlighted anomalies. The visualization provides a clear 
  representation of the data stream and detected anomalies, facilitating easy interpretation.


# Real-time Anomaly Detection

This project demonstrates real-time anomaly detection using Dash and Plotly.

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/codlearete/Efficient-Data-Stream-Anomaly-Detection.git
2. Navigate to the project directory:
   ```bash
   cd Efficient-Data-Stream-Anomaly-Detection
4. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   
   On Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   On Linux/macOS:
   ```bash
   source venv/bin/activate
6. Install dependencies
   ```bash
   pip install -r requirements.txt
7. Run the following command to start the Dash application:
   ```bash
   python your_script_name.py

Replace your_script_name.py with the actual name of your Python script.

Open your web browser and go to http://localhost:8050/ to view the real-time anomaly detection dashboard.

