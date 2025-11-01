# 🧠 MindAlly: Your Cognitive Reframe Coach

**An active mind coach that analyzes your thoughts for negative patterns (like "Catastrophizing"). It then provides quick, 2-minute cognitive exercises to help you reframe your mindset in real-time.**

This application is built entirely in **Python** using the **Streamlit** multi-page app framework.

## The Core Idea: Bite-Sized CBT

Many people today feel overwhelmed, anxious, and burnt out. While journaling is helpful, it can feel passive. "MindAlly" is designed to be an **active partner** in your mental health.

Instead of just storing your thoughts, this app uses a concept from **Cognitive Behavioral Therapy (CBT)**. It helps you:
1.  **Identify** the negative thought patterns (cognitive distortions) that get you "stuck."
2.  **Challenge** those thoughts with a simple, guided 2-minute exercise.
3.  **Reframe** your mindset to be more positive and resilient.

---

## ⚙️ How It Works

The app's main loop is simple, fast, and effective:

1.  **Check-In (Home Page):** You write down what's on your mind.
2.  **Analyze:** The app (simulating an NLP model) analyzes your text for keywords related to common cognitive distortions (e.g., "always," "never," "disaster," "everyone thinks").
3.  **Identify:** It tells you what pattern it found, like **"All-or-Nothing Thinking"** or **"Mind Reading,"** and explains what it is.
4.  **Reframe:** It gives you a specific, actionable prompt (e.g., "What is *one small thing* that was *not* a complete failure?") to help you challenge that thought.
5.  **Grow:** When you complete the exercise, a new plant is added to your virtual **"Mind Garden,"** providing a visual reward for your progress.

---

## ✨ Key Features

This app is split into three main pages:

* **🏠 Home:** The main check-in page. This is where you share your thoughts, get them analyzed, and perform the "reframe" exercises.
* **🧰 Toolkit:** Proactive tools for when you're not checking in.
    * **SOS Panic Button:** A 1-minute guided breathing exercise for immediate stress relief.
    * **Focus Timer:** A simple timer to help you focus on work, meditation, or just being present.
    * **Guided Reframes:** A library of common negative thoughts (e.g., about work, relationships) and examples of how to challenge them.
* **🌳 My Mind Garden:** A gamified progress tracker. Your garden grows with every exercise you complete, turning your mental health work into a beautiful, visual representation of your growth.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit (for the multi-page web app)
* **Logic:** The core analysis logic is currently a Python keyword-based system. This can be upgraded with an NLP model (like BERT or a fine-tuned LLM) in the future.

---

## 📁 Project Structure

This project uses Streamlit's multi-page app structure. Your main script (`Home.py`) is in the root folder, and all other pages are in the `pages/` sub-folder.

## 🚀 How to Run Locally

Get this application running on your local machine in 4 simple steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
    cd YOUR_REPOSITORY
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the environment
    python -m venv venv
    
    # On Windows:
    .\venv\Scripts\activate
    
    # On macOS/Linux:
    source vVenv/bin/activate
    ```

3.  **Install the dependencies:**
    (The `requirements.txt` file should contain one word: `streamlit`)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run Home.py
    ```

Your default web browser will automatically open with the running application.
