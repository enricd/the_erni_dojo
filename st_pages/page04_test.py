from time import sleep
from pathlib import Path
import os
import streamlit as st
from PIL import Image


def p04_test():

    st.markdown("""
                <style>
                    [class="css-k3w14i effi0qh3"] {
                        font-size: 18px;
                    }
                </style>""",
                unsafe_allow_html=True
    )

    st.write("⚠️ NOTE: Logic is still not fully implemented!! ⚠️")

    cols = st.columns((3,1,3))
    with cols[0]:
        agent1_file = st.file_uploader("⬆️📄 Upload Player1 Agent (.py)", type=[".py"])
        #print(agent1_file)
        if not agent1_file:
            demo_agent1_file = st.selectbox("Or select a demo Agent here...", ("", "bot_agent", "random_agent", "test_agent"), key=1, disabled=(agent1_file is not None))
    with cols[1]:
        st.markdown("<h1 style='text-align:center'> - vs - </h1>", unsafe_allow_html=True)
    with cols[2]:
        agent2_file = st.file_uploader("⬆️📄 Upload Player2 Agent (.py)", type=[".py"])
        demo_agent2_file = st.selectbox("Or select a demo Agent here...", ("", "bot_agent", "random_agent", "test_agent"), key=2)
    
    cols1 = st.columns((3,4,3))
    with cols1[1]:
        start_status = st.empty()
        img_placeholder = st.image("./images/cyberpunk_dojo_placeholder_564.png", use_column_width=True)

        if not (agent1_file or demo_agent1_file) and not (agent2_file or demo_agent2_file):
            start_status.write("Waiting for Player1 and Player2...")
        elif not (agent1_file or demo_agent1_file):
            start_status.write("Waiting for Player1...")
        elif not (agent2_file or demo_agent2_file):
            start_status.write("Waiting for Player2...")
        else:
            is_play = start_status.button("▶️"+" "+"Hajime!")

            if is_play:
                play_id = 0
                #game_engine(play_id=play_id)

                game_plays_folder = Path(f"./game_plays/play_{play_id:0>4d}")
                imgs_paths = [img for img in os.listdir(game_plays_folder)]
                imgs = [Image.open(game_plays_folder / img_path) for img_path in imgs_paths]

                for img in imgs:
                    img_placeholder.image(img, use_column_width=True)
                    sleep(0.3)