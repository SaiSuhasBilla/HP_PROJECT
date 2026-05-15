import streamlit as st
from backend import AkinatorAI

st.set_page_config(page_title="Harry Potter Akinator", page_icon="⚡")

if 'game' not in st.session_state:
    st.session_state.game = AkinatorAI('hp_modified.csv')
    st.session_state.finished = False

st.title("⚡ The AI Wizard Guesser")
st.markdown("Think of a Harry Potter character, and I will read your mind using **Decision Trees**.")

st.write(f"Candidates remaining: **{len(st.session_state.game.candidates)}**")

if len(st.session_state.game.candidates) <= 1:
    st.session_state.finished = True

if not st.session_state.finished:
    question_feature = st.session_state.game.get_next_question()
    
    if question_feature:
        display_q = question_feature.replace('_', ' ').title()
        st.header(f"Question {st.session_state.game.step_counter + 1}:")
        st.subheader(f"**{display_q}?**")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes ✅", use_container_width=True):
                st.session_state.game.update_candidates(question_feature, 1)
                st.rerun()
        with col2:
            if st.button("No ❌", use_container_width=True):
                st.session_state.game.update_candidates(question_feature, 0)
                st.rerun()
    else:
        st.session_state.finished = True
        st.rerun()
else:
    guess = st.session_state.game.get_prediction()
    st.success(f"🎉 I guess... **{guess}**!")
    
    if st.button("Play Again 🔄"):
        del st.session_state.game
        del st.session_state.finished
        st.rerun()