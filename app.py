# Import libraries
import streamlit as st

# --- PAGE SETUP ---
finetune_page = st.Page(
    "views/fine_tuning.py",
    title="Fine Tuning",
    icon=":material/discover_tune:",
    default=True,
)

config_page = st.Page(
    "views/configuration.py",
    title="Configuration",
    icon=":material/toggle_on:",
)


about_page = st.Page(
    "views/about.py",
    title="About",
    icon=":material/info:",
)

pg = st.navigation({
    "Admin": [config_page],
    "Home": [finetune_page],
    "About": [about_page],
                    })

pg.run()
