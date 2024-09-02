import streamlit as st
import lamini
from lamini import Lamini
import pandas as pd
from util import *

# Define session state variables
if "data" not in st.session_state:
    st.session_state.data = None
if "model" not in st.session_state:
    st.session_state.model = ''
if "learning_rate" not in st.session_state:
    st.session_state.learning_rate = None
if "max_steps" not in st.session_state:
    st.session_state.max_steps = None
if "optimizer" not in st.session_state:
    st.session_state.optimizer = None
if "app_activation" not in st.session_state:
    st.session_state.app_activation = False
if "lamini_api_key" not in st.session_state:
    st.session_state.lamini_api_key = ''

# Initialize streamlit app
page_title = "FineTune Lab"
page_icon = "🔧"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# --- MAIN PAGE CONFIGURATION ---
st.title(page_title)
st.write(':blue[***Shape the Future of AI with Precision Tuning 🔧✨Powered by Lamini✨***]')
st.write("FineTune Lab empowers you to fine-tune Large Language Models with your specific data, creating highly "
         "customized and accurate AI solutions. Whether you’re optimizing for niche applications 🎯 or refining "
         "general models 🔄, our solution offers a seamless and efficient way to enhance the capabilities of your "
         "LLMs. 🤖✨")

if st.session_state.app_activation:
    api_configuration_status = '✔️'
    info_message = 'Above parameters can be changed from Configuration page'
else:
    api_configuration_status = '❌'
    info_message = 'Configure the API from Configuration page before proceeding'

# Data frame to store the application configuration settings
df = pd.DataFrame({
    'API Configuration': api_configuration_status,
    'LLM': [st.session_state.model],
    'Learning Rate': [st.session_state.learning_rate],
    'Maximum Training Steps': [st.session_state.max_steps],
    'Optimizer': [st.session_state.optimizer]
})

# Display the selected configuration settings
st.subheader('Selected Configuration:')
st.dataframe(df, hide_index=True, use_container_width=True)
st.info(info_message, icon='ℹ️')

# Loading the specific data set for model fine-tuning
st.subheader('Load Your Specific Data:')
st.write('Click on the below button to load the specific data from repository')
load_data_button = st.button('Load Data', type='primary', disabled=not st.session_state.app_activation)
if load_data_button:
    st.session_state.data = get_data()
    st.toast('Data Loaded Successfully!', icon='🎉')

# Proceed to model fine-tuning only if data is loaded successfully
if st.session_state.data is not None:
    st.subheader('Loaded Data:')
    with st.expander('Data'):
        st.write(st.session_state.data)
    st.subheader('Model Fine Tuning:')
    st.write('Click the below button to start fine tuning the LLM')
    fine_tune_button = st.button('Start Finetuning', type='primary', disabled=not st.session_state.app_activation)
    if fine_tune_button:
        lamini.api_key = st.session_state.lamini_api_key
        llm = Lamini(st.session_state.model)
        llm.tune(data_or_dataset_id=st.session_state.data,
                 finetune_args={'learning_rate': st.session_state.learning_rate,
                                'max_steps': st.session_state.max_steps,
                                'optim': st.session_state.optimizer})
        st.info('Tuning job submitted. Check job status at: https://app.lamini.ai/tune')
