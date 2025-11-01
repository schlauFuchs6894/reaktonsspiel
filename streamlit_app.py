import streamlit as st
import time
import random

st.title("🕹️ Reaktionsspiel: Drücke bei 3!")

if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "number" not in st.session_state:
    st.session_state.number = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "reaction_time" not in st.session_state:
    st.session_state.reaction_time = None

def start_game():
    st.session_state.game_started = True
    st.session_state.reaction_time = None
    st.session_state.number = None
    st.session_state.start_time = None

    st.write("Bereit... gleich geht's los!")
    time.sleep(random.uniform(2, 5))  # Zufällige Wartezeit
    st.session_state.number = random.randint(1, 3)
    st.session_state.start_time = time.time()

start_button = st.button("Spiel starten", on_click=start_game)

if st.session_state.game_started and st.session_state.number is not None:
    st.write(f"Zahl: **{st.session_state.number}**")

    if st.session_state.number == 3:
        if st.button("Jetzt drücken!"):
            st.session_state.reaction_time = time.time() - st.session_state.start_time
            st.write(f"🎉 Deine Reaktionszeit: **{st.session_state.reaction_time:.3f} Sekunden**")
            st.session_state.game_started = False
    else:
        st.write("Nicht drücken! Das war nicht die 3.")
        if st.button("Gedrückt..."):
            st.write("❌ Falsch gedrückt! War nicht die 3.")
            st.session_state.game_started = False
