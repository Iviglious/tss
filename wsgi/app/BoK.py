""" This module contains functions for generation of diagrams using bokeh library """

import flask
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
#from bokeh.charts import Bar
#from bokeh.sampledata.autompg import autompg as df
from bokeh.models.widgets import Panel, Tabs

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

def generate_sample_bar_tab(msg):
    """ Generate a sample graph of bars with tabs """

    fig1 = figure(width=600, height=400)
    fig1.vbar(x=[1, 2, 3], width=0.5, bottom=0, top=[1.2, 2.5, 3.7], color="firebrick")
    tab1 = Panel(child=fig1, title="User_1")

    fig2 = figure(width=600, height=400)
    fig2.vbar(x=[1, 2, 3], width=0.5, bottom=0, top=[3.2, 6.5, 5.7], color="brown")
    tab2 = Panel(child=fig2, title="User_2")

    tabs = Tabs(tabs=[tab1, tab2])

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(tabs)
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

def generate_bar_tab(msg, arr):
    """ Generate a graph of bars with tabs from array of data"""

    # get all users (distinct)
    usr_set = set()
    if arr:
        for exp in arr:
            usr_set.add(exp['user_name'])

    tab_list = list()
    # loop thru each user (create a tab per user)
    if arr:
        for usr in usr_set:
            d_date = [d["date"] for d in arr if d["user_name"] == usr]
            d_amount = [d["amount"] for d in arr if d["user_name"] == usr]
            fig = figure(width=300, height=200, x_axis_type="datetime")
            fig.vbar(x=d_date, width=0.5, bottom=0, top=d_amount, color="green")
            tab_list.append(Panel(child=fig, title=usr))

    tabs = Tabs(tabs=tab_list)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(tabs)
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
