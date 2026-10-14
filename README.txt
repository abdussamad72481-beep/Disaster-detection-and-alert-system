TWO AI PROJECTS FOR FIRST-YEAR BTECH CSE
========================================

PROJECT 1: MACHINE LEARNING — Student Practice Score Predictor
- Algorithm: Linear Regression (scikit-learn)
- Inputs: study hours per day and attendance percentage
- Output: estimated practice score
- Uses a tiny illustrative dataset for learning, not real student decisions.

PROJECT 2: DEEP LEARNING — Handwritten Digit Classifier
- Framework: TensorFlow/Keras
- Dataset: MNIST handwritten digits
- Model: Neural network
- Input: 28 x 28 grayscale digit image
- Output: predicted digit from 0 to 9

HOW TO RUN PROJECT 1
1. Install Python 3.10 or 3.11.
2. Open this folder in VS Code.
3. Open Terminal in VS Code.
4. Run:
   pip install -r project1_machine_learning/requirements.txt
5. Run:
   python project1_machine_learning/student_score_predictor.py

HOW TO RUN PROJECT 2
1. In the VS Code terminal, run:
   pip install -r project2_deep_learning/requirements.txt
2. Train the neural network (first run downloads MNIST, so internet is needed):
   python project2_deep_learning/train_model.py
3. Start the web interface:
   streamlit run project2_deep_learning/app.py
4. Open the local address printed in the terminal and upload a clear, centered image of one digit.

NOTE
- TensorFlow is a large package and may take time to install.
- Project 1 is a real basic ML model trained on example data.
- Project 2 is a real neural network trained on MNIST.
- Both are educational demos and can make mistakes.

SHORT VIVA LINES
Machine Learning project:
"My project predicts an estimated practice score using Linear Regression. The model learns a relationship from example data containing study hours, attendance, and practice scores."

Deep Learning project:
"My project recognizes handwritten digits using a neural network made with TensorFlow and Keras. It trains on the MNIST dataset and predicts a digit from 0 to 9."
