import lamini
import streamlit
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
if "job_status" not in st.session_state:
    st.session_state.job_status = ''
if "fine_tuning_start" not in st.session_state:
    st.session_state.fine_tuning_start = False

# Initialize streamlit app
page_title = "FineTune Lab"
page_icon = "🔧"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

lamini.api_key = st.session_state.lamini_api_key
llm = Lamini(st.session_state.model)

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
df_config = pd.DataFrame({
    'API Configuration': api_configuration_status,
    'LLM': [st.session_state.model],
    'Learning Rate': [st.session_state.learning_rate],
    'Maximum Training Steps': [st.session_state.max_steps],
    'Optimizer': [st.session_state.optimizer]
})

# Display the selected configuration settings
st.subheader('Selected Configuration:')
st.dataframe(df_config, hide_index=True, use_container_width=True)
st.info(info_message, icon='ℹ️')

# Loading the sample data set for model fine-tuning
st.subheader('Load the Sample Data:')
st.write('Click on the appropriate button to load the sample data')
col1, col2 = st.columns(2)
with col1:
    load_data_button_lamini = st.button('Lamini Sample Data', disabled=not st.session_state.app_activation)
    if load_data_button_lamini:
        st.session_state.data = get_data_lamini()
        st.toast('Lamini Sample Data Loaded Successfully!', icon='🎉')
with col2:
    load_data_button_earning_call = st.button('Earning Call Sample Data', disabled=not st.session_state.app_activation)
    if load_data_button_earning_call:
        st.session_state.data = get_data_earnings_call()
        st.toast('Earnings Call Sample Data Loaded Successfully!', icon='🎉')

# Proceed to model fine-tuning only if data is loaded successfully
if st.session_state.data is not None:
    st.subheader('Loaded Data:')
    with st.expander('Data'):
        st.write(st.session_state.data)
    st.subheader('Model Fine Tuning:')
    st.write('Click the below button to start fine tuning the LLM')
    fine_tune_button = st.button('Start Finetuning', type='primary', disabled=not st.session_state.app_activation)
    if fine_tune_button:
        st.session_state.job_status = llm.tune(data_or_dataset_id=st.session_state.data,
                          finetune_args={'learning_rate': st.session_state.learning_rate,
                                         'max_steps': st.session_state.max_steps,
                                         'optim': st.session_state.optimizer})
        st.session_state.fine_tuning_start = True
        st.info('Tuning job submitted.')

    # Status of fine tuning job should be shown only when Fine tuning process has been started
    if st.session_state.fine_tuning_start:
        streamlit.subheader('Status:')

        # Get the status of all fine tuning jobs however display the status of most recent job only
        all_jobs_status = llm.get_jobs()
        job_link = f"https://app.lamini.ai/tune/{all_jobs_status[0]['job_id']}"
        job_status = all_jobs_status[0]['status']
        job_id = all_jobs_status[0]['job_id']

        # Data frame to store the LLM fine tuning job status
        df_job_status = pd.DataFrame({
            'Job ID': [job_id],
            'Job Status': [job_status],
            'Job Link': [job_link]
        })

        st.dataframe(df_job_status, column_config={
           "Job Link": st.column_config.LinkColumn("Job Link", display_text=job_link),
        }, hide_index=True, use_container_width=True)
