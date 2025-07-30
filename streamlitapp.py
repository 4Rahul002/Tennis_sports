import streamlit as st
import pymysql
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Tennis Rankings Explorer", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #8bc34a, #4caf50);
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #2c3e50, #34495e);
        color: white;
        padding: 20px;
    }
    .sidebar .sidebar-content .stSelectbox,
    .sidebar .sidebar-content .stSlider,
    .sidebar .sidebar-content .stTextInput {
        background-color: rgba(255, 255, 255, 0.2);
        color: white;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.5);
    }
    .sidebar .sidebar-content label {
        color: white;
        font-size: 16px;
        margin-bottom: 10px;
        display: block;
    }
    .heading, .subheading {
        color: white;
        background-color: rgba(44, 62, 80, 0.7);
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        margin: 10px 0;
        text-align: center;
    }
    .heading {
        font-size: 2.5em;
    }
    .subheading {
        font-size: 1.5em;
    }
    .content-box {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin: 10px auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Function to create a database connection using pymysql
def get_connection():
    try:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="Laptop@321",
            database="tennis"
        )
    except pymysql.Error as err:
        st.error(f"Error connecting to MySQL: {err}")
        return None

# Function to load data from the database
@st.cache_data
def load_data(query):
    conn = get_connection()
    if conn is not None:
        try:
            df = pd.read_sql(query, conn)
            conn.close()
            return df
        except pymysql.Error as err:
            st.error(f"Error loading data: {err}")
    return pd.DataFrame()

# Load datasets
df_rankings = load_data("""
    SELECT r.rank, r.movement, r.points, r.competitions_played, c.name AS competitor_name, c.country, c.abbreviation
    FROM Competitor_Rankings r
    JOIN Competitor c ON r.competitor_id = c.competitor_id
""")

df_venues = load_data("""
    SELECT v.venue_id, v.venue_name, v.city_name, v.country_name, v.country_code, v.timezone, c.complex_name
    FROM Venues v
    JOIN Complexes c ON v.complex_id = c.complex_id
""")

# Sidebar filters
with st.sidebar:
    st.markdown('<div class="heading">Filters</div>', unsafe_allow_html=True)
    year = st.selectbox("Year", [2024], key="year_select")
    week = st.selectbox("Week", list(range(1, 53)), key="week_select")
    rank_range = st.slider("Rank Range", 1, 100, (1, 24), key="rank_slider")

# Apply filters
df_rankings = df_rankings[(df_rankings['rank'] >= rank_range[0]) & (df_rankings['rank'] <= rank_range[1])]

# Main content
st.markdown('<div class="heading">🎾 Tennis Rankings Explorer</div>', unsafe_allow_html=True)

# Rankings Section
st.markdown('<div class="subheading">Rankings</div>', unsafe_allow_html=True)
st.markdown('<div class="content-box">', unsafe_allow_html=True)
if not df_rankings.empty:
    st.dataframe(df_rankings)
else:
    st.warning("No rankings data available.")
st.markdown('</div>', unsafe_allow_html=True)

# Visualizations
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="subheading">Rankings Distribution</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    if not df_rankings.empty:
        fig = px.histogram(df_rankings, x='rank', title='Distribution of Rankings', color_discrete_sequence=['#3498db'])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for rankings distribution.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="subheading">Points Distribution</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    if not df_rankings.empty:
        fig = px.histogram(df_rankings, x='points', title='Distribution of Points', color_discrete_sequence=['#2ecc71'])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for points distribution.")
    st.markdown('</div>', unsafe_allow_html=True)

# Country-wise Stats
st.markdown('<div class="subheading">Country-wise Statistics</div>', unsafe_allow_html=True)
st.markdown('<div class="content-box">', unsafe_allow_html=True)
if not df_rankings.empty:
    country_df = df_rankings.groupby("country").agg(
        Competitors=('competitor_name', 'count'),
        Avg_Points=('points', 'mean')
    ).reset_index().sort_values(by='Competitors', ascending=False)
    fig = px.bar(country_df, x='country', y='Competitors', color='Avg_Points',
                 title='Competitors by Country', labels={'country': 'Country', 'Competitors': 'Number of Competitors'},
                 color_continuous_scale=px.colors.sequential.Viridis)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data available for country-wise stats.")
st.markdown('</div>', unsafe_allow_html=True)

# Additional Insights
st.markdown('<div class="subheading">Competitions Played vs Points</div>', unsafe_allow_html=True)
st.markdown('<div class="content-box">', unsafe_allow_html=True)
if not df_rankings.empty:
    fig = px.scatter(df_rankings, x='competitions_played', y='points', color='country',
                     title='Competitions Played vs Points', hover_name='competitor_name')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data available for competitions played vs points.")
st.markdown('</div>', unsafe_allow_html=True)

# Venues and Complexes Section
st.markdown('<div class="subheading">Venues and Complexes</div>', unsafe_allow_html=True)
st.markdown('<div class="content-box">', unsafe_allow_html=True)
if not df_venues.empty:
    st.dataframe(df_venues)
else:
    st.warning("No venues data available.")
st.markdown('</div>', unsafe_allow_html=True)

# Search Competitors Layout
left_column, right_column = st.columns([1, 2])
with left_column:
    st.markdown('<div class="subheading">Search Competitors</div>', unsafe_allow_html=True)
    competitor_name = st.text_input("Competitor Name", key="competitor_search")

with right_column:
    if competitor_name:
        competitor_data = df_rankings[df_rankings['competitor_name'].str.contains(competitor_name, case=False)]
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        if not competitor_data.empty:
            st.markdown(f'<div class="subheading">Details for {competitor_name}</div>', unsafe_allow_html=True)
            st.dataframe(competitor_data)
        else:
            st.warning("No data found for the specified competitor.")
        st.markdown('</div>', unsafe_allow_html=True)
