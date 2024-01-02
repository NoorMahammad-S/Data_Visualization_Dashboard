from flask import Flask, render_template
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

app = Flask(__name__)

@app.route('/')
def index():
    # Create sample data for demonstration
    data = {'Category': ['A', 'B', 'C', 'D'],
            'Value': [30, 45, 12, 78]}

    # Create a bar chart using Plotly
    bar_chart = px.bar(data, x='Category', y='Value', title='Sample Bar Chart')

    # Create a pie chart using Plotly
    pie_chart = go.Figure(data=[go.Pie(labels=data['Category'], values=data['Value'])])
    pie_chart.update_layout(title='Sample Pie Chart')

    # Create a line chart using Plotly
    line_chart = make_subplots(rows=1, cols=1)
    line_chart.add_trace(go.Scatter(x=data['Category'], y=data['Value'], mode='lines+markers', name='Line Chart'))
    line_chart.update_layout(title='Sample Line Chart')

    # Render the dashboard with three charts
    return render_template('dashboard.html',
                           bar_chart=bar_chart.to_html(full_html=False),
                           pie_chart=pie_chart.to_html(full_html=False),
                           line_chart=line_chart.to_html(full_html=False))

if __name__ == '__main__':
    app.run(debug=True)
