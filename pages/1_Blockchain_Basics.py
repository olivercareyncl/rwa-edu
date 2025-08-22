import streamlit as st, pandas as pd, hashlib, time

st.title("🏗️ Blockchain Basics")
st.caption("Add transactions → build a block → see how hashes secure the chain.")

# --- helpers
def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

if "mempool" not in st.session_state:
    st.session_state.mempool = []
if "chain" not in st.session_state:
    # genesis block
    st.session_state.chain = [{
        "index": 0, "timestamp": time.time(), "transactions": ["Genesis block"],
        "prev_hash": "0"*64, "nonce": 0, "hash": ""
    }]
    st.session_state.chain[0]["hash"] = sha256(
        f'{st.session_state.chain[0]["index"]}{st.session_state.chain[0]["timestamp"]}{st.session_state.chain[0]["transactions"]}{st.session_state.chain[0]["prev_hash"]}{st.session_state.chain[0]["nonce"]}'
    )

st.subheader("1) Add transactions to the mempool")
tx = st.text_input("New transaction (e.g., Alice pays Bob 5)", key="tx_input")
col_add, col_clear = st.columns(2)
if col_add.button("➕ Add"):
    if tx.strip():
        st.session_state.mempool.append(tx.strip())
if col_clear.button("🧹 Clear mempool"):
    st.session_state.mempool = []

st.code("\n".join(st.session_state.mempool) or "(empty)")

st.subheader("2) Mine a block (toy PoW)")
difficulty = st.slider("Difficulty (number of leading zeros)", 1, 5, 3)
if st.button("⛏️ Mine block"):
    prev = st.session_state.chain[-1]
    nonce = 0
    start = time.time()
    while True:
        candidate = {
            "index": len(st.session_state.chain),
            "timestamp": time.time(),
            "transactions": st.session_state.mempool[:] or ["(no transactions)"],
            "prev_hash": prev["hash"],
            "nonce": nonce
        }
        block_str = f'{candidate["index"]}{candidate["timestamp"]}{candidate["transactions"]}{candidate["prev_hash"]}{candidate["nonce"]}'
        h = sha256(block_str)
        if h.startswith("0"*difficulty):
            candidate["hash"] = h
            st.session_state.chain.append(candidate)
            st.session_state.mempool = []
            break
        nonce += 1
        # keep the UI responsive
        if nonce % 5000 == 0 and time.time() - start > 5:
            st.warning("Mining is taking a while at this difficulty; try lowering it.")
            break

st.subheader("3) Inspect the chain")
df = pd.DataFrame([{
    "idx": b["index"],
    "tx_count": len(b["transactions"]),
    "prev_hash": b["prev_hash"][:10]+"…",
    "nonce": b["nonce"],
    "hash": b.get("hash","")[:10]+"…"
} for b in st.session_state.chain])
st.dataframe(df, use_container_width=True)

st.subheader("4) Tamper test (see hashes break)")
i = st.number_input("Choose block to edit (not 0)", min_value=1, max_value=len(st.session_state.chain)-1 if len(st.session_state.chain)>1 else 1, step=1)
if st.button("✍️ Edit chosen block’s first transaction"):
    st.session_state.chain[int(i)]["transactions"][0] = "🛠️ Tampered!"
    # recompute this block's hash only (downstream will mismatch)
    b = st.session_state.chain[int(i)]
    block_str = f'{b["index"]}{b["timestamp"]}{b["transactions"]}{b["prev_hash"]}{b["nonce"]}'
    b["hash"] = sha256(block_str)

# validate
ok = True
for j in range(1, len(st.session_state.chain)):
    if st.session_state.chain[j]["prev_hash"] != st.session_state.chain[j-1]["hash"]:
        ok = False; break
st.info("Chain valid ✅" if ok else "Chain broken ❌ — hashes no longer link. Re-mining required.")

