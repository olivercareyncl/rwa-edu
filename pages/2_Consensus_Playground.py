import streamlit as st, time, hashlib, random

st.title("⛏️ Consensus Playground")
st.caption("Adjust difficulty to feel why consensus protects history (toy Proof‑of‑Work).")

def pow_sim(difficulty:int, max_steps:int=150000):
    nonce = 0; t0 = time.time()
    while nonce < max_steps:
        h = hashlib.sha256(f"data{nonce}".encode()).hexdigest()
        if h.startswith("0"*difficulty):
            return nonce, time.time()-t0
        nonce += 1
    return None, time.time()-t0

d = st.slider("Difficulty", 1, 6, 3)
if st.button("Run simulation"):
    nonce, secs = pow_sim(d)
    if nonce is None:
        st.warning(f"No solution found in the step budget. That’s the point: higher difficulty = harder to rewrite history.")
    else:
        st.success(f"Found a valid nonce {nonce} in {secs:.2f}s at difficulty {d}.")

st.markdown("""
**Takeaway:** To change an old block, an attacker must redo **all** the work from that block onward *and* catch up with the honest network.  
That’s why Proof‑of‑Work secures history.
""")

