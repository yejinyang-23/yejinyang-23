import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="초짜 마법사의 대모험", page_icon="🧙", layout="centered")

# 세션 상태 초기화
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
    st.session_state.monster_count = 0
    st.session_state.current_monster = None

# 제목
st.title("🧙 초짜 마법사의 대모험 🧙")

# 게임 스테이지별 진행
if st.session_state.stage == 'intro':
    st.write("어느 날, 왕국에 이상한 몬스터들이 나타났다!")
    st.write("초짜 마법사 '너'는 왕의 명령으로 모험을 떠난다.")
    if st.button("모험 시작하기!"):
        st.session_state.stage = 'encounter'
        st.session_state.current_monster = random.choice(
            ["고구마 드래곤", "춤추는 슬라임", "화난 당근", "노래하는 오우거"]
        )

elif st.session_state.stage == 'encounter':
    st.subheader(f"👾 몬스터 등장: {st.session_state.current_monster}!")
    st.write("무엇을 할까?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✨ 마법 쓰기"):
            if random.choice([True, False]):
                st.success(f"너의 마법이 {st.session_state.current_monster}에게 적중했다! 몬스터는 도망갔다!")
            else:
                st.warning(f"마법이 빗나갔다! {st.session_state.current_monster}가 웃으며 너를 놀린다...")
            st.session_state.monster_count += 1
            st.session_state.current_monster = random.choice(
                ["고구마 드래곤", "춤추는 슬라임", "화난 당근", "노래하는 오우거"]
            )
    with col2:
        if st.button("🏃‍♂️ 도망가기"):
            st.info(f"너는 {st.session_state.current_monster}를 피해 멋지게 도망쳤다!")
            st.session_state.monster_count += 1
            st.session_state.current_monster = random.choice(
                ["고구마 드래곤", "춤추는 슬라임", "화난 당근", "노래하는 오우거"]
            )
            

    if st.session_state.monster_count >= 3:
        st.session_state.stage = 'ending'

elif st.session_state.stage == 'ending':
    st.balloons()
    st.success("🎉 드디어 왕국을 지킨 초짜 마법사!")
    st.write("왕이 말했다: '그래도 꽤 쓸만하군!'")
    st.write("🏆 [ 게임 끝! 고생했어! ] 🏆")
    if st.button("다시 시작하기"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
