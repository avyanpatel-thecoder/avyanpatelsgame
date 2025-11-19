import streamlit as st
import runpy
import os

st.set_page_config(page_title="Avyan Patel's Game", layout="centered")
st.title("Avyan Patel's Game")

root = os.path.dirname(__file__)

# Only consider Python files. Never attempt to execute non-.py files (your repo contains a React/JSX file named 'game code').
# This wrapper is intentionally conservative and will show an instructional message if no .py app is found.
candidates = ["streamlit_app.py", "game_code.py", "app.py", "main.py"]
found = None
for name in candidates:
    p = os.path.join(root, name)
    if os.path.exists(p) and p.endswith('.py'):
        found = p
        break

if not found:
    st.error(
        "No Python Streamlit app found. I detected non-Python files (for example a React file named 'game code').\n\n"
        "If your app is React/JSX, host it separately (Vercel/Netlify) and embed it into Streamlit via st.components.v1.iframe, or convert the UI to Python/Streamlit.\n\n"
        "To proceed with Streamlit, add a Python file (e.g., game_code.py) that builds the UI with Streamlit and re-deploy."
    )
else:
    st.write("Running game script: {}".format(os.path.basename(found)))
    try:
        runpy.run_path(found, run_name='__main__')
    except Exception as e:
        st.error("Failed to run {}: {}".format(found, e))

# Notes:
# - This wrapper will not execute JS/JSX files. The file 'game code' in your repo appears to be a React component (JSX) and contains emoji characters that are invalid in Python source.
# - I created a separate game.jsx file (copy of your original) so the React source is preserved with a proper extension. Host that React app separately or convert to Python.