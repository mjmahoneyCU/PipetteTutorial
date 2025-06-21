import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(page_title="Buffs Biotech: Pipetting Masterclass", layout="wide")

# --- STUDENT NAME ---
team_name = st.text_input("Enter your team name to track your progress:")
if team_name:
    st.success(f"Welcome Team {team_name}! Let's master pipetting.")

    tabs = st.tabs([
        "Intro", "Parts of Pipette", "Set Volume", "Attach Tip", "Draw Liquid",
        "Dispense Liquid", "Viscous Solutions", "Common Errors", "Practice & Reflection"
    ])

    # TAB 0: Intro
    with tabs[0]:
        st.header("📘 Introduction to Pipetting")
        st.markdown("""
Micropipettes allow scientists to transfer tiny liquid volumes precisely — critical for every biotech lab!
Today, you will learn **how to pipette accurately**, fix common mistakes, and test your skills.
""")

    # TAB 1: Parts of Pipette
    with tabs[1]:
        st.header("🔩 Parts of a Micropipette")
        st.markdown("""
- **Plunger** (pushes and releases liquid)  
- **Volume adjustment dial**
- **Volume display window**
- **Tip ejector button**
- **Shaft** (where the tip fits)
""")
        st.info("💡 **Take a moment to locate each part on the actual micropipette at your bench.**")
        col1, col2 = st.columns(2)
        with col1:
            st.image("pipettor.png", caption="Labeled micropipette", use_container_width=True)
        with col2:
            st.image("pipette_box.png", use_container_width=True)

    # TAB 2: Set Volume
    with tabs[2]:
        st.header("🎯 Setting the Volume")
        st.markdown("""
- Turn the dial clockwise to decrease, counterclockwise to increase.
- Always stay within the correct range for each pipette:
  - P20: 2–20 µL
  - P200: 20–200 µL
  - P1000: 100–1000 µL
- Rotate slightly past your volume, then dial back for best accuracy.
""")
        st.image("pipette_volumes.png", caption="Pipette volume settings", use_container_width=True)

        st.subheader("🧠 Match the Pipette Display to the Correct Volume:")
        volume_options = ["Select", "2 µL", "10 µL", "20 µL", "80 µL", "100 µL", "200 µL", "800 µL"]

        pipetteA = st.selectbox("Pipette A:", volume_options, index=0, key="pipetteA_q")
        pipetteB = st.selectbox("Pipette B:", volume_options, index=0, key="pipetteB_q")
        pipetteC = st.selectbox("Pipette C:", volume_options, index=0, key="pipetteC_q")
        pipetteD = st.selectbox("Pipette D:", volume_options, index=0, key="pipetteD_q")

        if st.button("Check My Matching Answers", key="check_matching_btn"):
            correct_answers = {
                "pipetteA_q": "800 µL",
                "pipetteB_q": "200 µL",
                "pipetteC_q": "100 µL",
                "pipetteD_q": "2 µL"
            }

            for key, label in zip(["pipetteA_q", "pipetteB_q", "pipetteC_q", "pipetteD_q"], ["A", "B", "C", "D"]):
                selection = locals()[f"pipette{label}"]
                if selection == correct_answers[key]:
                    st.success(f"Pipette {label}: Correct! ✅")
                else:
                    st.warning(f"Pipette {label}: Incorrect. Please try again! 🤔")

            st.markdown("---")

        answer1 = st.radio("Which pipette would you use for 150 µL?", ["P20", "P200", "P1000"], index=None, key="volume_check")
        if answer1 == "P200":
            st.success("Correct! P200 (20–200 µL) is the right choice for 150 µL. ✅")
        elif answer1:
            st.warning("Not quite. That pipette's range doesn't cover 150 µL. Please try again! 🤔")

    # TAB 3: Attach Tip
    with tabs[3]:
        st.header("🧪 Attaching the Tip")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
- Push the pipette firmly into the correct color tip:
  - Clear for P20
  - Yellow for P200
  - Blue for P1000
- Listen for a soft 'click' to confirm attachment.

