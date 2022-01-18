from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd

# Create your views here3

#@login_required(login_url='/accounts/login/')
def home(request):
    def scatter():
        
        df =  pd.read_csv(r"C:\Users\User\Documents\SideHustles\FSProjOne\ADS.csv")

        data = [go.Histogram(x=df['Branch'],marker=dict(color='green'))] #histogram only needs one set of data

        layout = go.Layout(
        hovermode='closest',
         xaxis = {'title':'Language Branch'},
         yaxis = {'title': 'Number of Language Included'},
        title = 'Language Branch vs Language Variation'
        )


        fig = go.Figure(data=data,layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter()
    }

    return render(request, 'home/welcome.html', context)

