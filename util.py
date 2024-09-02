import streamlit as st


# Function for Lamini API configuration
def lamini_api_key_configuration():
    st.subheader("Lamini API Key:🔑")
    lamini_api_key = st.text_input("Enter your Lamini API Key:", type="password",
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


def get_data():
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
