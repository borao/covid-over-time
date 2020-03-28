import io

from flask import Flask, Response
from aggregate import get_county_data


import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/result')
def result():
    fig = get_county_data("Orange", "California")
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run()
