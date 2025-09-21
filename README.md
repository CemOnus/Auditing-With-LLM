# LLM Auditing – Digital Flipbook (Streamlit)

This Streamlit app renders **Using Large Language Models in Auditing with a Risk Perspective** as an interactive, page‑flip digital book right in the browser using **pdf.js** and **turn.js**.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud
1. Create a new GitHub repo and upload these files.
2. Go to Streamlit Community Cloud and choose the repo + `app.py`.
3. Click Deploy.

No server storage is needed — the PDF is embedded (base64) inside the app for fast loading.

## Folder structure
```
llm-audit-flipbook/
├─ app.py
├─ requirements.txt
├─ assets/
│  └─ Using Large Language Models in Auditing with a Risk Perspective.pdf
└─ README.md
```
