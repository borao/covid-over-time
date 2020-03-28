import io

from flask import Flask, Response, render_template, request
from aggregate import get_county_data


import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)


@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/result', methods=['GET', 'POST'])
def result():
    fig = get_county_data(request.form.get('state'), request.form.get('county'))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run()
