import streamlit as st


# Function for Lamini API configuration
def lamini_api_key_configuration():
    st.subheader("Lamini API Key:🔑")
    lamini_api_key = st.text_input("Enter your Lamini API Key:", type="password", value=st.session_state.lamini_api_key,
                                   help='Get API Key from: https://app.lamini.ai/account')
    if lamini_api_key == '':
        st.warning('Enter Lamini API Key ️')
        app_activation = False
    elif len(lamini_api_key) == 64:
        st.success('Lets Proceed!', icon='️👉')
        app_activation = True
    else:
        st.warning('Please enter the correct API Key 🗝️!', icon='⚠️')
        app_activation = False
    return lamini_api_key, app_activation


def display_footer():
    footer = """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            text-align: center;
            color: grey;
            padding: 10px 0;
        }
        </style>
        <div class="footer">
            Made with ❤️ by <a href="mailto:zeeshan.altaf@92labs.ai">Zeeshan</a>. 
        </div>
    """
    st.markdown(footer, unsafe_allow_html=True)


def get_data_lamini():
    data = [
        {
            "input": "Are there any step-by-step tutorials or walkthroughes available in the documentation?",
            "output": "Yes, there are step-by-step tutorials and walkthroughes available in the documentation section. "
                      "Here's an example for using Lamini to get insights into any python SDK: "
                      "https://lamini-ai.github.io/example/",
        },
        {
            "input": "Is the Lamini type system similar to a python type system?",
            "output": "Yes, the Lamini type system is built using Pydantic BaseModel.",
        },
        {
            "input": "Does Lamini have a limit on the number of API requests I can make?",
            "output": "Lamini provides each user with free tokens up front.",
        },
        {
            "input": "What does it mean to cancel a job using the `cancel_job()` function? Can we stop the machine from"
                     "doing its task?",
            "output": "The `cancel_job()` function is used to stop a tuning job that is currently running.",
        },
        {
            "input": "Can Lamini automatically handle hyperparameter tuning during the customization process? How does "
                     "it optimize the model for a specific use case?",
            "output": "Lamini is capable of automatically handling hyperparameter tuning during the model customization"
                      " process. It employs an intelligent algorithm to explore the hyperparameter space and find the "
                      "optimal combination of values. This is done through techniques such as heuristics, grid search, "
                      "random search, Bayesian optimization, or genetic algorithms. Lamini efficiently utilizes "
                      "computational resources to evaluate multiple model instances with different hyperparameter "
                      "configurations. It incorporates techniques like cross-validation to prevent overfitting and "
                      "ensure generalization. By automating hyperparameter tuning, Lamini streamlines the machine "
                      "learning workflow and improves the chances of developing high-performing models for specific "
                      "use cases.",
        },
        {
            "input": "Can you explain the CC-BY license mentioned? What does it allow me to do with the customized "
                     "language model?",
            "output": "Lamini allows for commercial use of their LLM technology under a permissive Apache 2.0 license "
                      "unless otherwise specified. You keep access and ownership of your own data, and we don't use "
                      "your data to tune models for anyone else but you. For more information, please reach out to "
                      "Lamini directly.",
        },
        {
            "input": "Can Lamini be used on a regular computer, or do I need specialized hardware or software?",
            "output": "Lamini can be used on a regular computer without any specialized hardware or software by using "
                      "the python client or REST APIs. It is designed to be easily accessible and user-friendly.  The "
                      "LLM Engine itself requires GPU accelerated servers capable of running large language models.  "
                      "Lamini hosts such machines that can be easily connected to, e.g. from a jupyter notebook or "
                      "python program.  Lamini also offers enterprise deployments of the LLM Engine on your "
                      "infrastructure.",
        },
        {
            "input": "Does Lamini require an internet connection to work, or can I use it offline?",
            "output": "Lamini requires an internet connection to work, as it is a cloud-based language model. "
                      "However, you can use it offline by downloading and running a local instance of the Lamini API. "
                      "To learn more about this deployment process, reach out to the Lamini team.",
        },
        {
            "input": "Can Lamini help me with tasks like translating text or answering questions, or is it focused on "
                     "generating text?",
            "output": "Lamini is primarily focused on generating text, and it can be used for tasks like "
                      "summarization and paraphrasing. Lamini can also be used to tune a LLM for tasks like "
                      "translation and question answering. You're talking to a model tuned using Lamini right "
                      "now!",
        },
        {
            "input": "What is Lamini? Is it like a robot or a computer program?",
            "output": "Lamini is a program for the execution of LLMs called a large language model engine. It is not "
                      "a robot, but rather a tool for building and executing LLMs.",
        },
        {
            "input": "Who is the Co-Founder of Lamini?",
            "output": "Sharon Zhou and Greg Diamos are the two Co-Founders of Lamini. Sharon is a Standford CS PhD in "
                      "Generative AI and awarded with MIT Technology Review 35 Under 35, for award-winning research "
                      "in generative AI. Greg is a PhD in Computer Engineering from Georgia Tech and has over 14,"
                      "000 citations in AI scaling laws and Tensor Cores."
                      "a robot, but rather a tool for building and executing LLMs.",
        },
        {
            "input": "Who is the CEO and CTO of Lamini?",
            "output": "Sharon Zhou is the CEO while Greg Diamos is the CTO of Lamini"
        },
    ]
    return data


