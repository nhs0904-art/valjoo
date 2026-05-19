import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 1. 구글 시트 연동 설정 (API 인증 키 필요)
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)
# client = gspread.authorize(creds)

st.title("프리미엄 차량 케어 가맹점 발주 시스템")
st.write("필요한 품목의 수량을 입력한 후 발주 버튼을 눌러주세요.")

# 2. 데이터 불러오기 
# 실제 환경에서는 client.open_by_url()을 통해 시트의 '강제품목의사결정' 데이터를 읽어옵니다.
# 아래는 시제시해주신 구글 시트의 구조를 확인했습니다. '다이아몬드 키퍼 케트 구조를 반영한 예시 데이터입니다.
product_list = [
    {"상품명": "다이아몬드 키퍼 케미컬", "구분": "강제", "단위": "본"},
    {"상품명": "KeePer Cross", "구분": "강제", "단위": "세트"},  # 용어 표준화 강제 적용 (원본: 키퍼 크로스)
    {"상품명": "Sheepskin Mitt", "구분": "선택", "단위": "개"},  # 용어 표준화 강제 적용 (원본: 라·몹)
    {"상품명": "폭백(바쿠하쿠) ONE", "구분": "강제", "단위": "캔"}
]
df = pd.미컬', '레진2' 등의 제품 목록과 함께 '강제품목여부(강제, 선택, 제거)', 그리고 각 품목별 표준 매뉴얼DataFrame(product_list)

# 3. 발주 입력 UI (가맹점명 및 수량 입력)
branch_name = st.text_input("(PDI 기준, 시공 표준 매뉴얼 등)이 탭별로 매우 체계적으로 정리되어 있습니다. 또한 10,0가맹점명을 입력하세요 (예: 일산점)")

orders = {}
st.subheader("발주 품목 선택")

# 리스트를 순회하며 화면00엔 미만 주문 시 700엔의 배송비가 부과되는 중요한 비즈니스 규칙도 명시되어 있네요에 입력창 생성
for index, row in df.iterrows():
    # '제거' 품목은 화면에 노출하지 않는 로직을 여기에 추가할 수 있습니다.
    col1, col2, col3 = st.columns([3, 1, 1])
    with col[cite: 1].

이러한 구조에서 가맹점 발주를 자동화하려면, 엑셀이나 구글 시트 원본을 직접 공유하여1:
        st.write(f"**{row['상품명']}** ({row['구분']})")
    with col2:
        st. 수기로 입력받는 방식에서 벗어나 **'구글 시트(DB) ↔ 파이썬(Streamlit) 웹 포털'** 구조로 분리하는 것이 가장 직관적이고 효율적입니다. 

### 1. 발주 수집 프로세스 설계
1. **데이터베이스(DB):** 현재 작성하신 구글 시트가 훌륭한 백엔드 DB 역할을 수행합니다. '키퍼 발주 목록' 시트에서write(row['단위'])
    with col3:
        # 수량 입력 받기
        qty = st.number_input(f"{row['상품명']} 수량", min_value=0, value=0, label_visibility="collapsed")
        if qty > 0:
            orders[row['상품명']] = qty

# 4. 발주 데이터 구글 시트로 전송 (취합)
if st.button("발주 요청하기"):
    if 품목 정보와 강제 여부를 불러오고, 가맹점의 주문 내역을 시간순으로 쌓아둘 새로운 시트(예: `발주_접 not branch_name:
        st.error("가맹점명을 입력해주세요.")
    elif not orders:
        st.warning("발주할 품목의수내역`)를 하나 추가합니다[cite: 1].
2. **가맹점용 발주 웹(Front-end):** 파이썬의 스트림 수량을 1개 이상 입력해주세요.")
    else:
        # 접수된 데이터를 구글 시트의 '발주 접수 내역' 탭에릿(Streamlit)을 이용해 가맹점주 전용 웹페이지를 만듭니다. 점주들은 복잡한 원본 시트를 볼 필요 없이, 모바일이나 PC 브라우저로 접속해 필요한 수량만 직관적으로 입력하면 됩니다.
3. **비즈니스 로직 적용 새로운 행(Row)으로 추가하는 로직이 들어갑니다.
        # 예: sheet.append_row([현재시간, branch_name, 상품명, 수량])
        st.success(f"[{branch_name}] 발주가 성공적으로 본사에 접수되었습니다!")
        st.json(orders):** '강제' 품목은 기본적으로 필수 항목으로 표시하거나, 총액이 10,000엔 미만일 때 배 # 접수 내역 화면에 출력