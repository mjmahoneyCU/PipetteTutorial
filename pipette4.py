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
- **Volume adjustment dial** - **Volume display window** - **Tip ejector button** - **Shaft (where the tip fits)**
""")
        st.info("💡 **Take a moment to locate each part on the actual micropipette at your bench.**")
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

            st.markdown("---")  # Separator after matching feedback

        answer1 = st.radio("Which pipette would you use for 150 µL?", ["P20", "P200", "P1000"], index=None, key="volume_check")
        if answer1 == "P200":
            st.success("Correct! P200 (20–200 µL) is the right choice for 150 µL. ✅")
        elif answer1:
            st.warning("Not quite. That pipette's range doesn't cover 150 µL. Please try again! 🤔")

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
            # Video for "Attach Tip"
            # Using components.html for embedding with autoplay and loop as requested previously,
            # though standard st.video is usually simpler if custom HTML is not strictly needed.
            # Replace the src URL with your actual YouTube embed URL.
            # Example: https://www.youtube.com/embed/YOUR_VIDEO_ID?autoplay=1&loop=1&playlist=YOUR_VIDEO_ID&controls=0
            # Note: For 'loop' to work with 'autoplay', 'playlist' parameter usually needs to be set to the video ID itself.
            youtube_attach_url = "https://youtu.be/CJWCM9kM-YE"  # Your Attach Tip video URL

            # Using a simplified embed URL structure if it's a standard YouTube share link
            # You might need to get the actual embed URL from YouTube's "Embed" share option
            # or extract the video ID and build the embed URL.
            # Let's assume the provided URL is a direct share link like http://www.youtube.com/watch?v=CJWCM9kM-YE8 or http://www.youtube.com/watch?v=CJWCM9kM-YE9

            # Attempt to extract video ID for robust embed URL
            video_id_attach = youtube_attach_url.split('/')[-1]  # Tries to get ID if URL is http://youtube.com/watch?v=00
            if 'http://youtube.com/watch?v=01' in youtube_attach_url:  # Handle common share link format
                video_id_attach = youtube_attach_url.split('=')[-1]

            embed_src_attach = f"https://www.youtube.com/embed/{video_id_attach}?autoplay=1&loop=1&playlist={video_id_attach}&controls=0&modestbranding=1"

            components.html(
                f"""
            <iframe width="100%" height="315"
                src="{embed_src_attach}"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
            </iframe>
            """,
                height=320,
            )

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
            # Video for "Drawing Liquid"
            youtube_draw_url = "https://youtu.be/TAsEXBQZqzo"  # Your Draw video URL
            video_id_draw = youtube_draw_url.split('/')[-1]
            if 'http://youtube.com/watch?v=01' in youtube_draw_url:
                video_id_draw = youtube_draw_url.split('=')[-1]

            embed_src_draw = f"https://www.youtube.com/embed/{video_id_draw}?autoplay=1&loop=1&playlist={video_id_draw}&controls=0&modestbranding=1"

            components.html(
                f"""
            <iframe width="100%" height="315"
                src="{embed_src_draw}"
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
            # Video for "Dispensing Liquid" (Expel)
            youtube_expel_url = "https://youtu.be/tF6XdJbuHZY"  # Your Expel video URL
            video_id_expel = youtube_expel_url.split('/')[-1]
            if 'http://youtube.com/watch?v=01' in youtube_expel_url:
                video_id_expel = youtube_expel_url.split('=')[-1]

            embed_src_expel = f"https://www.youtube.com/embed/{video_id_expel}?autoplay=1&loop=1&playlist={video_id_expel}&controls=0&modestbranding=1"

            components.html(
                f"""
            <iframe width="100%" height="315"
                src="{embed_src_expel}"
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

    # --- Viscous Solutions ---
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

        st.info("""
        **Remember: Converting Volume to Weight**

        - Remember that **1 mL is also equal to 1000 microliters (µL)**.
        - Water has a density of **1 gram per milliliter (g/mL)**.
        - One grams is equal to 1000 milligrams and 1 mililiter is equal to 1000 microliters (µl).
        - That means you can also express the density of water as 1 mg per µl.
        - That means **1 microliter (µL)** of water weighs about **1 milligram (mg)** or **0.001 grams (g)**.
        - **Corn syrup has a density of approximately 1.38 g/mL (or 1.38 mg/µL)**.

        ✍️ **So:**
        - **For Water:**
        - 100 µL = 100 mg = 0.100 g
        - 10 µL = 10 mg = 0.010 g
        - 1000 µL = 1000 mg = 1.000 g
        
        - **For Corn Syrup (approximate):**
        - 100 µL ≈ 138 mg ≈ 0.138 g
        - 10 µL ≈ 13.8 mg ≈ 0.0138 g
        - 1000 µL ≈ 1380 mg ≈ 1.380 g
        """)

        st.markdown("---")
        st.subheader("📊 Your Pipetting Performance:")
        st.markdown("""
        **Understanding Percent Error:**

        Percent error tells you how close your measured value is to the true (target) value. It helps you understand the accuracy of your pipetting.
        """)

        # This is the updated formatting for the equation using st.latex()
        st.latex(r" \text{Percent Error} = \frac{|\text{Measured Value} - \text{True Value}|}{\text{True Value}} \times 100\% ")

        # Updated text for percent error criteria
        st.markdown("""
        For pipetting, your 'Measured Value' is the average weight you get from your trials, and your 'True Value' is the target weight (converted from your target volume).

        **What’s a good percent error?**
        - Below **15%** = Excellent accuracy! ✅
        - Above **15%** = Let’s work on it! ❌

        ---

        **Standard Deviation:**
        - Tells us how spread out your measurements are.
        - A small value means your pipetting is consistent.
        - A large value means some trials are way off — try to be more steady and repeatable.
        """)

        st.markdown("---")  # Separator after the explanation block for clarity

        pipettes = ["P20", "P200", "P1000"]
        water_targets = {"P20": 0.010, "P200": 0.100, "P1000": 1.000}  # in grams for water
        corn_syrup_targets = {"P20": 0.0138, "P200": 0.138, "P1000": 1.380}  # in grams for corn syrup (using 1.38 g/mL density)
        data = {}

        # --- Water Measurements ---
        st.subheader("💧 Water Measurements")
        for pipette in pipettes:
            st.subheader(f"{pipette} Practice with Water - Target Volume: {int(water_targets[pipette] * 1000)} µL")
            st.markdown(f"*(Expected weight: {water_targets[pipette]:.3f} g)*")
            entries = []
            for i in range(1, 6):
                weight = st.number_input(f"Water {pipette} Entry {i} (g)", min_value=0.0, max_value=2.0, step=0.001, format="%.3f", key=f"water_{pipette}_weight_{i}")
                entries.append(weight)

            entries_np = np.array(entries)
            non_default_entries = entries_np[entries_np != 0.0]

            if len(non_default_entries) > 0:
                mean_weight = np.mean(non_default_entries)
                std_weight = np.std(non_default_entries)

                if water_targets[pipette] > 0:
                    percent_error = (abs(mean_weight - water_targets[pipette]) / water_targets[pipette]) * 100
                else:
                    percent_error = np.nan

                st.write(f"**Average measured weight for {pipette} (Water):** {mean_weight:.3f} g")
                st.write(f"**Standard deviation (consistency check) for {pipette} (Water):** {std_weight:.3f} g")
                st.write(f"**Target weight (Water):** {water_targets[pipette]:.3f} g")

                if not np.isnan(percent_error):
                    if percent_error <= 15.0:  # Updated threshold to 15%
                        st.success(f"**Percent Error (Water):** {percent_error:.2f}% ✅ Excellent accuracy!")
                    else:  # Otherwise, it's above 15%
                        st.error(f"**Percent Error (Water):** {percent_error:.2f}% ❌ Try again — review technique!")
                else:
                    st.info("Percent Error: N/A")

                fig, ax = plt.subplots(figsize=(8, 4))
                ax.bar(range(1, len(non_default_entries) + 1), non_default_entries, color='skyblue')
                ax.axhline(mean_weight, color='r', linestyle='--', label=f'Mean ({mean_weight:.3f}g)')
                ax.axhline(water_targets[pipette], color='g', linestyle=':', label=f'Target ({water_targets[pipette]:.3f}g)')
                ax.set_title(f"{pipette} Weights (Water, Target {int(water_targets[pipette]*1000)} µL)")
                ax.set_xlabel("Trial Number")
                ax.set_ylabel("Measured Weight (g)")
                ax.set_ylim(bottom=0)
                ax.legend()
                ax.grid(axis='y', linestyle='--', alpha=0.7)
                st.pyplot(fig)
                plt.close(fig)

                data[f"water_{pipette}_mean"] = mean_weight
                data[f"water_{pipette}_std"] = std_weight
                data[f"water_{pipette}_percent_error"] = percent_error
            else:
                st.info("Enter your measured weights (to 3 decimal places) above to see calculations and plot for water.")

        st.markdown("---")
        st.subheader("🍯 Corn Syrup Measurements")
        # --- Corn Syrup Measurements ---
        for pipette in pipettes:
            st.subheader(f"{pipette} Practice with Corn Syrup - Target Volume: {int(corn_syrup_targets[pipette] * 1000 / 1.38)} µL (approx.)")  # Display approximate µL
            st.markdown(f"*(Expected weight: {corn_syrup_targets[pipette]:.3f} g)*")
            entries = []
            for i in range(1, 6):
                weight = st.number_input(f"Corn Syrup {pipette} Entry {i} (g)", min_value=0.0, max_value=2.0, step=0.001, format="%.3f", key=f"corn_syrup_{pipette}_weight_{i}")
                entries.append(weight)

            entries_np = np.array(entries)
            non_default_entries = entries_np[entries_np != 0.0]

            if len(non_default_entries) > 0:
                mean_weight = np.mean(non_default_entries)
                std_weight = np.std(non_default_entries)

                if corn_syrup_targets[pipette] > 0:
                    percent_error = (abs(mean_weight - corn_syrup_targets[pipette]) / corn_syrup_targets[pipette]) * 100
                else:
                    percent_error = np.nan

                st.write(f"**Average measured weight for {pipette} (Corn Syrup):** {mean_weight:.3f} g")
                st.write(f"**Standard deviation (consistency check) for {pipette} (Corn Syrup):** {std_weight:.3f} g")
                st.write(f"**Target weight (Corn Syrup):** {corn_syrup_targets[pipette]:.3f} g")

                if not np.isnan(percent_error):
                    if percent_error <= 15.0:  # Updated threshold to 15%
                        st.success(f"**Percent Error (Corn Syrup):** {percent_error:.2f}% ✅ Excellent accuracy!")
                    else:  # Otherwise, it's above 15%
                        st.error(f"**Percent Error (Corn Syrup):** {percent_error:.2f}% ❌ Try again — review technique!")
                else:
                    st.info("Percent Error: N/A")

                fig, ax = plt.subplots(figsize=(8, 4))
                ax.bar(range(1, len(non_default_entries) + 1), non_default_entries, color='orange')  # Different color for corn syrup
                ax.axhline(mean_weight, color='r', linestyle='--', label=f'Mean ({mean_weight:.3f}g)')
                ax.axhline(corn_syrup_targets[pipette], color='g', linestyle=':', label=f'Target ({corn_syrup_targets[pipette]:.3f}g)')
                ax.set_title(f"{pipette} Weights (Corn Syrup, Target {int(corn_syrup_targets[pipette]*1000/1.38)} µL)")
                ax.set_xlabel("Trial Number")
                ax.set_ylabel("Measured Weight (g)")
                ax.set_ylim(bottom=0)
                ax.legend()
                ax.grid(axis='y', linestyle='--', alpha=0.7)
                st.pyplot(fig)
                plt.close(fig)

                data[f"corn_syrup_{pipette}_mean"] = mean_weight
                data[f"corn_syrup_{pipette}_std"] = std_weight
                data[f"corn_syrup_{pipette}_percent_error"] = percent_error
            else:
                st.info("Enter your measured weights (to 3 decimal places) above to see calculations and plot for corn syrup.")

        st.markdown("---")
        st.subheader("Reflection")
        reflection1 = st.text_area("1. Why is pipetting accuracy important in biotechnology?")
        reflection2 = st.text_area("2. Which pipette or solution was hardest to use accurately and why?")

        if st.button("🚀 Finish Practice!"):
            st.success("✅ Great job completing your pipetting practice!")
            st.balloons()

            # Prepare DataFrame for CSV Export
            results_data = []
            for pipette in pipettes:
                results_data.append({
                    "Team Name": team_name,
                    "Pipette": pipette,
                    "Liquid": "Water",
                    "Mean (g)": data.get(f"water_{pipette}_mean", np.nan),
                    "Std Dev (g)": data.get(f"water_{pipette}_std", np.nan),
                    "Percent Error": data.get(f"water_{pipette}_percent_error", np.nan)
                })
                results_data.append({
                    "Team Name": team_name,
                    "Pipette": pipette,
                    "Liquid": "Corn Syrup",
                    "Mean (g)": data.get(f"corn_syrup_{pipette}_mean", np.nan),
                    "Std Dev (g)": data.get(f"corn_syrup_{pipette}_std", np.nan),
                    "Percent Error": data.get(f"corn_syrup_{pipette}_percent_error", np.nan)
                })

            results_df = pd.DataFrame(results_data)

            st.markdown("---")
            st.subheader("📁 Download Your Results")

            csv = results_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download CSV of Your Results",
                data=csv,
                file_name=f"pipetting_results_{team_name.replace(' ', '_')}.csv",
                mime="text/csv"
            )

else:
    st.warning("👆 Please enter your team name above to start.")
