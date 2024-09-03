import streamlit as st

st.subheader('About')
with st.expander('Application'):
    st.markdown(''' Fine Tune Large Language Models with your specific data''')
with st.expander('Technologies Used'):
    st.markdown(''' 
    * Lamini -- Fine Tuning of LLMs 
    * Supported LLMs for fine tuning:
        * Llama 3.1
        * Mistral v3
        * Phi 3
        * Qwen 2
    * Streamlit -- For application Front End
    ''')
with st.expander('Contact'):
    st.markdown(''' Any Queries: Contact [Zeeshan Altaf](mailto:zeeshan.altaf@92labs.ai)''')
with st.expander('Source Code'):
    st.markdown(''' Source code: [GitHub](https://github.com/mzeeshanaltaf/llm-finetuning-lamini)''')
