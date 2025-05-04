import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- CONFIG ---
st.set_page_config(page_title="Buffs Biotech: Pipetting Masterclass", layout="wide")

# --- STUDENT NAME ---
name = st.text_input("Enter your name or nickname to track your progress:")
partner = st.text_input("Enter your lab partner's name:")

if name and partner:
    st.success(f"Welcome {name} and {partner}! Let's master pipetting.")

    tabs = st.tabs([
        "Intro", "Parts of Pipette", "Set Volume", "Attach Tip", "Draw Liquid",
        "Dispense Liquid", "Viscous Solutions", "Common Errors", "Practice & Reflection"
    ])

    with tabs[0]:
        st.header("📘 Introduction to Pipetting")
        st.markdown("""
Micropipettes allow scientists to transfer tiny liquid volumes precisely — critical for every biotech lab!
Today, you will learn **how to pipette accurately**, fix common mistakes, and test your skills.
""")

    with tabs[1]:
        st.header("🔩 Parts of a Micropipette")
        st.markdown("""
- **Plunger** (pushes and releases liquid)  
- **Volume adjustment dial**  
- **Volume display window**  
- **Tip ejector button**  
- **Shaft (where the tip fits)"
""")
        col1, col2 = st.columns(2)
        with col1:
            st.image("pipettor.png", caption="Labeled micropipette", use_container_width=True)
        with col2:
            st.image("pipette_box.png", use_container_width=True)

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

        pipetteA = st.selectbox("Pipette A displays:", volume_options, key="pipetteA")
        pipetteB = st.selectbox("Pipette B displays:", volume_options, key="pipetteB")
        pipetteC = st.selectbox("Pipette C displays:", volume_options, key="pipetteC")
        pipetteD = st.selectbox("Pipette D displays:", volume_options, key="pipetteD")

        if st.button("Check My Matching Answers"):
            correct_answers = {
                "pipetteA": "800 µL",
                "pipetteB": "200 µL",
                "pipetteC": "100 µL",
                "pipetteD": "2 µL"
            }
            score = sum([
                pipetteA == correct_answers["pipetteA"],
                pipetteB == correct_answers["pipetteB"],
                pipetteC == correct_answers["pipetteC"],
                pipetteD == correct_answers["pipetteD"]
            ])
            st.success(f"You got {score} out of 4 matches correct!")

        answer1 = st.radio("Which pipette would you use for 150 µL?", ["P20", "P200", "P1000"], key="volume_check")

    with tabs[3]:
        st.header("🧪 Attaching the Tip")
        st.markdown("""
- Push the pipette firmly into the correct color tip:
  - Clear for P20
  - Yellow for P200
  - Blue for P1000
- Listen for a soft 'click' to confirm attachment.

✍️ **Now practice adding tips to your pipettes at your bench.**
""")

    with tabs[4]:
        st.header("💧 Drawing Liquid")
        st.markdown("""
- Press the plunger to the **first stop**.
- Insert the tip just 2–3 mm below the liquid surface.
- Release the plunger slowly to draw liquid without bubbles.

✍️ **Practice drawing up liquid into your pipette. Watch for bubbles!**
""")
        answer2 = st.radio("Which stop do you press to when drawing liquid?", ["First Stop", "Second Stop"], key="draw_check")

    with tabs[5]:
        st.header("⚡ Dispensing Liquid")
        st.markdown("""
- Press gently to the **first stop** to dispense most liquid.
- Press to the **second stop** to eject the final drop.
- Remove tip while still pressing down.

✍️ **Now practice dispensing the liquid you just drew up.**
""")
        answer3 = st.radio("Which stop do you press to when fully dispensing?", ["First Stop", "Second Stop"], key="dispense_check")

    with tabs[6]:
        st.header("🧴 Handling Viscous Solutions")
        st.markdown("""
- Pre-wet the tip before aspirating.
- Aspirate and dispense **slowly**.
- Be patient — viscous liquids move slower than water!

✍️ **Try pipetting the corn syrup you've been provided. Be slow and steady.**
""")
        answer4 = st.radio("When pipetting viscous liquids, should you pipette faster or slower?", ["Faster", "Slower"], key="viscous_check")

    with tabs[7]:
        st.header("🚨 Common Pipetting Mistakes")
        st.markdown("""
- Pressing to second stop before drawing = too much volume
- Letting go too fast = air bubbles
- Pipetting at wrong angle = inaccurate volume
- Not changing tips = contamination
""")
        mistakes = st.checkbox("✅ I understand how to avoid common pipetting mistakes!")

    with tabs[8]:
        st.header("🏋️ Practice Challenge + Reflection")

        pipettes = ["P20", "P200", "P1000"]
        targets = {"P20": 0.010, "P200": 0.100, "P1000": 1.000}  # Target volumes in grams (assuming 1g/mL density)
        data = {}

        for pipette in pipettes:
            st.subheader(f"{pipette} Practice - Target Volume: {int(targets[pipette]*1000)} µL")
            entries = []
            for i in range(1, 6):
                weight = st.number_input(f"{pipette} Entry {i} (g)", min_value=0.0, max_value=2.0, step=0.001, key=f"{pipette}_weight_{i}")
                entries.append(weight)

            entries_np = np.array(entries)
            mean_weight = np.mean(entries_np)
            std_weight = np.std(entries_np)

            st.write(f"**Average weight for {pipette}:** {mean_weight:.3f} g")
            st.write(f"**Standard deviation for {pipette}:** {std_weight:.3f} g")
            st.write(f"**Target volume:** {targets[pipette]:.3f} g")

            fig, ax = plt.subplots()
            ax.bar(range(1, 6), entries)
            ax.axhline(mean_weight, color='r', linestyle='--', label='Mean')
            ax.axhline(targets[pipette], color='g', linestyle=':', label='Target')
            ax.set_title(f"{pipette} Weights")
            ax.set_xlabel("Trial")
            ax.set_ylabel("Weight (g)")
            ax.legend()
            st.pyplot(fig)

            data[f"{pipette}_mean"] = mean_weight
            data[f"{pipette}_std"] = std_weight

        st.markdown("---")
        st.subheader("Reflection")
        reflection1 = st.text_area("1. Why is pipetting accuracy important in biotechnology?")
        reflection2 = st.text_area("2. Which pipette was hardest to use accurately and why?")

        if st.button("🚀 Finish Practice!"):
            st.success("✅ Great job completing your pipetting practice!")

else:
    st.warning("👆 Please enter your name and partner's name above to start.")
