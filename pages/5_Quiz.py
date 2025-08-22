import streamlit as st

st.title("🧪 Quick Quiz")
st.caption("Check your understanding. No grades, just feedback.")

QUESTIONS = [
    ("A blockchain block links to the previous one using…", ["QR codes", "Passwords", "Cryptographic hashes", "Spreadsheets"], 2,
     "Blocks store the previous block’s **hash**; any change breaks the link."),
    ("Tokenisation mainly enables…", ["Fractional ownership & easier transfer", "Higher interest rates", "Guaranteed profits", "Lower taxes"], 0,
     "Tokens make it easy to split and transfer ownership; no profits or tax outcomes are guaranteed."),
    ("Consensus difficulty primarily affects…", ["How pretty the UI is", "How hard it is to rewrite history", "The number of wallets", "Government approvals"], 1,
     "Higher difficulty raises the cost to alter past blocks."),
    ("RWA yield depends on…", ["Only token price", "Underlying cashflows & fees", "Hashtags", "Exchange logo"], 1,
     "Real‑world **cashflows** minus **fees** drive returns."),
]

score = 0
for i, (q, opts, correct, expl) in enumerate(QUESTIONS, 1):
    st.subheader(f"{i}. {q}")
    choice = st.radio("Pick one:", opts, index=None, key=f"q{i}")
    if choice is not None:
        if opts.index(choice) == correct:
            st.success("✅ Correct")
            score += 1
        else:
            st.error("❌ Not quite")
        with st.expander("Why?"):
            st.write(expl)

st.divider()
st.metric("Your score", f"{score}/{len(QUESTIONS)}")

