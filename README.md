# 🧭 The New Financial System — Explained (Streamlit App)

An interactive **Streamlit app** that teaches the fundamentals of **Blockchain**, **Consensus Mechanisms**, and **Tokenised Real-World Assets (RWAs)**.  
Learn by doing — add transactions to a blockchain, try mining, fractionalise assets, and test your knowledge with a quick quiz.

---

## 🚀 Features
- 🏗️ **Blockchain Basics** — add transactions, mine blocks, and see how tampering breaks the chain.  
- ⛏️ **Consensus Playground** — adjust Proof-of-Work difficulty and feel why rewriting history is hard.  
- 🏠 **RWA Tokenisation Demo** — fractionalise a property/treasury bill, calculate yields, and explore liquidity scenarios.  
- ⚠️ **Risks & Reality** — understand common risks (custody, regulation, liquidity).  
- 🧪 **Quick Quiz** — check your understanding with instant feedback.  
- 📖 **Glossary** — plain-English definitions of blockchain and finance terms.  

---

## 📁 Project Structure
rwa-edu/
├─ app.py # Home / overview
├─ requirements.txt # Dependencies
├─ .gitignore # Ignore venv, cache, logs
├─ README.md # Project documentation
├─ pages/
│ ├─ 1_Blockchain_Basics.py # add tx -> mine block -> tamper test
│ ├─ 2_Consensus_Playground.py# feel PoW difficulty
│ ├─ 3_RWA_Tokenisation_Demo.py
│ ├─ 4_Risks_and_Reality.py
│ └─ 5_Quiz.py
└─ assets/
└─ glossary.md


---

## 🛠️ Installation & Run Locally
```bash
# 1. Clone the repo
git clone https://github.com/your-username/rwa-edu.git
cd rwa-edu

# 2. (Optional) create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py

## ☁️ Deploy on Streamlit Cloud

1. Push this repo to **GitHub**.  
2. Go to [Streamlit Cloud](https://share.streamlit.io).  
3. Click **“New app”** → select your repo, branch, and `app.py`.  
4. Click **Deploy** → your educational app is live! 🎉  

---

## 🎯 Why this app?

Blockchain and tokenisation are shaping the **new financial system**, but the concepts are often hidden in jargon.  
This app makes the ideas **interactive, visual, and easy to understand** — for students, professionals, and curious investors alike.  
