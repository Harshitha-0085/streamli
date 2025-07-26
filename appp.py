import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup connection to Google Sheet (if needed)
@st.cache_resource
def connect_to_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("your-creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("FestivalVibeSubmissions").sheet1
    return sheet

# Header
st.set_page_config(page_title="FestivalVibe", page_icon="🌸")
st.markdown("""
# 🌸 FestivalVibe — Celebrate Telugu Culture With Us! 🎉

🪔 **What’s your favorite festival memory?**  
🌼 **How does your family celebrate Bathukamma, Bonalu, or Sankranti?**  
📸 Upload your stories, photos, or even your grandma’s secret recipes on **FestivalVibe** – a fun app built to preserve and celebrate the beautiful traditions of **Andhra Pradesh & Telangana**!

💬 *Speak in your language. Share your vibes. Make your culture timeless.*

👇 **Submit your festival story today!**
""", unsafe_allow_html=True)

# Form
st.subheader("📝 Share Your Festival Story")
with st.form("story_form"):
    name = st.text_input("Your Name")
    festival = st.selectbox("Choose Festival", ["Ugadi", "Bonalu", "Sankranti", "Bathukamma", "Other"])
    story = st.text_area("Your Memory / Ritual / Recipe")
    image_url = st.text_input("Image Link (optional)")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and story:
            try:
                sheet = connect_to_sheet()
                sheet.append_row([name, festival, story, image_url])
                st.success("Your story has been added to FestivalVibe! 🌟")
            except:
                st.warning("Error saving to Google Sheet. Please check credentials.")
        else:
            st.warning("Please fill in all required fields.")

# Display (optional preview)
st.markdown("---")
st.subheader("📚 Latest Festival Vibes (Top 3)")

try:
    sheet = connect_to_sheet()
    data = sheet.get_all_records()
    if data:
        df = pd.DataFrame(data)[::-1].head(3)  # Latest 3
        for i, row in df.iterrows():
            st.markdown(f"### ✨ {row['festival']} by {row['name']}")
            st.write(row['story'])
            if row['image_url']:
                st.image(row['image_url'], use_column_width=True)
            st.markdown("---")
    else:
        st.info("No stories submitted yet. Be the first!")
except:
    st.stop()
