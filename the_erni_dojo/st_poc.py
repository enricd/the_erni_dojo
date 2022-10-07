import streamlit as st


def main():

    st.set_page_config(
        page_title="ERNI Dojo (PoC)",
        page_icon="👾",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            #'Get Help': 'https://www.extremelycoolapp.com/help',
            #'Report a bug': "enric.domingo@betterask.erni",
            'About': "POC concept of the ERNI Dojo platform where ERNIans compete, practice and learn programming game bots!"
        }
    )

    st.title("(PoC) The ERNI Dojo 👨‍💻🎮👾")

    cols = st.columns((3,1,3))
    with cols[0]:
        agent1_file = st.file_uploader("Player1 Agent (.py)", type=[".py"])
    with cols[2]:
        agent2_file = st.file_uploader("Player2 Agent (.py)", type=[".py"])
    
    cols1 = st.columns((2,4,2))
    with cols1[1]:
        is_play = st.button("Hajime!")

        img_placeholder = st.empty()
        if is_play:
            img_placeholder.image(".\images\Placeholder_view_vector.svg.png", use_column_width=True)


if __name__ == "__main__":
    main()