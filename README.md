# 📱 SIM Deal Auditor

Automated SIM-only deal scraper across **uSwitch**, **MoneySuperMarket**, and **CompareTheMarket**.  
Outputs a colour-coded Excel file matching your audit format.

---

## 🚀 Deploy to Streamlit Cloud (Free, ~10 minutes)

### Step 1 — Create a GitHub account
Go to [github.com](https://github.com) and sign up for a free account if you don't have one.

### Step 2 — Create a new repository
1. Click the **+** icon (top right) → **New repository**
2. Name it `sim-deal-auditor`
3. Set it to **Public**
4. Click **Create repository**

### Step 3 — Upload the files
1. In your new repo, click **Add file** → **Upload files**
2. Upload ALL files from this folder:
   - `app.py`
   - `requirements.txt`
   - `packages.txt`
   - `install_browsers.py`
3. Also create the folder `.streamlit/` and upload `config.toml` inside it
4. Click **Commit changes**

### Step 4 — Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **New app**
4. Select your `sim-deal-auditor` repository
5. Main file path: `app.py`
6. Click **Deploy**

✅ You'll get a public URL like `https://yourname-sim-deal-auditor.streamlit.app`  
Bookmark it — that's your tool, usable from any browser, any device.

---

## 🖥️ How to use the app

1. **Select contract lengths** — 1M, 12M, 24M (or all three)
2. **Set price range** — e.g. £5 to £20
3. Click **Start Audit**
4. The app visits each site with a real browser, extracts deals, and builds the table
5. Click **Download Excel** — file matches your colour-coded format

---

## 📊 Excel Output Format

- One sheet per contract length (1M Market, 12M Market, 24M Market)
- Three side-by-side tables: uSwitch | MoneySuperMarket | CompareTheMarket
- Rows = price points (£5–£20)
- Columns = networks (Three, Vodafone, SMARTY, TalkMobile, VOXI, iD Mobile, Lebara, GiffGaff, Spusu, O2, Sky)
- **Green** = best data value at that price point
- **Amber** = mid-range
- **Red** = worst value
- **Unlimited** = always green

---

## ⚠️ Known limitations

- Sites with heavy anti-bot protection may return partial data on some runs
- If a site changes its page structure, the scraper may need updating
- Streamlit Community Cloud has a ~1GB memory limit — large scrapes may need the paid tier

---

## 🔄 Updating the app

To update: edit the files in GitHub → Streamlit Cloud auto-redeploys within ~2 minutes.
