import streamlit as st
from streamlit_ace import st_ace


def page03_code():
    
    st.header("👩‍💻 Code your agent! 👨‍💻")

    cols = st.columns(2)

    start_template = """def agent(obs, config):

    # --- logic of your agent here: ---

    actions = config.actions
    next_action = actions.UP

    # ---------------------------------

    # always return one of the possible obs.actions
    return next_action
    """

    with cols[0]:
        code = st_ace(
            value=start_template, 
            language="python", 
            theme="chaos",
            min_lines=30,
            )

    with cols[1]:
        st.markdown("``` python\n" + code)