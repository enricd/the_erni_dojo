import numpy as np
import pandas as pd
from time import time, sleep
from datetime import datetime
from pathlib import Path
import os
import streamlit as st
from fnmatch import fnmatch
from io import StringIO


def main():
    
    st.set_page_config(
        page_title = "ALFRED Problems",
        page_icon = "🧪",
        layout = "wide",
        initial_sidebar_state = "auto"
    )
    
    st.title("Testing Streamlit features")
    
    file = st.file_uploader("Upload a file:")
    print(file)
    print(type(file))
    
    if file:
        # bytes_data = StringIO(file.getvalue().decode("utf-8"))
        # st.write("filename:", file.name)
        # st.write(bytes_data)
        
        #exec(file.read())
        with open("./files/file.py", "wb") as f:
            f.write(file.getbuffer())
            
        from files.file import demo_func
        
        st.write(demo_func(2, 3))
            
               
if __name__ == "__main__":
    
    main()