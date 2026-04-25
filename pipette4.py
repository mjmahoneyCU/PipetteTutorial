import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(page_title="Pipetting Tutorial", layout="wide")

# --- STYLING ---
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
h2, h3 {
    color: #1a1a1a;
    border-bottom: 2px solid #CFB87C;
    padding-bottom: 0.25rem;
}
.stButton > button {
    background-color: #CFB87C;
    color: #000000;
    border: none;
    font-weight: 600;
}
.stButton > button:hover {
    background-color: #b8a269;
    color: #000000;
}
</style>
""", unsafe_allow_html=True)

# --- DEPARTMENT BANNER ---
st.image("CBEN.png", use_container_width=True)

# --- PAGE TITLE ---
st.title("Pipetting Tutorial")


# --- REUSABLE FUNCTION FOR PRACTICE BLOCKS ---
def pipette_practice_block(team_member, pipette_type, liquid, target_grams, bar_color, data_dict):
    """Render one pipetting practice block and update the shared data dictionary."""
    if liquid == "Water":
        target_uL = int(target_grams * 1000)
    else:
        target_uL = int(target_grams * 1000 / 1.38)

    st.subheader(f"{pipette_type} Practice with {liquid} — Team Member {team_member}")
    st.caption(f"Target volume: {target_uL} µL  |  Expected weight: {target_grams:.3f} g")

    key_prefix = f"{liquid.lower().replace(' ', '_')}_{pipette_type}_TM{team_member}"
    entries = []
    cols = st.columns(5)
    for i, col in enumerate(cols, 1):
        with col:
            weight = st.number_input(
                f"Trial {i}",
                min_value=0.0, max_value=2.0, step=0.001,
                format="%.3f",
                key=f"{key_prefix}_weight_{i}"
            )
            entries.append(weight)

    valid = np.array([e for e in entries if e > 0])
    if len(valid) == 0:
        st.info("Enter measurements above to see your results.")
        st.markdown("---")
        return

    mean = np.mean(valid)
    std = np.std(valid)

    metric_cols = st.columns(3)
    metric_cols[0].metric("Mean", f"{mean:.3f} g")
    metric_cols[1].metric("Std Dev", f"{std:.3f} g")

    if liquid == "Water":
        pct_err = abs(mean - target_grams) / target_grams * 100
        metric_cols[2].metric("Percent Error", f"{pct_err:.1f}%")

        if pct_err <= 3:
            st.success("Within professional tolerance — excellent accuracy.")
        elif pct_err <= 10:
            st.info("Accurate for lab practice. In a real experiment, you'd want to tighten this further.")
        else:
            st.warning("Accuracy is off — review your technique and try again.")

        data_dict[f"{key_prefix}_percent_error"] = pct_err
    else:
        metric_cols[2].metric("Target", f"{target_grams:.3f} g")

        if std <= 0.005:
            st.success("Outstanding consistency.")
        elif std <= 0.020:
            st.info("Good consistency. Keep your pace slow and steady.")
        else:
            st.warning("High variability — focus on a consistent aspiration and dispense speed.")

    # Plot
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.bar(range(1, len(valid) + 1), valid, color=bar_color, edgecolor='#333333', linewidth=0.5)
    ax.axhline(mean, color='#D62728', linestyle='--', linewidth=1.5, label=f'Your mean ({mean:.3f} g)')
    ax.axhline(target_grams, color='#2CA02C', linestyle=':', linewidth=1.5, label=f'Target ({target_grams:.3f} g)')
    ax.set_xlabel("Trial", fontsize=10)
    ax.set_ylabel("Measured weight (g)", fontsize=10)
    ax.set_ylim(bottom=0)
    ax.legend(loc='upper right', fontsize=9, framealpha=0.95)
    ax.grid(axis='y', linestyle=':', alpha=0.4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    st.pyplot(fig)
    plt.close(fig)

    data_dict[f"{key_prefix}_mean"] = mean
    data_dict[f"{key_prefix}_std"] = std
    st.markdown("---")


# --- STUDENT NAME ---
team_name = st.text_input("Enter your team name to track your progress:")
if team_name:
    st.success(f"Welcome Team {team_name}! Let's master pipetting.")

    tabs = st.tabs([
        "Introduction", "Pipette Anatomy", "Setting Volume", "Attaching Tips",
        "Drawing Liquid", "Dispensing", "Viscous Solutions", "Common Errors",
        "Practice & Reflection"
    ])

    with tabs[0]:
        st.header("Introduction to Pipetting")
        st.markdown("""
Micropipettes allow scientists to transfer tiny liquid volumes precisely — critical for every biotech lab.
Today, you will learn **how to pipette accurately**, fix common mistakes, and test your skills.
""")

    with tabs[1]:
        st.header("Parts of a Micropipette")
        st.markdown("""
