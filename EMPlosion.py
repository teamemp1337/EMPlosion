import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from ipyvizzu import Chart, Data, Config, Style
from streamlit.components.v1 import html
from st_aggrid import AgGrid, DataReturnMode, GridOptionsBuilder, GridUpdateMode, JsCode
from st_aggrid.shared import GridUpdateMode, DataReturnMode
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

gb = GridOptionsBuilder.from_dataframe(unit_df)
gb.configure_default_column(groupable=True,
                            value=True,
                            enableRowGroup=True,
                            aggFunc='sum',
                            editable=True)

gb.configure_column('Risk Impact',
                    cellEditor='agRichSelectCellEditor',
                    cellEditorParams={'values':scale},
                    cellEditorPopup=True)

gb.configure_column('Risk Likelihood',
                    cellEditor='agRichSelectCellEditor',
                    cellEditorParams={'values':scale},
                    cellEditorPopup=True)

gb.configure_grid_options(enableRangeSelection=True)

response = AgGrid(unit_df,
                  gridOptions=gb.build(),
                  fit_columns_on_grid_load=True,
                  allow_unsafe_jscode=True,
                  enable_enterprise_modules=True,
                  editable = True,
                  theme = 'streamlit',
                  data_return_mode = DataReturnMode.AS_INPUT,
                  update_mode = GridUpdateMode.MODEL_CHANGED)

st.dataframe(unit_df)    # confirm changes to df