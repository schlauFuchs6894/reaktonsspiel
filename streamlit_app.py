import streamlit as st
import time

# Initialisierung
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "reaction_time" not in st.session_state:
    st.session_state.reaction_time = None
if "game_started" not in st.session_state:
    st.session_state.game_started = False

st.title("⏱️ Reaktionsspiel: Drücke bei 3 Sekunden!")

# Start-Knopf
if not st.session_state.game_started:
    if st.button("Start"):
        st.session_state.start_time = time.time()
        st.session_state.game_started = True
        st.session_state.reaction_time = None

# Timer läuft
if st.session_state.game_started:
    elapsed = time.time() - st.session_state.start_time

    # Automatisches Refresh alle 100ms
    st.experimental_rerun() if elapsed < 3 else None

    st.write(f"⏳ Timer: {elapsed:.2f} Sekunden")

    # Reaktions-Knopf
    if st.button(f"Stop bei {elapsed:.2f} s"):
        st.session_state.reaction_time = elapsed
        st.session_state.game_started = False

# Ergebnisanzeige
if st.session_state.reaction_time is not None:
    st.success(f"🎉 Deine Reaktionszeit: {st.session_state.reaction_time:.3f} Sekunden")
