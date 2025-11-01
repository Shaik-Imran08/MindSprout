import streamlit as st

st.set_page_config(page_title="My Garden", page_icon="🌳")

st.title("🌳 My Mind Garden")
st.markdown("Your progress is beautiful. Each time you complete a reframe exercise, a new plant grows in your garden.")
st.markdown("---")

# Check if session state is initialized (user might land here first)
if 'garden_plants' not in st.session_state:
    st.session_state.garden_plants = []

num_plants = len(st.session_state.garden_plants)

# Display the simple metric
st.metric(label="Reframes Completed (Plants Grown)", value=num_plants)

# Display the garden
st.markdown("### Your Garden")
if num_plants == 0:
    st.info("Your garden is waiting to grow. 🌱\n\nGo to the 'Home' page to start your first check-in!")
else:
    # Create a simple visual "garden"
    # We use Markdown to control the text size and make it look nice
    
    # Calculate rows. Let's do 10 plants per row.
    plants_per_row = 10
    num_rows = (num_plants // plants_per_row) + 1
    
    garden_display = ""
    for i in range(num_rows):
        start_index = i * plants_per_row
        end_index = start_index + plants_per_row
        row_plants = st.session_state.garden_plants[start_index:end_index]
        garden_display += " ".join(row_plants) + "\n"
        
    st.markdown(f"<p style='font-size: 36px; line-height: 1.5;'>{garden_display}</p>", unsafe_allow_html=True)

# Add some gamification logic
st.markdown("---")
if num_plants > 10:
    st.markdown("Amazing! You've grown a small grove! 🌳🌳")
elif num_plants > 5:
    st.markdown("Your garden is flourishing! 🌷")
elif num_plants > 0:
    st.markdown("Great start! Your first few sprouts have appeared. 🌱")