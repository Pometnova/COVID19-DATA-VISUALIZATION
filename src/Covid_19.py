import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

print('modules are imported')

dataset_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(dataset_url)

#1. ----------------------------------------------------
# visualization of all cases of Covid-19 in the world
fig = px.choropleth(df, locations = 'Country', locationmode = 'country names', color ='Recovered', animation_frame = 'Date')
fig.update_layout(title_text ='Global Deaths of Coved-19')
#fig.show()

#--show China table--
df_china = df[df.Country == 'China']
#print(df_china.head())

#--show only Date and Confirmed columns from China table--
df_china = df_china[['Date', 'Confirmed']]

#2.-------------------------------------------------------
#infection rate per every 24 hours. to do that use .diff()
df_china ['Infection Rate'] = df_china['Confirmed'].diff()
#print(df_china.head())

#3. -------------------------------------------------------
#show confirmed and infection rate
#px.line(df_china, x = 'Date', y = ['Confirmed', 'Infection Rate']).show()


#4. -------------------------------------------------------
# show how many people were infected in one day in China
df_china['Infection Rate'].max()
#print(df_china['Infection Rate'].max())

#5. --------------------------------------------------------
# create two new lists named countries and max_infection_rates
# List countries show all countries and use .unique() method to get rid of repetitions of countries name
# List max_infection_rates holds new list of countries with .diff information/that calculate difference between two days of confirmed covid cases
countries = list(df['Country'].unique())
max_infection_rates = []
#calculate the maximum rate of each country
for c in countries :
    MIR = df[df.Country == c].Confirmed.diff().max()   # .diff() calculate the differense between two values in one column in two rows
                                                       # отнимает значение нижнего числа в строке от верхнего в одном и том же столбце]
    max_infection_rates.append(MIR)  #.appedd -- add country to the list that was calculated in a for each loop(MIR) above
#print(max_infection_rates)

# 5a ----------------------------------------------------
df_MIR = pd.DataFrame()
df_MIR['Country'] = countries
df_MIR['Max Infection Rate'] = max_infection_rates
#print(df_MIR)

# 5b -----------------------------------------------------
#px.bar(df_MIR, x='Country', y='Max Infection Rate', color = 'Country',
# ='Global Maximum Infection Rate').show()


#6. ------------------------------------------------------
#calculate the infection rate in the Italy
italy_lockdown_start_date = '2020-10-01'
italy_lockdown_a_month_later = '2020-08-01'
italy_lockdown_a_two_month_later = '2021-07-01'
df_italy = df[df.Country == 'Italy']
df_italy['Infection Rate'] = df_italy.Confirmed.diff()
#print(df_italy.head())

#visualisation.
#add vertical line that indicate starting day of the lockdown
fig = px.line(df_italy, x = 'Date', y = 'Infection Rate', title = 'Before and after Lockdown in Italy')
fig.add_shape(
    dict(
        type="line",
        x0=italy_lockdown_start_date,
        y0=0,
        x1=italy_lockdown_start_date,
        y1= 205000,  #df_italy['Infection Rate'].max(),
        line = dict(color='red', width=3)

    )
)
fig.add_shape(
    dict(
        type="line",
        x0 = italy_lockdown_a_two_month_later,
        y0=0,
        x1=italy_lockdown_a_two_month_later,
        y1= 205000,
        line = dict(color='blue', width=3)

   )
)

fig.add_annotation(
    dict(
        x = '2020-07-01',
        y = df_italy['Infection Rate'].max(),
        text = 'Starting day of the lockdown',
    )
)

fig.add_annotation(
    dict(
        x='2020-08-01',
        y=df_italy['Infection Rate'].min(),
       text='One month after lockdown'

 )
)

#fig.show()


#7. -------------------------------------------------------------------
#calculate the deaths rate
df_italy['Deaths Rate'] = df_italy.Deaths.diff()
#show in a one graph Infection rate and Deaths rate
fig = px.line(df_italy, x='Date', y=['Infection Rate', 'Deaths Rate'])


df_italy['Infection Rate']=df_italy['Infection Rate']/df_italy['Infection Rate'].max()
df_italy['Deaths Rate'] = df_italy['Deaths Rate']/df_italy['Deaths Rate'].max()
fig=px.line(df_italy,x='Date', y=['Infection Rate', 'Deaths Rate'])

#add vertical lines in the diagram
fig.add_shape (
    dict(
        type='line',
        x0=italy_lockdown_start_date,
        y0=0,
        x1=italy_lockdown_start_date,
        y1=df_italy['Infection Rate'].max(),
        line=dict(color='yellow', width =3)
    )
)

fig.add_shape(
    dict(
        type="line",
        x0 = italy_lockdown_a_two_month_later,
        y0=0,
        x1=italy_lockdown_a_two_month_later,
        y1= df_italy['Infection Rate'].max(),
        line = dict(color='green', width=3)

    )
)
#fig.show()

#8. ----------------------------------------------------------------

#Colect data about Covid-19 cases in Germany

germany_lockdown_start_date = '2020-03-23'
germany_lockdown_month_later = '2020-04-23'
df_germany = df[df.Country == 'Germany']
df_germany['Infection Rate']= df_germany['Confirmed'].diff()
df_germany['Deaths Rate'] = df_germany['Deaths'].diff()

#show the diagram/visualization
fig = px.line(df_germany, x='Date', y=['Infection Rate', 'Deaths Rate'])

#normalize the graphic to show tha date in the same range(одинаковый диапазон)
df_germany['Infection Rate']=df_germany['Infection Rate']/df_germany['Infection Rate'].max()
df_germany['Deaths Rate']=df_germany['Deaths Rate']/df_germany['Deaths Rate'].max()
fig = px.line(df_germany, x='Date', y=['Infection Rate','Deaths Rate'])

#add shape/add vertical lines that indicate start and end of the lockdown
fig.add_shape (
    type ='line',
    x0=germany_lockdown_start_date,
    y0=0,
    x1=germany_lockdown_start_date,
    y1=df_germany['Infection Rate'].max(),
    line=dict(color='orange', width=3)
)
fig.add_shape(
    type='line',
    x0=germany_lockdown_month_later,
    y0=0,
    x1=germany_lockdown_month_later,
    y1=df_germany['Infection Rate'].max(),
    line=dict(color='green', width=3)
)
fig.show()











