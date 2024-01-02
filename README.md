# Data Visualization Dashboard

This is a simple Flask web application that demonstrates data visualization using Plotly. The project includes three types of charts: Bar Chart, Pie Chart, and Line Chart.

## Prerequisites

Make sure you have Python installed on your machine.

```bash
# Install dependencies
pip install -r requirements.txt
```

## Running the Application

1. Clone the repository:

```bash
git clone https://github.com/NoorMahammad-S/Data_Visualization_Dashboard.git
cd Data_Visualization_Dashboard
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

Visit [http://localhost:5000/](http://localhost:5000/) in your browser to view the data visualization dashboard.

## Project Structure

- `app.py`: Flask application with sample data and chart creation.
- `dashboard.html`: HTML template for rendering the charts.

## Charts

- **Bar Chart:** Demonstrates a simple bar chart using Plotly Express.
- **Pie Chart:** Shows a basic pie chart using Plotly.
- **Line Chart:** Displays a line chart with markers using Plotly Subplots.

Feel free to modify the `data` dictionary in `app.py` to use your own dataset.
