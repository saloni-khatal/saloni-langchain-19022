# Streamlit Healthy Lifestyle FAQ Chatbot
# Save as app.py

import sys
import traceback

try:
    import streamlit as st
except Exception:
    print("Missing dependency: streamlit. Run: pip install streamlit")
    sys.exit(1)

st.set_page_config(page_title="💪 Healthy Lifestyle Chatbot", page_icon="🍏", layout="centered")

st.title("💪 Healthy Lifestyle FAQ Chatbot")
st.markdown("Ask anything about **diet, exercise, sleep, mental health, or wellness tips**.")

# ---------------- FAQ Data ----------------
faq_data = [
    {"question": "What is a balanced diet?",
     "answer": "A balanced diet includes a mix of fruits, vegetables, proteins, whole grains, and healthy fats."},

    {"question": "How much water should I drink daily?",
     "answer": "On average, 8 glasses (around 2 liters) per day is recommended, but it may vary depending on activity level and climate."},

    {"question": "How often should I exercise?",
     "answer": "At least 150 minutes of moderate-intensity aerobic activity per week, plus strength training twice a week."},

    {"question": "What are good sleep habits?",
     "answer": "Maintain a regular sleep schedule, avoid screens before bedtime, and keep your bedroom dark and quiet."},

    {"question": "How to manage stress?",
     "answer": "Practice mindfulness, meditation, breathing exercises, regular exercise, and ensure adequate rest."},

    {"question": "What foods boost immunity?",
     "answer": "Citrus fruits, berries, nuts, yogurt, garlic, spinach, and foods rich in vitamin C and zinc can help."},

    {"question": "What are healthy snacks?",
     "answer": "Fruits, nuts, yogurt, hummus with vegetables, or whole-grain crackers are good healthy snacks."},

    {"question": "Can I lose weight without exercise?",
     "answer": "Yes, diet plays a major role in weight loss, but exercise improves overall health and metabolism."},

    {"question": "How much sleep do adults need?",
     "answer": "Adults typically need 7-9 hours of sleep per night for optimal health."},

    {"question": "What are some stress-relief activities?",
     "answer": "Yoga, meditation, journaling, walking in nature, listening to music, and spending time with loved ones are helpful."},

    {"question": "How to maintain mental health?",
     "answer": "Practice self-care, get enough sleep, stay socially connected, exercise regularly, and seek professional help if needed."},

    {"question": "Is intermittent fasting healthy?",
     "answer": "Intermittent fasting can be beneficial for some people, but consult a healthcare professional before starting."},

    {"question": "How can I improve my digestion?",
     "answer": "Eat fiber-rich foods, stay hydrated, chew food thoroughly, avoid overeating, and include probiotics."},

    {"question": "What vitamins are essential?",
     "answer": "Vitamins A, B-complex, C, D, E, and K are essential for overall health, along with minerals like calcium, iron, and zinc."},

    {"question": "How to stay motivated for exercise?",
     "answer": "Set realistic goals, track progress, vary workouts, exercise with friends, and reward yourself for milestones."}
]

# ---------------- Sidebar Quick Links ----------------
st.sidebar.title("📌 Quick FAQs")
quick_links = [
    "Balanced Diet",
    "Water Intake",
    "Exercise Frequency",
    "Sleep Tips",
    "Stress Management",
    "Immunity Foods",
    "Healthy Snacks",
    "Mental Health",
    "Weight Loss",
    "Vitamins & Minerals"
]
for item in quick_links:
    st.sidebar.markdown(f"- {item}")

# ---------------- Simple Keyword Retrieval ----------------
def faq_retrieval(user_query):
    user_query = user_query.lower()
    matches = []
    for f in faq_data:
        if any(word in user_query for word in f["question"].lower().split()):
            matches.append(f)
    return matches

# ---------------- Main Input Box ----------------
query = st.text_input("💬 Type your question here:")

if st.button("Get Answer") and query:
    with st.spinner("Searching for answers..."):
        try:
            results = faq_retrieval(query)
        except Exception:
            st.error("Error while retrieving answer.")
            st.code(traceback.format_exc())
            st.stop()

    if results:
        st.subheader("✅ Answer(s) Found")
        for r in results:
            st.success(f"{r['answer']}")
            st.info(f"📌 Related Question: *{r['question']}*")
    else:
        st.warning("❌ Sorry, I couldn't find an exact answer.")
        # Optional: show top 3 related questions by keyword overlap
        st.markdown("💡 Try asking about:")
        suggestions = sorted(faq_data, key=lambda x: len(set(x['question'].lower().split()) & set(query.lower().split())), reverse=True)[:3]
        for s in suggestions:
            st.write(f"- {s['question']}")
