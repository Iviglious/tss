""" This module contains functions for generation of diagrams using bokeh library """

import flask
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

from app.forms import ExpenseForm

# Visualisation helping functions using bokeh library

def generate_sample_graph(msg):
    """ Generate a sample dummy diagram """

    # Create a polynomial line graph with those arguments
    x_list = list(range(1, 6))
    fig = figure(title="Polynomial")
    fig.line(x_list, [i ** 2 for i in x_list], color="blue", line_width=2)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)
    html = flask.render_template(
        'demo.html'
        , plot_script=script
        , plot_div=div
        , js_resources=js_resources
        , css_resources=css_resources
        , form=ExpenseForm()
        , message=msg
    )
    return encode_utf8(html)
