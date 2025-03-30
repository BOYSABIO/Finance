import streamlit as st 

# Page Config 
st.set_page_config(
    page_title = "Finance Application",
    page_icon = "⚉",
    layout = "wide"
)

# Tab Organization
home_tab, General_tab, Money_tab, Rebalancing_tab = st.tabs(['Home', 'General', 'Money', 'Rebalancing'])

with home_tab:
    st.title("Finance Application")
    st.subheader("Here is a subheader if needed")
    st.write("Here is text")
    st.text("Here is text")

with General_tab:
    st.title("General")
    st.subheader("Here is a subheader if needed")
    st.write("Here is text")
    st.text("Here is text")

with Money_tab:
    st.title("Money")

with Rebalancing_tab:
    st.title("Rebalancing")


