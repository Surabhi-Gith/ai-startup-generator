import streamlit as st
import random
from datetime import datetime
import os

# Streamlit page settings
st.set_page_config(page_title="AI Startup Idea Generator", page_icon="💡", layout="centered")

# 💡 Title & subtitle
st.title("💡 AI Startup Idea Generator")
st.caption("Turn bold ideas into billion-dollar businesses. Built by Surabhi Singh.")

st.markdown("---")

# 📂 Category selector
categories = ["General", "HealthTech", "FinTech", "EdTech", "ClimateTech", "AI Tools", "SaaS", "Productivity", "Mental Health"]
col1, col2 = st.columns(2)
with col1:
    category = st.selectbox("📂 Choose a category", categories)
with col2:
    tone = st.selectbox("🧠 Idea Style", ["Innovative", "Disruptive", "Simple", "AI-Driven"])

# 🔍 Topic input
topic = st.text_input("🔍 What’s your startup about? (problem, trend, niche)", placeholder="e.g. loneliness, language learning, remote teams")

# 🛠 Idea generator logic
def generate_ideas(topic, category, tone):
    topic = topic.capitalize()
    base = f"in the {category} space" if category != "General" else ""
    emoji = random.choice(["🚀", "💡", "🌱", "✨", "🔥", "🧠", "📈"])

    templates = [
        f"{emoji} A platform for solving {topic} {base} using AI-driven matching.",
        f"{emoji} A mobile-first tool to address {topic} by combining gamification and AI {base}.",
        f"{emoji} A community-led app to tackle {topic} {base}, backed by token-based incentives.",
        f"{emoji} A no-code SaaS product that helps people automate {topic}-related tasks {base}.",
        f"{emoji} A GPT-powered assistant that gives expert advice on {topic} for users {base}.",
        f"{emoji} A smart marketplace that solves {topic} by connecting niche creators and users {base}."
    ]

    if tone == "Simple":
        templates = [t.replace("using", "with") for t in templates]

    return random.sample(templates, 3)

# 🚀 Generate Ideas
if st.button("🚀 Generate Startup Ideas"):
    if topic:
        st.markdown("---")
        st.subheader("🚀 Your 3 AI Startup Ideas")
        ideas = generate_ideas(topic, category, tone)

        for i, idea in enumerate(ideas, 1):
            st.markdown(f"**{i}.** {idea}")

        st.balloons()

        # 💾 Save to file
        if st.checkbox("💾 Save these ideas to a local file"):
            filename = f"startup_ideas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            os.makedirs("generated", exist_ok=True)
            path = os.path.join("generated", filename)
            with open(path, "w") as f:
                f.write(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                f.write(f"📂 Category: {category}\n")
                f.write(f"🔍 Topic: {topic}\n")
                f.write(f"🧠 Tone: {tone}\n\n")
                for i, idea in enumerate(ideas, 1):
                    f.write(f"{i}. {idea}\n")
            st.success(f"Ideas saved to `{path}` 📄")
    else:
        st.warning("Please enter a topic to generate startup ideas.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Surabhi • [GitHub](https://github.com/Surabhi-Gith)")
