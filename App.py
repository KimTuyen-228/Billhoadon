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
    "Lẩu Thái Hải Sản": 199000,
    "Lẩu Thập Cẩm": 199000,
    "Lẩu Mắm": 199000000,
    "Gỏi ngó sen tai heo": 89000,
    "Chả giò": 79000,
    "Bò nướng mỡ chài": 139000,
    "Tôm sốt mắm tắc": 139000,
    "🍟 Khoai Tây Chiên": 35000,
    "🍜 Mì Trộn": 45000,
    "🥤 Nước Ngọt": 15000
