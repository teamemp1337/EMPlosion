import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

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
gb.configure_default_column(editable=False)

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

