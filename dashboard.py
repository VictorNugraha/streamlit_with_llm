import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_book as stb

stb.set_book_config(
                     menu_title="Features",
                     menu_icon="",
                     options=[
                            "Home",
                            "PDF Summarizer",
                            "PDF QnA"
                            ], 
                     paths=[
                            "menu/home", 
                            "menu/summarizer", 
                            "menu/qna"
                            ],
                     icons=[
                            "house",
                            "book",
                            "question",
                            ],
                     )