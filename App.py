import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# CẤU HÌNH TRANG
# ==========================================
st.set_page_config(
    page_title="Food Support - Order",
    page_icon="🍔",
    layout="wide"
)

# ==========================================
# CSS GIAO DIỆN
# ==========================================
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }

    .sub-title {
        text-align: center;
        font-size: 18px;
        color: gray;
    }

    .price {
        color: #e63946;
        font-weight: bold;
        font-size: 18px;
    }

    .invoice {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# TIÊU ĐỀ
# ==========================================
st.markdown(
    '<div class="main-title">🍔 FOOD SUPPORT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Đồ ăn nhanh - Ngon - Tiện lợi - Giá hợp lý</div>',
    unsafe_allow_html=True
)

st
