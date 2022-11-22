import base64
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('EMPlosion Risk Assessment Tool')

# Make the default width setting span the entire screen
# st.set_page_config(layout="wide")
random_url = "https://assets.phenompeople.com/CareerConnectResources/prod/HONEUS/images/1920-568-coding-blog-1616781712070.png"
st.image(random_url, use_column_width="always")

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("""
This app enables dynamic risk assessment for the EMPlosion wargaming scenario.
""")

units = ['87 ABW', '305 AMW', '621 CRW', '514 AMW', '108 W']
columns1 = ['Impact', 'Likelihood', 'Current Mitigation', 'Existing Control Effectiveness', 'Risk Rating']
impact_scale = ['Very High', 'High', 'Moderate', 'Low', 'Very Low']
prob_scale = ['Very High', 'High', 'Moderate', 'Low', 'Very Low']

df = pd.DataFrame([
                 [(st.selectbox('Impact',list(impact_scale), key=1,label_visibility="hidden")),
                 (st.selectbox('Impact',list(impact_scale), key=2,label_visibility="hidden")), 3, 4],
                 ['305 ABW', 35, 7, 36],
                 ['621 ARW', 5, 17, 16],
                 ['514 ARW', 5, 37, 6]
                  ],
    index=["87 ABW", "305 ABW", "621 ARW", "514 ARW"], # <--- more items added
    columns=["Impact", "Likelihood", "Current Mitigation", "Risk Rating"])
# team = pd.DataFrame(units,columns=columns)
st.dataframe(df,use_container_width=True)

st.sidebar.header('User Input Risks')

selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2023))))
selected_unit = st.sidebar.selectbox('Unit', list(units))
selected_impact_scale = st.sidebar.selectbox('Risk Impact', list(impact_scale))
selected_prob_scale = st.sidebar.selectbox('Risk Likelihood', list(prob_scale))


# Web scraping of NBA player stats
# @st.cache
# def load_data(year):
#     url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
#     html = pd.read_html(url, header=0)
#     df = html[0]
#     raw = df.drop(df[df.Age == 'Age'].index)  # Deletes repeating headers in content
#     raw = raw.fillna(0)
#     playerstats = raw.drop(['Rk'], axis=1)
#     return playerstats


# playerstats = load_data(selected_year)

# Sidebar - Team selection
# sorted_unique_team = sorted(playerstats.Tm.unique())
# selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# selected_unit = st.sidebar.multiselect('Unit', jbm, jbm)

# Sidebar - Position selection
# unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
# selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
# df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

df_selected_risks = list(selected_impact_scale) + list(selected_prob_scale)
# st.dataframe(df_selected_risks)

st.header('Profile of Selected Risk(s)')
# st.write(
#     'Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
# st.dataframe(df_selected_team)


# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
# def filedownload(df):
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
#     href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
#     return href


# st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap
# if st.button('Intercorrelation Heatmap'):
#     st.header('Intercorrelation Matrix Heatmap')
#     df_selected_team.to_csv('output.csv', index=False)
#     df = pd.read_csv('output.csv')
#
#     corr = df.corr()
#     mask = np.zeros_like(corr)
#     mask[np.triu_indices_from(mask)] = True
#     with sns.axes_style("white"):
#         f, ax = plt.subplots(figsize=(7, 5))
#         ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
#     st.pyplot()

#
# ## Step 3: Let's Write Some Text
# st.title("Streamlit 3000")
# st.markdown("# Streamlit 6000")

# ## Step 4: Let's display a Dataframe

# df = pd.read_csv("countries of the world.csv", decimal=",")
# df
# ## Btw you can easily print debug while working
# st.write(df.dtypes.values.tolist()[2:4])
# # ## Step 5: Let's get interactive
# cols = df.columns.values.tolist()
# cols = [c for c, t in zip(cols, df.dtypes.values.tolist())
#         if "float" in str(t).lower() or "int" in str(t).lower()]
# our_chosen_col = st.selectbox(label="Select A Column", options=cols)

# ## Step 6: Let's use the value
# c1, c2, c3 = st.columns(3)
# with c1:
#     st.header("Mean")
#     st.metric(label="Mean", value=df[our_chosen_col].mean().round(1),
#               delta=None)
# with c2:
#     st.header("Median")
#     st.metric(label="Median",
#               value=df[our_chosen_col].median().round(1),
#               delta=(df[our_chosen_col].mean() - df[
#                   our_chosen_col].median()).round(1))
# with c3:
#     st.header("Sum")
#     st.metric(label="Sum", value=df[our_chosen_col].sum().round(1))
#
# # ## Step 7: All of Plotly, Matplolib, Seaborn and others do work!
# # ## pip install plotly
#
# fig = px.scatter(df, x=our_chosen_col, y="Area (sq. mi.)",
#                  # size="pop",
#                  color="Region",
#                  hover_name="Country",
#                  log_x=True)
# st.plotly_chart(fig, use_container_width=True)
# #
# # ## Step 8: Just to show of
# df_lat = pd.read_csv("country_lat_lon.csv")
# df_lat.columns = ["_", "Country", "lat", "lon"]
# df["Country"] = df["Country"].apply(lambda x: x.strip())
# ## use our colum again and select only the top-10
# df = pd.merge(
#     df.sort_values(our_chosen_col, ascending=False).head(30), df_lat,
#     on="Country", how='left').dropna()
# st.map(df)
