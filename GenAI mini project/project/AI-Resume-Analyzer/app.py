import json
import os

import streamlit as st

from dotenv import load_dotenv
from docx import Document
from pypdf import PdfReader

from openai import OpenAI

#load .env variable
load_dotenv()

API_KEY=os.getenv("OPENAI_API_KEY")
MODEL=os.getenv("OPENAI_MODEL")
