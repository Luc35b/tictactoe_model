# Tic-Tac-Toe AI (GUI Version)

A machine learning-powered Tic-Tac-Toe game built in Python using `tkinter` and `scikit-learn`. This project lets you play against a trained neural network AI in a graphical interface. Includes a scoreboard and restart button for replayability!

---

## Features

- Play as "X" against a AI "O"
- Restart the game anytime with a button
- Scoreboard tracking: Player wins, AI wins, and Ties
- ML model trained using `sklearn`'s MLPClassifier
- Dataset generation included (10,000 random games)

---

## Project Structure

```bash
tictactoe_model/
│
├── generate_dataset.py # Creates tictac_single.txt with training data
├── train_model.py # Trains and saves the AI model to tictac_model.pkl
├── gui.py # GUI game interface
├── tictac_single.txt # Training dataset (generated)
└── tictac_model.pkl # Trained AI model (generated)
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tictactoe_gui_ai.git
cd tictactoe_gui_ai
```

2. Install Requirements

```bash
pip install scikit-learn numpy pandas joblib
```

3. Generate Dataset & Train Model

```bash
python generate_dataset.py
python train_model.py
```

This will create tictac_single.txt and tictac_model.pkl.

4. Run the GUI

```bash
python gui.py
```

How the AI Works
The AI model is trained using MLPClassifier from scikit-learn

It learns from 10,000+ board configurations and corresponding optimal moves

During gameplay, it uses predict_proba() to choose the most likely successful move
