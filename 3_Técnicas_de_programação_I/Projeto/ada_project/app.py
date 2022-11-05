
import numpy as np
import pandas as pd  
import plotly.express as px 
import streamlit as st  
st.set_page_config(
    page_title="Ada project dashboard",
    page_icon="✅",
    layout="wide",
)

df_month_revenue = pd.read_csv('df_month_revenue.csv')
df_all_sells = pd.read_csv('df_all_sells.csv')
df_consolidate = pd.read_csv('df_consolidate.csv')

# dashboard title
st.title("Ada project dashboard")

# top-level filters

# creating a single-element container
placeholder = st.empty()

# near real-time / live feed simulation

sells = df_all_sells.shape[0]
# creating KPIs
balance = np.sum(df_month_revenue['balance'])


with placeholder.container():

    # create three columns
    kpi1, kpi2, kpi3 = st.columns(3)

    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="Sellings ⏳",
        value=round(sells),
        delta=round(sells) - 10,
    )
    
    kpi2.metric(
        label="Months ",
        value=int(sells),
        delta=-10 + sells,
    )
    
    kpi3.metric(
        label="Balance ＄",
        value=f"$ {round(balance,2)} ",
        delta=-round(balance) * 100,
    )

    # create two columns for charts
    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        st.markdown("### First Chart")
        
        sum_balance = np.sum(df_consolidate['balance'])
        df_consolidate.loc[df_consolidate['balance'] < 0.05*sum_balance, 'product'] = 'Other' # Represent only large countries
        fig = px.pie(df_consolidate, names='product', values='balance', title='Product balance')
        st.write(fig)
        
    with fig_col2:
        st.markdown("### Second Chart")
        _filter = st.selectbox("Select the product", df_month_revenue.columns)

        fig2 = px.line(data_frame=df_month_revenue, y=_filter, x='date', markers=True)
        st.write(fig2)

    st.markdown("### Detailed Data View")
    st.dataframe(df_month_revenue)
    