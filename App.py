import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(
    page_title="Food Support",
    page_icon="🍔",
    layout="wide"
)

# ==========================================
# TIÊU ĐỀ
# ==========================================
st.title("🍔 FOOD SUPPORT")
st.subheader("Hệ thống gọi món và quản lý hóa đơn")
st.divider()

# ==========================================
# MENU
# ==========================================
menu = {
    "🍕 Pizza Hải Sản": 120000,
    "🍝 Mì Ý Bò Bằm": 50000,
    "🍔 Burger Gà": 65000,
    "🥗 Salad Trộn": 50000,
    "🥩 Bít Tết Bò Mỹ": 250000,
    "🍖 Sườn Nướng BBQ": 180000,
    "🍗 Cánh Gà Chiên Mắm": 75000,
    "🍟 Khoai Tây Chiên": 35000,
    "🍜 Mì Trộn": 45000,
    "🥤 Nước Ngọt": 15000
