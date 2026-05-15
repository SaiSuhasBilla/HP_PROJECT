# ⚡ Harry Potter AI Wizard Guesser

An interactive, web-based intelligent guessing game (Akinator clone) that reads your mind to guess any Harry Potter character you think of. The project utilizes **Streamlit** for a reactive user interface and **Scikit-Learn (Decision Trees)** to dynamically optimize the questions asked based on your remaining character pool.

---

## 🚀 Key Features

* **Dynamic Decision-Tree Optimization**: Instead of using hardcoded question paths, an isolated `DecisionTreeClassifier` trains on the remaining character pool at every single turn. It calculates the absolute mathematically best feature to split on next.
* **On-the-Fly Filtering**: Watch the remaining possibilities count dynamically shrink as you answer.
* **State Preservation**: Built with Streamlit's `session_state` to prevent unnecessary re-runs, creating a seamless and snappy UI gameplay loop.
* **Fully Local & Air-gapped**: Reads directly from your specialized, pre-processed dataset (`hp_modified.csv`) without needing API keys or active internet connections during gameplay.

---

## 🛠️ Project Architecture

The codebase cleanly isolates the algorithmic math from the rendering layers, following a strict separation of concerns pattern:

```text
hp_akinator/
├── app.py             # UI Rendering, State management, Button event logic
├── backend.py         # Machine Learning Engine & custom mathematical splitting
├── hp_modified.csv    # Your finalized, curated, binary character dataset
└── README.md          # Project documentation

<img width="813" height="427" alt="Screenshot_16-5-2026_11157_localhost" src="https://github.com/user-attachments/assets/68411bb0-8331-4c79-a0ef-c479c449f1fe" />

<img width="804" height="382" alt="Screenshot_16-5-2026_11215_localhost" src="https://github.com/user-attachments/assets/53c17630-747a-47d5-adc7-41d1c4cd66d3" />

<img width="824" height="356" alt="Screenshot_16-5-2026_11234_localhost" src="https://github.com/user-attachments/assets/fa474184-67ea-4d06-b0b0-f12206ce3760" />

