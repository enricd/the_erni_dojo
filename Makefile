install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
run:
	streamlit run st_poc.py

all: install run