# MarginIQ v5 — Enterprise AI Pricing Committee
### Streamlit Deployment Package

---

## Files in this folder

```
marginiq-deploy/
├── app.py              ← Main Streamlit entry point
├── marginiq.html       ← Full MarginIQ prototype (4 agents, 50 suppliers)
├── requirements.txt    ← Python dependencies
├── .streamlit/
│   └── config.toml     ← Theme + server settings
└── README.md           ← This file
```

---

## Option 1 — Run Locally (Fastest, for demo day)

```bash
# Step 1: Install streamlit (only needed once)
pip install streamlit

# Step 2: Navigate into this folder
cd marginiq-deploy

# Step 3: Run
streamlit run app.py
```

Then open your browser at: **http://localhost:8501**

---

## Option 2 — Deploy on Streamlit Cloud (Free, Shareable URL)

1. Create a free account at **https://share.streamlit.io**
2. Push this entire folder to a **GitHub repository** (public or private)
3. Go to share.streamlit.io → **New App**
4. Select your repo, branch `main`, file `app.py`
5. Click **Deploy**
6. In ~60 seconds you get a shareable URL like:
   `https://yourname-marginiq.streamlit.app`

---

## Option 3 — Deploy on Hugging Face Spaces (Free)

1. Create account at **huggingface.co**
2. New Space → SDK: **Streamlit**
3. Upload all files from this folder
4. Space auto-deploys and gives public URL

---

## Troubleshooting

| Problem | Fix |
|---|---|
| "marginiq.html not found" | Make sure `marginiq.html` is in the **same folder** as `app.py` |
| Blank white screen | Refresh browser, clear cache |
| App too small / cut off | Increase `height=900` in app.py to `1000` or `1080` |
| Fonts not loading | Needs internet connection (Google Fonts CDN) |
