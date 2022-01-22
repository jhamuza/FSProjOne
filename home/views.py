from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect, render
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import plotly
import matplotlib.pyplot as plt
import pandas as pd
from django.urls import reverse
from home.forms import CustomUserCreationForm # Changed user to home, as we wanted this to import the CustomUserCreationForm from home

# Create your views here3

#@login_required(login_url='/accounts/login/')

def dashboard(request):
    return render(request, "home/dashboard.html")

def ref(request):
    return render(request, "home/references.html")

def csvfiles(request):
    return render(request, "home/files.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "home/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))

def irrigation(request):
    return render(request, "home/irrigation.html")

def infobanjir(request):
    return render(request, "home/infobanjir.html")

#@login_required(login_url='/accounts/login/')
def home(request):
    
    DID_December =  pd.read_csv(r"C:\Users\User\Documents\SideHustles\FSProjOne\XJ_JPNB\DID_December.csv")
    PIB =  pd.read_csv(r"C:\Users\User\Documents\SideHustles\FSProjOne\XJ_JPNB\PIB_Sarawak River.csv")

    def rivLevel():
        frequency = [89, 6]
        status = ['Normal', 'Danger']
        
        fig = px.pie(values=frequency, names=status)
        fig.update_traces(textfont_size=12)
        
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def aveFlood():
        
        colors = plotly.colors.qualitative.Prism

        fig = px.bar(DID_December, DID_December['Date'], y=DID_December['Average'],
             color=DID_December['Average'], barmode='stack',
             text=DID_December['District'],
             color_discrete_sequence=colors)

        fig.update_layout(title = {'text': "Average Water Level of Flood Areas by Dates",'x':0.5, 'xanchor': 'center'},
                        title_font_size=30,
                        legend=dict(yanchor="bottom", y=0.0, 
                                    xanchor="right", x=1.2),
                        legend_font_size=16, 
                        xaxis_title = 'Date', 
                        yaxis_title ='Average Water Level',
                        xaxis_tickangle=-45,
                        width = 1080, height = 600)

        # Don't forget to remove from update_traces
        fig.update_traces(textfont_size=12)
        
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div
    
    def sarawakRiver():
        fig = px.box(data_frame = PIB,x = "Status",y = "Current Water Level",color= "Status")

        fig.update_layout(height=600, width=600)

        fig.update_yaxes(range=[-5, 45])

        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': rivLevel(),
        'plot2': sarawakRiver(),
        'plot3': aveFlood(),
        # 
        
    }

    return render(request, 'home/dashboard.html', context)

class page2PageView(TemplateView): #was planning to add another page, this could be handy once i wanted to designate the login page
    template_name ="home/Page2.html"

