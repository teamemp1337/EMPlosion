import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from ipyvizzu import Chart, Data, Config, Style
from streamlit.components.v1 import html
from st_aggrid import AgGrid, GridOptionsBuilder
from st_vizzu import *

# Make the default width setting span the entire screen
st.set_page_config(layout="wide")
st.title('EMPlosion Risk Assessment Tool')
random_url = "https://assets.phenompeople.com/CareerConnectResources/prod/HONEUS/images/1920-568-coding-blog-1616781712070.png"
st.image(random_url, use_column_width="always")

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("""
The purpose of this app is to identify/assess risk for the EMPlosion wargaming scenario.
""")

scale = ['',
         'Very High',
         'High',
         'Moderate',
         'Low',
         'Very Low'
]

unit_df = pd.read_csv('risk_assessment.csv')
# AgGrid(unit_df)

gb = GridOptionsBuilder.from_dataframe(unit_df)
gb.configure_default_column(editable=True)

gb.configure_column('Risk Impact',
    cellEditor='agRichSelectCellEditor',
    cellEditorParams={'values':scale},
    cellEditorPopup=True
)

gb.configure_column('Risk Likelihood',
    cellEditor='agRichSelectCellEditor',
    cellEditorParams={'values':scale},
    cellEditorPopup=True
)

gb.configure_grid_options(enableRangeSelection=True)

response = AgGrid(
    unit_df,
    gridOptions=gb.build(),
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,
    enable_enterprise_modules=True
)

def create_chart():

    # initialize chart
    chart = Chart(width="640px", height="360px", display="manual")

    # add data
    data = Data()
    data_frame = pd.read_csv("https://github.com/vizzuhq/ipyvizzu/raw/main/docs/examples/stories/titanic/titanic.csv")
    data.add_data_frame(data_frame)

    chart.animate(data)

    # add config
    chart.animate(Config({"x": "Count", "y": "Sex", "label": "Count","title":"Passengers of the Titanic"}))
    chart.animate(Config({"x": ["Count","Survived"], "label": ["Count","Survived"], "color": "Survived"}))
    chart.animate(Config({"x": "Count", "y": ["Sex","Survived"]}))

    # add style
    chart.animate(Style({"title": {"fontSize": 35}}))

    return chart._repr_html_()

CHART = create_chart()
html(CHART, width=650, height=370)

# Load Data
df9 = pd.read_csv("music_data.csv", index_col=0)
# Create ipyvizzu Object with the DataFrame
obj = create_vizzu_obj(df9)

# Preset plot usage. Preset plots works directly with DataFrames.
bar_obj = bar_chart(df9,
            x = "Kinds",
            y = "Popularity",
            title= "1.Using preset plot function `bar_chart()`"
            )

# Animate with defined arguments
anim_obj = beta_vizzu_animate( bar_obj,
    x = "Genres",
    y =  ["Popularity", "Kinds"],
    title = "Animate with beta_vizzu_animate () function",
    label= "Popularity",
    color="Genres",
    legend="color",
    sort="byValue",
    reverse=True,
    align="center",
    split=False,
)

# Animate with general dict based arguments
_dict = {"size": {"set": "Popularity"},
    "geometry": "circle",
    "coordSystem": "polar",
    "title": "Animate with vizzu_animate () function",
    }
anim_obj2 = vizzu_animate(anim_obj,_dict)

# Visualize within Streamlit
with st.container(): # Maintaining the aspect ratio
    st.button("Animate")
    vizzu_plot(anim_obj2)

# if "mdf" not in st.session_state:
#     st.session_state.mdf = pd.DataFrame(
#         columns=['Unit', 'Risk', 'Impact', 'Likelihood', 'Risk Rating'])

# run = st.button('Submit')
# df_new = pd.DataFrame({'Unit': unit,
#                        'Risk': risk,
#                        'Impact': impact,
#                        'Likelihood': likelihood,
#                        'Risk Rating': risk_rating}, index=[unit])

# if run:
#     st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
#     st.dataframe(st.session_state.mdf)
#
# st.write(f"Total Rows: {st.session_state.mdf.shape[0]}")

# unit_df.iloc[1]

