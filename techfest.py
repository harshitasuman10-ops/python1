import streamlit as st

st.set_page_config(page_title="InterviewMirror", page_icon="🎯")

st.title("🎯 InterviewMirror")
st.subheader("Your personal interview practice assistant")

role = st.selectbox(
    "Choose your target role",
    ["Software Developer", "Data Analyst", "AI/ML Intern"]
)

question = st.selectbox(
    "Choose an interview question",
    [
        "Tell me about yourself.",
        "Why should we select you?",
        "Describe a challenge you solved."
    ]
)

st.write("**Interview question:**", question)

answer = st.text_area(
    "Type your answer here",
    placeholder="Write your interview answer..."
)

if st.button("Evaluate My Answer"):
    if not answer.strip():
        st.warning("Please type your answer first.")
    else:
        words = len(answer.split())
        st.subheader("Your feedback")

        st.write(f"**Target role:** {role}")
        st.write(f"**Word count:** {words}")

        if words < 30:
            st.info("Try adding more detail and a specific example.")
        elif words > 150:
            st.info("Try making your answer more concise.")
        else:
            st.success("Good starting length! Now check relevance, clarity, and examples.")

        st.write("**Improvement tip:** Explain the situation, your action, and the result.")