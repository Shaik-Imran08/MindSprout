import streamlit as st
import time

st.set_page_config(page_title="Toolkit", page_icon="🧰")

st.title("🧰 Your Mental Toolkit")
st.markdown("Proactive tools to help you feel better, anytime.")

# --- 1. SOS Button ---
st.markdown("---")
st.markdown("### 🆘 SOS: Panic Button")
st.markdown("Feeling overwhelmed? Click here for a 1-minute guided breathing exercise.")

if 'breathing' not in st.session_state:
    st.session_state.breathing = False

if st.button("Start 1-Minute Breathing", type="primary"):
    st.session_state.breathing = True

if st.session_state.breathing:
    st.info("Follow the guide. You're doing great.")
    progress_bar = st.progress(0)
    text_placeholder = st.empty()
    
    # 6 cycles of ~10 seconds each
    for i in range(6):
        text_placeholder.markdown("### Inhale... (4s)")
        progress_bar.progress(i/6 + 0.05)
        time.sleep(4)
        
        text_placeholder.markdown("### Hold... (3s)")
        progress_bar.progress(i/6 + 0.10)
        time.sleep(3)
        
        text_placeholder.markdown("### Exhale... (5s)")
        progress_bar.progress(i/6 + 0.16)
        time.sleep(5)

    text_placeholder.success("Well done. You've completed the exercise.")
    st.session_state.breathing = False


# --- 2. Focus Timer ---
st.markdown("---")
st.markdown("### ⏳ Focus Timer")
st.markdown("Clear your mind. Set a timer and just focus on one thing (or nothing at all).")

# We can't play audio easily without hosting a file,
# so we'll just provide the timer.
minutes = st.number_input("Set focus timer (minutes):", min_value=1, max_value=60, value=5)

if st.button("Start Focus Timer"):
    total_seconds = minutes * 60
    timer_placeholder = st.empty()
    timer_bar = st.progress(0)
    
    for i in range(total_seconds):
        secs_left = total_seconds - i
        mins_left = secs_left // 60
        secs_display = secs_left % 60
        
        timer_placeholder.markdown(f"## Time remaining: {mins_left:02}:{secs_display:02}")
        timer_bar.progress((i + 1) / total_seconds)
        time.sleep(1)
        
    timer_placeholder.success("Timer finished! Great job focusing.")
    st.balloons()


# --- 3. Guided Reframes ---
st.markdown("---")
st.markdown("### 📖 Guided Reframes")
st.markdown("Common worries and how to challenge them.")

with st.expander("Challenge a Work Worry"):
    st.markdown("""
    **The Thought:** "If I make a mistake, I'll be fired. I have to be perfect."
    
    **The Pattern:** This is **All-or-Nothing Thinking**.
    
    **The Reframe:**
    1.  What is the *evidence* that one mistake will get you fired?
    2.  Have other people made similar mistakes and *not* been fired?
    3.  What is a more realistic standard for your work? (e.g., "I will do my best, and if I make a mistake, I will learn from it.")
    """)

with st.expander("Process a Fight with a Friend/Partner"):
    st.markdown("""
    **The Thought:** "They are so mad at me, they'll probably never forgive me."
    
    **The Pattern:** This is **Catastrophizing** and **Mind Reading**.
    
    **The Reframe:**
    1.  You cannot know what they are thinking. You are assuming the worst.
    2.  What is the actual issue? (e.g., "I forgot to call them back.")
    3.  What is a simple, constructive step you can take? (e.g., "I will send them a text saying I'm sorry I missed them and ask to talk.")
    """)