import streamlit as st

st.set_page_config(page_title="FestiveVibe", layout="wide")

st.title("🎉 FestiveVibe: Celebrating the Traditions of Telugu States")

st.markdown("""
Welcome to **FestiveVibe** – a cultural hub to explore and share the beautiful festival traditions of **Andhra Pradesh** and **Telangana**.
""")

# Sidebar filters
st.sidebar.header("🔍 Filter by Region")
region = st.sidebar.selectbox("Choose Region", ["All", "Andhra Pradesh", "Telangana"])

# Festivals data
festivals = {
    "Sankranti": {
        "state": "Both",
        "description": "Sankranti is celebrated with rangoli (muggulu), bhogi fire, and kite flying.",
    },
    "Bathukamma": {
        "state": "Telangana",
        "description": "A floral festival where women sing and dance around beautiful flower stacks.",
    },
    "Bonalu": {
        "state": "Telangana",
        "description": "Goddess Mahakali festival where devotees offer cooked rice and dance.",
    },
    "Ugadi": {
        "state": "Both",
        "description": "New Year festival with Ugadi pachadi and rituals.",
    },
    "Vinayaka Chavithi": {
        "state": "Both",
        "description": "Lord Ganesha is worshipped with clay idols, sweets and cultural events.",
    },
    "Dasara": {
        "state": "Both",
        "description": "Also known as Dussehra – celebration of good over evil with processions.",
    }
}

# Display festival cards
st.subheader("🌟 Explore Festivals")
for fest, details in festivals.items():
    if region == "All" or region in details["state"]:
        with st.expander(f"🎊 {fest}"):
            st.write(details["description"])
            st.image("https://source.unsplash.com/800x400/?festival,india", use_column_width=True)

# User contribution section
st.subheader("📝 Add Your Tradition")

with st.form("submit_tradition"):
    name = st.text_input("Your Name")
    festival = st.selectbox("Festival", list(festivals.keys()))
    story = st.text_area("Describe how you celebrate it in your town or family.")
    photo = st.file_uploader("Upload a Photo (optional)", type=["jpg", "jpeg", "png"])
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("🎉 Your tradition has been submitted! Thank you for preserving our culture!")

# Footer
st.markdown("---")
st.markdown("© 2025 FestiveVibe • Built with ❤️ using Streamlit")

