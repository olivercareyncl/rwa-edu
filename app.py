import streamlit as st

st.set_page_config(page_title="The New Financial System — Explained", page_icon="🧭", layout="wide")

st.title("🧭 The New Financial System — Explained")
st.caption("An interactive guide to Blockchain, Tokenisation, and Real‑World Assets (RWAs).")

col1, col2 = st.columns([1.2, 1])
with col1:
    st.markdown("""
### What is a blockchain?
A **blockchain** is a shared public spreadsheet. New rows (transactions) are grouped into **blocks**, each block locks to the previous one with a **cryptographic hash**. Change a past row and the hash breaks — the spreadsheet *tells on you*.

### Why does this matter?
- **Trust without a central gatekeeper**: anyone can verify the record.
- **Programmable money**: smart contracts automate rules (interest, collateral, royalties).
- **24/7 markets**: assets can move and settle in minutes, not days.

### What are RWAs (Tokenised Real‑World Assets)?
RWAs are off‑chain assets (property, treasuries, carbon credits) represented as **tokens** on a blockchain. Tokens let you:
- **Fractionalise** ownership (buy 0.1% of a building),
- **Trade** more easily,
- **Automate** payouts via smart contracts.

Use the pages on the left to **learn by doing**.
""")

with col2:
    st.info("Tip: You can view the source code on GitHub and reuse any component in your own projects.")
    st.markdown("**Try next:** “🏗️ Blockchain Basics” to see how hashes secure a chain.")
    st.divider()
    st.markdown("### Glossary (quick hits)")
    st.markdown("- **Hash**: digital fingerprint of data\n- **Block**: bundle of transactions\n- **Consensus**: how the network agrees\n- **Tokenisation**: representing ownership as tokens")

