import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# 1. 구글 시트 연동 설정
@st.cache_resource
def init_connection():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://spreadsheets.google.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    # 깃허브 배포를 위해 st.secrets 사용 (로컬 테스트 시에는 secret.json 파일 경로 직접 기입 가능)
    creds_dict = st.secrets["gcp_service_account"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    return client

client = init_connection()
# 공유해주신 구글 시트 URL을 입력하세요
SHEET_URL = "https://docs.google.com/spreadsheets/d/1EAk9EDmuaZPgF87DwSRzJkzGrUSzRNGtNwnAX7bFhVE/edit"
doc = client.open_by_url(SHEET_URL)
order_sheet = doc.worksheet("발주접수내역") # 시트 내 탭 이름 확인 필수

st.title("프리미엄 차량 케어 가맹점 발주 시스템")

# 2. 데이터 불러오기 (샘플 데이터)
product_list = [
    {"상품명": "다이아몬드 키퍼 케미컬", "구분": "강제", "단위": "본"},
    {"상품명": "KeePer Cross", "구분": "강제", "단위": "세트"},
    {"상품명": "Sheepskin Mitt", "구분": "선택", "단위": "개"},
    {"상품명": "폭백(바쿠하쿠) ONE", "구분": "강제", "단위": "캔"}
]
df = pd.DataFrame(product_list)

# 3. 발주 입력 UI
branch_name = st.text_input("가맹점명을 입력하세요 (예: 일산점)")
orders = {}

st.subheader("발주 품목 선택")
for index, row in df.iterrows():
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(f"**{row['상품명']}** ({row['구분']})")
    with col2:
        st.write(row['단위'])
    with col3:
        qty = st.number_input(f"{row['상품명']} 수량", min_value=0, value=0, label_visibility="collapsed", key=row['상품명'])
        if qty > 0:
            orders[row['상품명']] = qty

# 4. 발주 데이터 전송 버튼
if st.button("발주 요청하기"):
    if not branch_name:
        st.error("가맹점명을 입력해주세요.")
    elif not orders:
        st.warning("발주할 품목의 수량을 1개 이상 입력해주세요.")
    else:
        # 구글 시트에 데이터 추가 (시간, 가맹점명, 품목, 수량 등)
        order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for item, qty in orders.items():
            order_sheet.append_row([order_time, branch_name, item, qty])
            
        st.success(f"[{branch_name}] 발주가 성공적으로 본사에 접수되었습니다!")
        st.json(orders)
