import streamlit as st
import pandas as pd


st.header('one')

from oauth import authorize_creds
#creds = 'client_secrets.json'
creds = 'GSCTatieLouCredentialsNonLegacy.json'
webmasters_service = authorize_creds(creds)


