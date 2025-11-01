import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Mind Health",
    page_icon="🧠",
    layout="centered"
)

# --- Session State Initialization ---
# This is crucial for a multi-page app to remember data
if 'garden_plants' not in st.session_state:
    st.session_state.garden_plants = []
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""
if 'distortion_type' not in st.session_state:
    st.session_state.distortion_type = ""
if 'reframe_prompt' not in st.session_state:
    st.session_state.reframe_prompt = ""

# --- "Cognitive Reframe" Logic ---
# This is a *simulation* of a real NLP model.
# In a real-world app, you'd replace this with a model.
COGNITIVE_DISTORTIONS = {
    "All-or-Nothing Thinking": {
        "keywords": ["disaster", "terrible", "perfect", "failed", "never", "always", "idiot", "ruined"],
        "description": "Seeing things in black-and-white. If it's not perfect, it's a total failure.",
        "reframe_prompt": "Let's find the 'gray area'. What is **one small thing** that was *not* a complete failure?"
    },
    "Catastrophizing": {
        "keywords": ["anxious", "what if", "panicking", "worst", "horrible", "awful"],
        "description": "Believing the worst-case scenario is the most likely outcome.",
        "reframe_prompt": "Let's challenge that fear. What is a **more realistic outcome**? What's a simple, small step you could take right now?"
    },
    "Mind Reading": {
        "keywords": ["everyone thinks", "they must think", "probably thinks", "she thinks", "he thinks"],
        "description": "Assuming you know what other people are thinking, usually negatively.",
        "reframe_prompt": "Those are *your* thoughts, not theirs. What is an **alternative, more neutral reason** for their behavior?"
    }
}

def analyze_text(text):
    """
    Simulates NLP analysis to find a cognitive distortion.
    Returns (distortion_type, description, reframe_prompt)
    """
    text_lower = text.lower()
    for distortion, data in COGNITIVE_DISTORTIONS.items():
        if any(keyword in text_lower for keyword in data["keywords"]):
            return (distortion, data["description"], data["reframe_prompt"])
    return (None, None, None) # No distortion found

# --- Callback Functions ---
# These functions are triggered by button presses
def handle_submit():
    """Called when the user submits their initial thought."""
    st.session_state.analysis_complete = True
    st.session_state.user_input = st.session_state.thought_input # Store from widget
    
    # Run the analysis
    distortion, desc, prompt = analyze_text(st.session_state.user_input)
    
    if distortion:
        st.session_state.distortion_type = distortion
        st.session_state.reframe_prompt = prompt
        
        # Show the analysis
        st.info(f"**I'm noticing a pattern:** {distortion}")
        st.markdown(f"**What it is:** {desc}")
    else:
        st.session_state.distortion_type = "None"
        st.session_state.reframe_prompt = "That's a valid feeling. What's one small, kind thing you can do for yourself right now?"
        st.success("Thanks for sharing. It's important to acknowledge how you feel.")

def handle_reframe():
    """Called when the user completes the reframe exercise."""
    with st.spinner("Planting a new seed in your garden..."):
        time.sleep(2) # Add a nice delay
        
    # Add a plant to the garden
    st.session_state.garden_plants.append("🌱")
    
    # Reset the app state for the next check-in
    st.session_state.analysis_complete = False
    st.session_state.user_input = ""
    st.session_state.distortion_type = ""
    st.session_state.reframe_prompt = ""
    
    st.balloons()
    st.success("Great job! You've successfully completed a reframe. A new plant has been added to your garden.")
    # The page will re-run, showing the initial prompt again
    
def handle_skip():
    """Called if the user skips the reframe."""
    st.session_state.analysis_complete = False
    st.session_state.user_input = ""
    st.session_state.distortion_type = ""
    st.session_state.reframe_prompt = ""
    st.info("That's okay. Your feelings are valid. Come back later if you like.")
    time.sleep(1)
    # Page will re-run

# --- Main App UI ---
st.title("🧠 Mind Health Coach")
st.markdown("A calm space to check in with yourself.")

# --- STATE 1: Initial Check-in ---
if not st.session_state.analysis_complete:
    st.markdown("### What's on your mind right now?")
    st.text_area(
        "Share your feelings here. Your entry is private.", 
        height=150, 
        key="thought_input"
    )
    
    st.button("Analyze My Thought", on_click=handle_submit, type="primary")

# --- STATE 2: Analysis & Reframe ---
else:
    st.markdown("### Your Thought:")
    st.markdown(f"> *{st.session_state.user_input}*")
    
    # This block is built in handle_submit(), but we re-display it here
    if st.session_state.distortion_type != "None" and st.session_state.distortion_type:
        st.info(f"**I'm noticing a pattern:** {st.session_state.distortion_type}")
        st.markdown(f"**What it is:** {COGNITIVE_DISTORTIONS[st.session_state.distortion_type]['description']}")
    
    st.markdown("---")
    
    # Display the reframe exercise
    st.markdown("### Let's Try a Quick Reframe")
    st.markdown(st.session_state.reframe_prompt)
    
    st.text_area("Your new thought:", key="reframe_input", height=100)
    
    # Use columns for the buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button(
            "Complete Exercise", 
            on_click=handle_reframe, 
            type="primary", 
            use_container_width=True
        )
    with col2:
        st.button(
            "Skip for Now", 
            on_click=handle_skip, 
            use_container_width=True
        )