- **Plunger** (pushes and releases liquid)
- **Volume adjustment dial**
- **Volume display window**
- **Tip ejector button**
- **Shaft** (where the tip fits)
""")
        st.info("Take a moment to locate each part on the actual micropipette at your bench.")
        col1, col2 = st.columns(2)
        with col1:
            st.image("pipettor.png", caption="Labeled micropipette", use_container_width=True)
        with col2:
            st.image("pipette_box.png", use_container_width=True)

    with tabs[2]:
        st.header("Setting the Volume")
        st.markdown("""
- Turn the dial clockwise to decrease, counterclockwise to increase.
- Always stay within the correct range for each pipette:
  - P20: 2–20 µL
  - P200: 20–200 µL
  - P1000: 100–1000 µL
- Rotate slightly past your volume, then dial back for best accuracy.
""")
        st.image("pipette_volumes.png", caption="Pipette volume settings", use_container_width=True)

        st.subheader("Match the Pipette Display to the Correct Volume")
        volume_options = ["Select", "2 µL", "10 µL", "20 µL", "80 µL", "100 µL", "200 µL", "800 µL"]
        correct_answers = {"A": "800 µL", "B": "200 µL", "C": "100 µL", "D": "2 µL"}

        selections = {}
        for label in ["A", "B", "C", "D"]:
            selections[label] = st.selectbox(f"Pipette {label}:", volume_options, index=0, key=f"pipette{label}_q")

        if st.button("Check My Matching Answers", key="check_matching_btn"):
            for label in ["A", "B", "C", "D"]:
                if selections[label] == correct_answers[label]:
                    st.success(f"Pipette {label}: Correct.")
                else:
                    st.warning(f"Pipette {label}: Not quite — try again.")
            st.markdown("---")

        answer1 = st.radio("Which pipette would you use for 150 µL?",
                           ["P20", "P200", "P1000"], index=None, key="volume_check")
        if answer1 == "P200":
            st.success("Correct. P200 (20–200 µL) is the right choice for 150 µL.")
        elif answer1:
            st.warning("Not quite. That pipette's range doesn't cover 150 µL. Try again.")

    with tabs[3]:
        st.header("Attaching the Tip")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
- Push the pipette firmly into the correct color tip:
  - Clear for P20
  - Yellow for P200
  - Blue for P1000
- Listen for a soft 'click' to confirm attachment.

**Now practice adding tips to your pipettes at your bench.**
""")
        with col2:
            video_id = "CJWCM9kM-YE"
            embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}&controls=0&modestbranding=1"
            components.html(
                f"""<iframe width="100%" height="315" src="{embed_url}"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>""",
                height=320,
            )

    with tabs[4]:
        st.header("Drawing Liquid")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
- Press the plunger to the **first stop**.
- Insert the tip just 2–3 mm below the liquid surface.
- Release the plunger slowly to draw liquid without bubbles.

