install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

run:
	streamlit run ./the_erni_dojo/st_poc.py

all: install run