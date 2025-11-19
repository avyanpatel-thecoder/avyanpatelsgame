import streamlit as st
import runpy
import os

st.set_page_config(page_title="Avyan Patel's Game", layout="centered")
st.title("Avyan Patel's Game")

root = os.path.dirname(__file__)
# Likely filenames to check for your existing game script
candidates = ["game_code.py", "game code.py", "game code", "app.py", "main.py"]
found = None
for name in candidates:
    p = os.path.join(root, name)
    if os.path.exists(p):
        found = p
        break

if not found:
    st.error("Could not find your game script in the repository. Checked: " + ", ".join(candidates) + ". Please rename your file (avoid spaces) or update streamlit_app.py to point to the correct path.")
else:
    st.write(f"Running game script: {os.path.basename(found)}")
    try:
        if found.endswith('.py'):
            runpy.run_path(found, run_name='__main__')
        else:
            with open(found, 'r', encoding='utf-8') as f:
                source = f.read()
            exec(compile(source, found, 'exec'), {})
    except Exception as e:
        st.error(f"Failed to run {found}: {e}")

# NOTE: If your game defines a function to start the Streamlit UI (e.g., main()),
# you can instead import that function and call it explicitly for better integration.