import streamlit as st
import math

st.title("🏠 RWA Tokenisation Demo")
st.caption("Fractionalise an asset, compute yields, and explore simple liquidity scenarios.")

st.subheader("1) Define the real‑world asset")
colA, colB, colC = st.columns(3)
with colA:
    asset_value = st.number_input("Asset value (e.g., property) £", 50_000, 50_000_000, 500_000, step=10_000)
with colB:
    annual_cashflow = st.number_input("Annual net cashflow (rent/coupon) £", 0, 5_000_000, 30_000, step=1_000)
with colC:
    tokens = st.number_input("Number of tokens", 100, 10_000_000, 100_000, step=100)

token_price = asset_value / tokens
cash_yield = (annual_cashflow / asset_value) * 100

st.metric("Implied token price", f"£{token_price:,.2f}")
st.metric("Cash yield (before fees)", f"{cash_yield:.2f}%")

st.subheader("2) Investor view")
col1, col2, col3 = st.columns(3)
with col1:
    my_invest = st.number_input("My investment (£)", 100, 1_000_000, 5_000, step=100)
with col2:
    platform_fee = st.slider("Platform fee (%)", 0.0, 3.0, 0.5, 0.1)
with col3:
    vacancy_risk = st.slider("Cashflow downside (%)", 0.0, 30.0, 5.0, 1.0)

my_tokens = my_invest / token_price if token_price > 0 else 0
net_cashflow = annual_cashflow * (1 - vacancy_risk/100) * (1 - platform_fee/100)
my_yield = (net_cashflow / asset_value) * 100

st.write(f"You’d hold **{my_tokens:,.2f} tokens** and earn an estimated **{my_yield:.2f}%** net yield (pro‑rata).")

st.subheader("3) Simple liquidity thought experiment")
spread = st.slider("Bid‑Ask spread (%)", 0.0, 5.0, 1.0, 0.1)
slippage = st.slider("DEX slippage on trade (%)", 0.0, 5.0, 0.5, 0.1)

sell_price = token_price * (1 - spread/100) * (1 - slippage/100)
buy_price  = token_price * (1 + spread/100) * (1 + slippage/100)

colx, coly = st.columns(2)
colx.metric("Estimated sell price", f"£{sell_price:,.2f}")
coly.metric("Estimated buy price",  f"£{buy_price:,.2f}")

st.markdown("""
**Takeaway:** Tokenisation makes **fractional ownership & automated payouts** easy, but **liquidity, fees, and cashflow risk** still drive returns — just like in traditional markets.
""")

