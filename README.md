Usability Testing Analysis with Mouse Tracking and Facial Expressions
===

The ultimate aim of the project is to combine concepts from two different worlds : software engineering 👩🏻‍💻 and AI 🤖, to create a smart software for facilitating usability testing analysis by using mouse tracking and facial expressions.

The goal of the project is to answer the following question: How can we support the usability testing process with data to help determine if a system is usable or not 📈? This can be achieved by leveraging the power of AI.

The mechanics of the solution are as follows: The software generates a real-time plot that shows changes in the user's facial expressions during the performance of required tasks😊. Additionally, it tracks and compares the user's mouse movements to a standard path, saving the results for analysis 🎮. 

## Dependence 📋
- pyautogui
- keyboard
- Pillow
- screeninfo
- opencv-python
- fer
- tensorflow

## Installation
1. Clone the repository
```
git clone https://github.com/sana-shamma/AI385-Automated-Usability-Testing-Mouse-Tracking-Facial-Expressions.git
```
2. Navigate to the project directory
```
cd AI385-Automated-Usability-Testing-Mouse-Tracking-Facial-Expressions/Code
```
3. Install the required dependencies from requirements.txt
```
pip install -r requirements.txt
```

## Directory Hierarchy 📂
```
|—— main1.py
|—— main2.py
|—— mouse_positions.txt
|—— mouse_positions_referance.txt
|—— output.png
|—— referance_image.png
|—— requirements.txt
|—— utilities
|    |—— DB_utilities.py
|    |—— emotion_utilities.py
|    |—— generate_screenshot.py
|    |—— graph_utilities.py
|    |—— mouse_tracking.py
|    |—— statistics_utilities.py
|    |—— task_usability.py
|    |—— usability_by_emotion.py

```
## Usage

To run the project, follow these steps in **order** :

1. Go to main2.py and assign values to the ``` database_name, user_name, and password ``` variables.
2. Go to mouse_positions_reference.txt and paste the typical path coordinates. (**hint**: you can use mouse_tracking.py to get the coordinates.)
3. Run main1.py.
```
Python main1.py
```
4. Run main2.py. (open other terminal)
```
Python main2.py
```
5. Close the main1.py by clicking the "esc" button.
6. Close the main2.py by clicking the "q" button.
7. Check the result from the database.

## Contributors ✍️

- Jana Aldubai
- Sana Shamma
- Salwa Shama
- Samah Shama

