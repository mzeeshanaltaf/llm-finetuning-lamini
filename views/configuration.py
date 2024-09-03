import streamlit as st
from util import *

lamini_supported_models = {'Llama 3.1': 'meta-llama/Meta-Llama-3.1-8B-Instruct',
                           'Mistral 3': 'mistralai/Mistral-7B-Instruct-v0.3',
                           'Phi-3': 'microsoft/Phi-3-mini-4k-instruct',
                           'Qwen 2': 'Qwen/Qwen2-7B-Instruct'}
# SIDEBAR CONFIGURATION
st.title("Configuration")

st.session_state.lamini_api_key, st.session_state.app_activation = lamini_api_key_configuration()

# Select the model to fine tune
st.subheader('Select LLM:')
model = st.selectbox('Select the LLM to Fine Tune', ('Llama 3.1', 'Mistral 3', 'Phi-3', 'Qwen 2'),
                     disabled=not st.session_state.app_activation)
st.session_state.model = lamini_supported_models[model]

# Select the hyperparameters for tuning
st.subheader('Hyper Parameter Tuning:')
st.session_state.learning_rate = st.slider('Select the learning rate:', 0.0001, 0.0009, 0.0001, 0.0001, format='%f',
                                           disabled=not st.session_state.app_activation)
st.session_state.max_steps = st.slider('Total number of training steps to perform:', 50, 300, 100, 50, format='%d',
                                       disabled=not st.session_state.app_activation)
st.session_state.optimizer = st.selectbox('Select the optimizer to use', ('adafactor', 'adamw_hf', 'adamw_torch',
                                                                          'adamw_torch_fused', 'adamw_apex_fused',
                                                                          'adamw_anyprecision'),
                                          disabled=not st.session_state.app_activation)
