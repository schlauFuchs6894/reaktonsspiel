import streamlit as st
import time

# Initialisierung der Session-Variablen
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0.0
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

# Funktion zum Starten des Timers
def start_timer():
    st.session_state.start_time = time.time()
    st.session_state.timer_running = True

# Funktion zum Stoppen des Timers
def stop_timer():
    if st.session_state.start_time:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
    st.session_state.timer_running = False

st.title("⏱️ Reaktionsspiel: Drücke bei 3 Sekunden!")

# Start-Button
if st.button("Start"):
    start_timer()

# Timer-Anzeige
if st.session_state.timer_running:
    current_time = time.time()
    elapsed = current_time - st.session_state.start_time
    st.write(f"⏳ Zeit: {elapsed:.2f} Sekunden")

    # Automatisches Stoppen bei 3 Sekunden
    if elapsed >= 3:
        stop_timer()

# Stop-Button mit Zeitanzeige
if st.session_state.timer_running:
    if st.button(f"Stop bei {time.time() - st.session_state.start_time:.2f} s"):
        stop_timer()

# Ergebnisanzeige
if not st.session_state.timer_running and st.session_state.elapsed_time > 0:
    st.success(f"🎉 Deine Reaktionszeit: {st.session_state.elapsed_time:.3f} Sekunden")
