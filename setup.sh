mkdir -p ~/.streamlit 
echo "[server]
headless = true
port = $PORT
enableCORS = false
[theme]
base=\"light\"
primaryColor=\"#207d0c\"

" > ~/.streamlit/config.toml