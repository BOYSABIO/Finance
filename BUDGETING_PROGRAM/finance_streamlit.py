import streamlit as st 

# Page Config 
st.set_page_config(
    page_title = "Finance Application",
    page_icon = "⚉",
    layout = "wide"
)

# Tab Organization
home_tab, Budgeting_money_check, Rebalancing_tab = st.tabs(['Home', 'Budgeting', 'Rebalancing'])

with home_tab:
    st.title("Finance Application")
    st.subheader("Here is a subheader if needed")
    st.write("Here is text")
    st.text("Here is text")

with Budgeting_money_check:
    st.title("General")
    st.subheader("Here is a subheader if needed")
    st.write("Here is text")
    st.text("Here is text")

with Rebalancing_tab:
    st.title("Rebalancing")
