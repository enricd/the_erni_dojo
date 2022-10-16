import streamlit as st
from pathlib import Path
import os
import sys
from time import sleep
from PIL import Image

from st_pages import p01_main, \
                    p02_instructions, \
                    p03_code, \
                    p04_test, \
                    p05_submit, \
                    p06_leaderboard, \
                    under_construction

#from src.game_engine import game_engine


def main():

    st.set_page_config(
        page_title="The ERNI Dojo",
        page_icon="👾",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            #'Get Help': 'https://www.extremelycoolapp.com/help',
            #'Report a bug': "enric.domingo@betterask.erni",
            'About': "POC concept of The ERNI Dojo platform where ERNIans compete, practice and learn programming game bots!"
        }
    )

    # TODO:
    # --- Pages ---:
    #  1. Main/Landing (later add more games and expose them here, also login funcs and user management)
    #  2. Instructions
    #  3. Code your agent
    #  4. Test your agent  [IN PROGRESS]
    #  5. Submit and manage your agents
    #  6. General ranking

    # st.markdown(""" <h1 style='text-align:center'> 👩‍💻🤖🎮👾 <i>The</i> ERNI <i>Dojo</i> 👾🎮🤖👨‍💻 </h1>  

    st.markdown("""<style>
                    [data-testid=stImage] {
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                    }

                    [data-baseweb=tab] {
                        font-size: 20px;
                        padding: 0px 5px;
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                    }
                </style>""",
                unsafe_allow_html=True
    )

    st.image("./images/the_erni_dojo_logo_dark.png", width=600)

    st.markdown("""<h3 style='text-align:center'> Prove of Concept </h3>
    </br>""", unsafe_allow_html=True)

    tabs = st.tabs(["Main ✅", 
                    "Instructions 🏗️", 
                    "Code 🏗️",     # streamlit-ace
                    "Test ✅",
                    "Submit 🏗️",
                    "Leaderboard 🏗️"
                    ])

    with tabs[0]:
        p01_main()
    
    with tabs[1]:
        under_construction()

    with tabs[2]:
        p03_code()

    with tabs[3]:
        p04_test()

    with tabs[4]:
        under_construction()

    with tabs[5]:
        under_construction()



if __name__ == "__main__":
    main()