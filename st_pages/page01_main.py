import streamlit as st
from pathlib import Path


def p01_main():

    st.markdown("""
                <style>
                    [class="css-1fv8s86 e16nr0p33"] {
                        max-width: 1000px;
                        margin-left: auto;
                        margin-right: auto;
                    }
                </style>""",
                unsafe_allow_html=True
    )

    st.markdown("#")

    st.markdown((Path(__file__).parents[1]/"README.md").read_text("utf-8"),
        unsafe_allow_html=True
        )


if __name__ == "__main__":
    p01_main()