✍️ **Now practice adding tips to your pipettes at your bench.**
""")
        with col2:
            youtube_attach_url = "https://youtu.be/CJWCM9kM-YE"
            video_id = youtube_attach_url.split("youtu.be/")[-1]
            embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}&controls=0&modestbranding=1"
            components.html(
                f"""
                <iframe width="100%" height="315"
                    src="{embed_url}"
                    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
                </iframe>
                """,
                height=320,
            )

    # TAB 4: Draw Liquid
    with tabs[4]:
        st.header("💧 Drawing Liquid")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
- Press the plunger to the **first stop**.
- Insert the tip just 2–3 mm below the liquid surface.
- Release the plunger slowly to draw liquid without bubbles.

✍️ **Practice drawing up liquid into your pipette. Watch for bubbles!**
""")
        with col2:
            youtube_draw_url = "https://youtu.be/TAsEXBQZqzo"
            video_id = youtube_draw_url.split("youtu.be/")[-1]
            embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}&controls=0&modestbranding=1"
            components.html(
                f"""
                <iframe width="100%" height="315"
                    src="{embed_url}"
                    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
                </iframe>
                """,
                height=320,
            )

        answer2 = st.radio("Which stop do you press to when drawing liquid?", ["First Stop", "Second Stop"], index=None, key="draw_check")
        if answer2 == "First Stop":
            st.success("Correct! The first stop is for drawing liquid, ensuring you only aspirate the set volume. ✅")
        elif answer2:
            st.warning("Not quite. Pressing to the second stop before drawing will lead to an incorrect (too large) volume. 🤔")

    # TAB 5: Dispense Liquid
    with tabs[5]:
        st.header("⚡ Dispensing Liquid")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
- Press gently to the **first stop**.
- Press to the **second stop** to eject the final drop.
- Remove tip while still pressing down.

✍️ **Now practice dispensing the liquid you just drew up.**
""")
        with col2:
            youtube_expel_url = "https://youtu.be/tF6XdJbuHZY"
            video_id = youtube_expel_url.split("youtu.be/")[-1]
            embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}&controls=0&modestbranding=1"
            components.html(
                f"""
                <iframe width="100%" height="315"
                    src="{embed_url}"
                    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
                </iframe>
                """,
                height=320,
            )

        answer3 = st.radio("Which stop do you press to when fully dispensing?", ["First Stop", "Second Stop"], index=None, key="dispense_check")
        if answer3 == "Second Stop":
            st.success("Correct! Pressing to the second stop ensures all liquid, including the last drop, is dispensed. ✅")
        elif answer3:
            st.warning("Not quite. You need to press further to dispense completely and accurately. 🤔")

    # TAB 6: Viscous Solutions
    with tabs[6]:
        st.header("🧴 Handling Viscous Solutions")
        st.markdown("""
- Pre-wet the tip before aspirating.
- Aspirate and dispense **slowly**.
- Be patient — viscous liquids move slower than water!

✍️ **Try pipetting the corn syrup you've been provided. Be slow and steady.**
""")
        answer4 = st.radio("When pipetting viscous liquids, should you pipette faster or slower?", ["Faster", "Slower"], index=None, key="viscous_check")
        if answer4 == "Slower":
            st.success("Correct! Slower aspiration and dispensing are essential for viscous solutions to ensure accuracy and prevent bubbles. ✅")
        elif answer4:
            st.warning("Not quite. Viscous liquids need more time to move through the tip due to their thickness. Please try again! 🤔")

    # TAB 7: Common Errors
    with tabs[7]:
        st.header("🚨 Common Pipetting Mistakes")
        st.markdown("""
- Pressing to second stop before drawing = too much volume
- Letting go too fast = air bubbles
- Pipetting at wrong angle = inaccurate volume
- Not changing tips = contamination
""")
        mistakes = st.checkbox("✅ I understand how to avoid common pipetting mistakes!")

    # TAB 8: Practice & Reflection
    with tabs[8]:
        st.header("🏋️ Practice Challenge + Reflection")
        st.markdown("""
Take turns using the P200 and P1000 to pipette water and corn syrup into a weigh boat. Record your measured weights and compare them to the target weight using percent error.

🎯 **Target volumes**  
- P200: 100 µL  
- P1000: 1000 µL  
""")
        st.subheader("✍️ Reflection Questions")
        reflection1 = st.text_area("1. Why is pipetting accuracy important in biotechnology?")
        reflection2 = st.text_area("2. Which pipette or solution was hardest to use accurately and why?")
        if st.button("✅ Submit Reflection"):
            st.success("Great job! Your reflections have been submitted.")