def get_data_earnings_call():
    data = [
        {"question": "What is the expected contribution of N5 to TSMC's wafer revenue in 2021?",
         "answer": "The expected contribution of N5 to TSMC's wafer revenue in 2021 is around 20%."},
        {"question": "What percentage of TSMC's wafer revenue in 2021 is attributed to the N5 technology node?",
         "answer": "The expected contribution of N5 to TSMC's wafer revenue in 2021 is around 20%."},
        {"question": "What is the estimated proportion of N5-based wafer sales to TSMC's total wafer revenue "
                     "in 2021?",
         "answer": "The expected contribution of N5 to TSMC's wafer revenue in 2021 is around 20%."},
        {"question": "What is the expected share of N5 technology in TSMC's wafer revenue for the year 2021?",
         "answer": "The expected contribution of N5 to TSMC's wafer revenue in 2021 is around 20%."},
        {"question": "What is the approximate percentage of TSMC's wafer revenue in 2021 that can be "
                     "attributed to the N5 node?",
         "answer": "The expected contribution of N5 to TSMC's wafer revenue in 2021 is around 20%."},
        {"question": "What is TSMC expected full-year growth in U.S. dollar terms for 2022?",
         "answer": "TSMC's expected full-year growth in U.S. dollar terms for 2022 is mid-30%."},
        {"question": "What is TSMC's projected growth rate in U.S. dollar terms for the full year 2022?",
         "answer": "TSMC's expected full-year growth in U.S. dollar terms for 2022 is mid-30%."},
        {"question": "What is the expected percentage increase in TSMC's revenue in U.S. dollar terms for the "
                     "year 2022?",
         "answer": "TSMC's expected full-year growth in U.S. dollar terms for 2022 is mid-30%."},
        {"question": "What is the forecasted growth rate of TSMC's revenue in U.S. dollar terms for the full "
                     "year 2022?",
         "answer": "TSMC's expected full-year growth in U.S. dollar terms for 2022 is mid-30%."},
        {"question": "What is the anticipated percentage change in TSMC's revenue in U.S. dollar terms for the "
                     "year 2022?",
         "answer": "TSMC's expected full-year growth in U.S. dollar terms for 2022 is mid-30%."},
        {"question": "What is the expected production schedule for TSMC N4X?",
         "answer": "The expected production schedule for N4X is in the first half of 2023."},
        {"question": "When is TSMC planning to start mass-producing the N4X technology node?",
         "answer": "The expected production schedule for N4X is in the first half of 2023."},
        {"question": "What is the expected timeline for the commercial availability of N4X wafers from TSMC?",
         "answer": "The expected production schedule for N4X is in the first half of 2023."},
        {"question": "When is TSMC expected to begin volume production of N4X-based wafers?",
         "answer": "The expected production schedule for N4X is in the first half of 2023."},
        {"question": "What is the anticipated production window for N4X technology from TSMC?",
         "answer": "The expected production schedule for N4X is in the first half of 2023."},
        {"question": "What is TSMC forecast for foundry industry growth in 2021 in U.S. dollar terms?",
         "answer": "TSMC's forecast for the foundry industry growth in 2021 in U.S. dollar terms is around 16%."},
        {"question": "What is TSMC's predicted growth rate for the foundry industry in U.S. dollar terms for "
                     "the year"
                     "2021?",
         "answer": "TSMC's forecast for the foundry industry growth in 2021 in U.S. dollar terms is around 16%."},
        {"question": "What is the expected percentage increase in foundry industry revenue in U.S. dollar "
                     "terms for"
                     "2021, according to TSMC's forecast?",
         "answer": "TSMC's forecast for the foundry industry growth in 2021 in U.S. dollar terms is around 16%."},
        {"question": "What is TSMC's forecasted growth rate for the global foundry market in U.S. dollar terms "
                     "for the year 2021?",
         "answer": "TSMC's forecast for the foundry industry growth in 2021 in U.S. dollar terms is around 16%."},
        {"question": "What is the anticipated growth rate of the foundry industry in U.S. dollar terms for "
                     "2021, as predicted by TSMC?",
         "answer": "TSMC's forecast for the foundry industry growth in 2021 in U.S. dollar terms is around 16%."},
        {"question": "What is the breakdown of TSMC 2021 capital budget allocation by technology?",
         "answer": "The breakdown of TSMC's 2021 capital budget allocation by technology is as follows: 80% will "
                   "be allocated for advanced process technologies, including 3-nanometer, 5-nanometer, "
                   "and 7-nanometer. 10% will be spent for advanced packaging and mask making.\n* 10% will be "
                   "spent for specialty technologies."},
        {"question": "What percentage of TSMC's 2021 capital budget will be allocated to advanced process "
                     "technologies, including 3-nanometer, 5-nanometer, and 7-nanometer?",
         "answer": "The breakdown of TSMC's 2021 capital budget allocation by technology is as follows: 80% "
                   "will be allocated for advanced process technologies, including 3-nanometer, 5-nanometer, "
                   "and 7-nanometer. 10% will be spent for advanced packaging and mask making. 10% will "
                   "be spent for specialty technologies."},
        {"question": "How much of TSMC's 2021 capital budget will be dedicated to advanced packaging and mask "
                     "making?",
         "answer": "The breakdown of TSMC's 2021 capital budget allocation by technology is as follows: 80% "
                   "will be allocated for advanced process technologies, including 3-nanometer, 5-nanometer, "
                   "and 7-nanometer. 10% will be spent for advanced packaging and mask making. 10% will "
                   "be spent for specialty technologies."},
        {"question": "What proportion of TSMC's 2021 capital budget will be spent on specialty technologies?",
         "answer": "The breakdown of TSMC's 2021 capital budget allocation by technology is as follows: 80% will "
                   "be allocated for advanced process technologies, including 3-nanometer, 5-nanometer, "
                   "and 7-nanometer. 10% will be spent for advanced packaging and mask making. 10% will be "
                   "spent for specialty technologies."},
        {"question": "What percentage of TSMC's 2021 capital budget will be allocated to 3-nanometer, "
                     "5-nanometer, and 7-nanometer process technologies combined?",
         "answer": "The breakdown of TSMC's 2021 capital budget allocation by technology is as follows: 80% "
                   "will be allocated for advanced process technologies, including 3-nanometer, 5-nanometer, "
                   "and 7-nanometer. 10% will be spent for advanced packaging and mask making. 10% will "
                   "be spent for specialty technologies."},
        {"question": "What is the expected revenue growth rate for TSMC from 2020 to 2025 in U.S. dollar terms?",
         "answer": "The expected revenue growth rate for TSMC from 2020 to 2025 in U.S. dollar terms is between "
                   "10% to 15%."},
        {"question": "What is the projected annual growth rate of TSMC's revenue from 2020 to 2025, expressed "
                     "as a percentage?",
         "answer": "The expected revenue growth rate for TSMC from 2020 to 2025 in U.S. dollar terms is "
                   "between 10% to 15%."},
        {"question": "What is the estimated compound annual growth rate (CAGR) of TSMC's revenue from 2020 to "
                     "2025 in U.S. dollar terms?",
         "answer": "The expected revenue growth rate for TSMC from 2020 to 2025 in U.S. dollar terms is "
                   "between 10% to 15%."},
        {"question": "What is the range of expected revenue growth for TSMC from 2020 to 2025, in terms of "
                     "percentage increase per annum?",
         "answer": "The expected revenue growth rate for TSMC from 2020 to 2025 in U.S. dollar terms is "
                   "between 10% to 15%."},
        {"question": "What is the forecasted annual revenue growth rate for TSMC from 2020 to 2025, expressed "
                     "as a percentage, based on industry trends and analyst estimates?",
         "answer": "The expected revenue growth rate for TSMC from 2020 to 2025 in U.S. dollar terms is "
                   "between 10% to 15%."},
        {"question": "What was TSMC revenue in US dollar terms in 2019?",
         "answer": "TSMC's revenue in US dollar terms in 2019 was USD 34.6 billion."},
        {"question": "What was TSMC revenue in US dollar terms for the year 2019?",
         "answer": "TSMC's revenue in US dollar terms in 2019 was USD 34.6 billion."},
        {"question": "What was TSMC total revenue in US dollars for the calendar year 2019?",
         "answer": "TSMC's revenue in US dollar terms in 2019 was USD 34.6 billion."},
        {"question": "What was TSMC annual revenue in US dollars for the year ending December 31, 2019?",
         "answer": "TSMC's revenue in US dollar terms in 2019 was USD 34.6 billion."},
        {"question": "What was TSMC revenue in US dollar terms for the fiscal year 2019?",
         "answer": "TSMC's revenue in US dollar terms in 2019 was USD 34.6 billion."},
        {"question": "What is the expected revenue growth for TSMC in 2022-Q2 in U.S. dollar terms?",
         "answer": "The expected revenue growth for TSMC in 2022-Q2 in U.S. dollar terms is 35%."},
        {"question": "What is the projected annual growth rate of Taiwan Semiconductor Manufacturing Company's "
                     "(TSMC) revenue from 2020 to 2025, assuming a moderate growth scenario?",
         "answer": "The expected revenue growth for TSMC in 2022-Q2 in U.S. dollar terms is 35%."},
        {"question": "What is the estimated compound annual growth rate (CAGR) of TSMC's revenue from 2020 to "
                     "2025, considering the company's historical growth trends and industry developments?",
         "answer": "The expected revenue growth for TSMC in 2022-Q2 in U.S. dollar terms is 35%."},
        {"question": "What is the range of possible revenue growth rates for TSMC from 2020 to 2025, based on "
                     "analyst forecasts and industry reports?",
         "answer": "The expected revenue growth for TSMC in 2022-Q2 in U.S. dollar terms is 35%."},
        {"question": "What is the expected average annual growth rate of TSMC's revenue from 2020 to 2025, "
                     "considering the company's strategic initiatives, market trends, and competitive "
                     "landscape?",
         "answer": "The expected revenue growth for TSMC in 2022-Q2 in U.S. dollar terms is 35%."},
        {"question": "What is the expected power improvement at the same speed for N2 compared to TSMC N3e?",
         "answer": "The expected power improvement at the same speed for N2 compared to N3e is 20% to 30%."},
        {"question": "What is the estimated percentage increase in power efficiency that can be achieved by "
                     "using N2 technology compared to N3e, assuming the same operating speed?",
         "answer": "The expected power improvement at the same speed for N2 compared to N3e is 20% to 30%."},
        {"question": "What is the expected power reduction percentage for N2 technology compared to N3e, "
                     "assuming the same clock speed?",
         "answer": "The expected power improvement at the same speed for N2 compared to N3e is 20% to 30%."},
        {"question": "What is the power improvement range that can be expected when transitioning from N3e to "
                     "N2 technology, measured as a percentage of the original power consumption at the same "
                     "clock speed?",
         "answer": "The expected power improvement at the same speed for N2 compared to N3e is 20% to 30%."},
        {"question": "What is the estimated power savings percentage that can be achieved by using N2 "
                     "technology compared to N3e, assuming the same operating frequency?",
         "answer": "The expected power improvement at the same speed for N2 compared to N3e is 20% to 30%."},
        {"question": "What is TSMC expected foundry industry growth for the full year of 2022?",
         "answer": "TSMC's expected foundry industry growth for the full year of 2022 is forecast to be close to "
                   "20%."},
        {"question": "What is TSMC annual growth rate for full year 2022 based on current market trends and "
                     "forecasts?",
         "answer": "TSMC's expected foundry industry growth for the full year of 2022 is forecast to be close "
                   "to 20%."},
        {"question": "What is the expected annual growth rate for the global foundry market, with TSMC being a "
                     "major player, for the year 2022, according to industry analysts and research firms?",
         "answer": "TSMC's expected foundry industry growth for the full year of 2022 is forecast to be close "
                   "to 20%."},
        {"question": "What is the forecasted growth rate for the semiconductor foundry industry, with TSMC "
                     "being a key player, for the full year 2022, considering the current market conditions "
                     "and demand trends?",
         "answer": "TSMC's expected foundry industry growth for the full year of 2022 is forecast to be close "
                   "to 20%."},
        {"question": "What is the estimated growth rate for the foundry industry, driven by TSMC and other "
                     "major players, for the year 2022, based on industry reports and market research?",
         "answer": "TSMC's expected foundry industry growth for the full year of 2022 is forecast to be close "
                   "to 20%."}
    ]
    return data