**Practice drawing up liquid into your pipette. Watch for bubbles.**
""")
        with col2:
            video_id = "TAsEXBQZqzo"
            embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}&controls=0&modestbranding=1"
            components.html(
                f"""<iframe width="100%" height="315" src="{embed_url}"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>""",
                height=320,
            )

        answer2 = st.radio("Which stop do you press to when drawing liquid?",
                           ["First Stop", "Second Stop"], index=None, key="draw_check")
        if answer2 == "First Stop":
            st.success("Correct. The first stop aspirates only the set volume.")
        elif answer2:
            st.warning("Not quite. Pressing to the second stop before drawing will pull up too much liquid.")

    with tabs[5]:
        st.header("Dispensing Liquid")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
- Press gently to the **first stop**.
- Press to the **second stop** to eject the final drop.
- Remove the tip while still pressing down.

**Practice dispensing the liquid you just drew up.**
""")
        with col2:
            video_id = "tF6XdJbuHZY"
            embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}&controls=0&modestbranding=1"
            components.html(
                f"""<iframe width="100%" height="315" src="{embed_url}"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>""",
                height=320,
            )

        answer3 = st.radio("Which stop do you press to when fully dispensing?",
                           ["First Stop", "Second Stop"], index=None, key="dispense_check")
        if answer3 == "Second Stop":
            st.success("Correct. The second stop ejects every last drop.")
        elif answer3:
            st.warning("Not quite. You need to press further to fully dispense.")

    with tabs[6]:
        st.header("Handling Viscous Solutions")
        st.markdown("""
- Pre-wet the tip before aspirating.
- Aspirate and dispense **slowly**.
- Be patient — viscous liquids move slower than water.

**Try pipetting the corn syrup you've been provided. Be slow and steady.**
""")
        answer4 = st.radio("When pipetting viscous liquids, should you pipette faster or slower?",
                           ["Faster", "Slower"], index=None, key="viscous_check")
        if answer4 == "Slower":
            st.success("Correct. Slower aspiration keeps volumes accurate and prevents bubbles.")
        elif answer4:
            st.warning("Not quite. Viscous liquids need more time to move through the tip.")

    with tabs[7]:
        st.header("Common Pipetting Mistakes")
        st.markdown("""
- Pressing to the second stop before drawing → too much volume
- Letting go too fast → air bubbles
- Pipetting at the wrong angle → inaccurate volume
- Not changing tips → contamination
""")

    with tabs[8]:
        st.header("Practice Challenge + Reflection")

        with st.expander("Converting Volume to Weight (reference)"):
            st.markdown("""
**Water** has a density of **1 g/mL**, which is the same as **1 mg/µL**. So 1 µL of water weighs about 1 mg (0.001 g).

**Corn syrup** has a density of approximately **1.38 g/mL** (or 1.38 mg/µL).

| Volume | Water weight | Corn syrup weight |
|---|---|---|
| 10 µL | 0.010 g | 0.014 g |
| 100 µL | 0.100 g | 0.138 g |
| 1000 µL | 1.000 g | 1.380 g |
""")

        with st.expander("Understanding Your Results"):
            st.markdown("**Percent Error — how close your average is to the true value.**")
            st.latex(r" \text{Percent Error} = \frac{|\text{Measured} - \text{True}|}{\text{True}} \times 100\% ")
            st.markdown("""
- Below **3%** → within professional tolerance
- 3–10% → accurate for practice, not for a real experiment
- Above 10% → review your technique

**Standard Deviation — how consistent your measurements are.**

A small value means your pipetting is consistent from trial to trial. A large value means your trials are scattered — try to be more steady and repeatable.
""")

        st.markdown("---")

        # Colors and targets
        water_color = "#4A90E2"
        cornsyrup_color = "#CFB87C"
        water_targets = {"P200": 0.100, "P1000": 1.000}
        corn_syrup_targets = {"P200": 0.138, "P1000": 1.380}
        data = {}

        st.header("Water Measurements")
        pipette_practice_block(1, "P200", "Water", water_targets["P200"], water_color, data)
        pipette_practice_block(2, "P200", "Water", water_targets["P200"], water_color, data)
        pipette_practice_block(3, "P1000", "Water", water_targets["P1000"], water_color, data)

        st.header("Corn Syrup Measurements")
        st.warning("For corn syrup, carefully cut the very tip off your pipette tip to make a wider opening. Pipette slowly.")
        pipette_practice_block(1, "P200", "Corn Syrup", corn_syrup_targets["P200"], cornsyrup_color, data)
        pipette_practice_block(2, "P200", "Corn Syrup", corn_syrup_targets["P200"], cornsyrup_color, data)
        pipette_practice_block(3, "P1000", "Corn Syrup", corn_syrup_targets["P1000"], cornsyrup_color, data)

        st.header("Reflection")
        reflection1 = st.text_area("1. Why is pipetting accuracy important in biotechnology?")
        reflection2 = st.text_area("2. Which pipette or solution was hardest to use accurately, and why?")

        # Check how many practice blocks have data
        blocks_filled = sum([
            1 for key in [
                "water_P200_TM1_mean", "water_P200_TM2_mean", "water_P1000_TM3_mean",
                "corn_syrup_P200_TM1_mean", "corn_syrup_P200_TM2_mean", "corn_syrup_P1000_TM3_mean"
            ] if key in data
        ])

        st.markdown("---")
        st.progress(blocks_filled / 6, text=f"{blocks_filled} of 6 practice blocks completed")

        if st.button("Finish Practice"):
            if blocks_filled < 6:
                st.warning(f"You've completed {blocks_filled} of 6 practice blocks. Finish all six before downloading results.")
            else:
                st.success("Practice complete. Your results are ready to download below.")

                results_data = []
                for liquid_label, liquid_key in [("Water", "water"), ("Corn Syrup", "corn_syrup")]:
                    for tm, pip in [(1, "P200"), (2, "P200"), (3, "P1000")]:
                        prefix = f"{liquid_key}_{pip}_TM{tm}"
                        results_data.append({
                            "Team Name": team_name,
                            "Pipette": f"{pip} (TM{tm})",
                            "Liquid": liquid_label,
                            "Mean (g)": data.get(f"{prefix}_mean", np.nan),
                            "Std Dev (g)": data.get(f"{prefix}_std", np.nan),
                            "Percent Error": data.get(f"{prefix}_percent_error", np.nan)
                        })

                results_df = pd.DataFrame(results_data)
                st.dataframe(results_df, use_container_width=True)

                csv = results_df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download CSV of Your Results",
                    data=csv,
                    file_name=f"pipetting_results_{team_name.replace(' ', '_')}.csv",
                    mime="text/csv"
                )

else:
    st.warning("Please enter your team name above to start.")
