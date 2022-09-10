from multiprocessing import context
from re import template
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from plotly.offline import plot
from plotly.graph_objs import Scatter
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Create your views here.

def index(request):
    header_str = 'Hello, dddd'
    template = loader.get_template('index.html')
    context = {'var1' : header_str, 'content' : ''}
    return HttpResponse(template.render(context,request))

def blank(request):
    header_str = 'Hello, dddd'
    template = loader.get_template('index.html')
    context = {'var1' : header_str, 'content' : 'blank.html'}
    return HttpResponse(template.render(context,request))


def dept(request):
    header_str = 'Hello, dddd'
    list_dept = ["MT300", "MT400", "MT500", "MT600", "MT700", "MT800", "MT900"]
    template = loader.get_template('index.html')
    context = {'var1' : header_str, 'content' : 'dept.html', 'list_dept' : list_dept}
    # return HttpResponse(template.render(context,request))
    return render(request, 'dept.html', context)

def x_chart(request):

    dbname = get_database()
    collection_name = dbname["mt800_tkantb"]
    key_dept = request.GET['key_dept']

    item_details = list(collection_name.find( {"lot_no" : "2207047"} ))


    thislist = []
    for item in item_details:
        temp = {"x" : item["record_time"], "y" : item["air_pres_lv"]}
        thislist.append(temp)

    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]

    x_data2 = [0,1,2,3]
    y_data2 = [x**1 for x in x_data2]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green'),
                        Scatter(x=x_data2, y=y_data2,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div') 

    header_str = 'Hello, dddd'
    template = loader.get_template('index.html')

    context = {'var1' : header_str, 'content' : 'x_chart.html', 'plot_div' : plot_div, 'list_of_lot' : get_lot(), 'key_dept' : key_dept}
    return HttpResponse(template.render(context,request))

def get_database():
    CONNECTION_STRING = "mongodb://mt800_user:mt800_user@163.50.57.97:27017/?authSource=mt800_tkantb"
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['mt800_tkantb']

def get_lot():
    dbname = get_database()
    collection_name = dbname["mt800_tkantb"]

    item_details = list(collection_name.distinct("lot_no")) 
    df = pd.DataFrame((item_details),
               columns =['Name'])
    df = df.dropna()
    # df = df[df['Name'].str.len()==7]
    print(df["Name"].astype(str).tolist())
    return df["Name"].astype(str).tolist()
