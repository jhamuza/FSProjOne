# Forward School Applied Data Science Project 1

## How to Install

- Create an virtual env 
    1. Check if you have a virtual env ``virtualenv --version``
    2. (Not Installed) Dont see a version number? run ``sudo pip install virtualenv``
    3. (Installed) Make a folder within the highest file of the project ``mkdir ~/env``
    4. run ``.\env\Scripts\activate``

- ``pip install -r requirements.txt``

- Create a Postgres Database & connect it within the plotly_django_tutorial.py settings

- ``python manage.py makemigrations``

- ``python manage.py migrate``

- ``python manage.py runserver``

# Project Introduction

Floods are identified as the most devastating hazards in the world (Prăvălie and Costache, 2013; Mishra and Sinha, 2020; Sarkar and Mondal, 2020). Flood often causes severe loss of human lives and socio-economic damage (Hirabayashi et al., 2013; Costache, 2019). The public in Sarawak has been urged to make essential preparations for potential floods and landslides, according to a news article published on December 23, 2021 by The Borneo Post, following the worst flood events in decades caused by three days of torrential rain in Klang Valley and Pahang. Based on another infographic released by MetMalaysia on December 22, 2021, a monsoon surge is forecast from December 27 to December 29, 2021, with constant rain in the western half of Sarawak and eastern Sabah during that time, adding to the concern.

In our first Mini Project for Applied Data Science with Forward School, we analyzed several data sets provided by Public Info Banjir and the Department of Irrigation and Drainage on the occurrence of floods and their average height in Sarawak, as well as to share the documentation involved from data scraping, cleaning, analyzing and visualization.

This is followed by a discussion centred on the aforementioned graphs and how the approaching rainy season will effect certain areas of Sarawak, as well as how the data may be used to assist both the government and the general population in mitigating the flood's impact.

# Challenges

- Data is not centralised and made available to the general public
- The transition from dealing with cleansed data to scraping your own data from scratch was a huge learning curve
- Implementing Django to visualise and make the project public was first difficult, but as the project progressed, it became manageable

# Future Works

## Web Scraping, Data Cleaning and Visualization

- Scrap daily data from Public Info Banjir for at least 3 days to better visualise the pattern of the water level in Sarawak River.
- Scrap at least 3 months of data from Department of Irrigation & Drainage Sarawak to anlyse the pattern of flood events. 

## Django Development

- To include better UI/UX experience for users when accessing the dashboard, especially in terms of the onboarding by utilizing more CSS / SCSS while also making the whole platform more responsive to both mobile and desktop users
- Pushing the project to an instance, either on Heroku or Digital Ocean
- To add query function, where users could actually search for specific terms and divisions of interest


# References

[Department of Irrigation and Drainage Sarawak](https://did.sarawak.gov.my/page-0-0-1517-Recorded-Flood-Event-in-Sarawak-P18.html)

[Public Info Banjir](https://publicinfobanjir.water.gov.my/)

# Useful Links

[Postgres](https://www.postgresql.org/)

[Bootstrap Theme Used](https://startbootstrap.com/themes/sb-admin-2/)

[Plotly](https://plot.ly/python/)

[Dash Docs](https://dash.plot.ly/)
