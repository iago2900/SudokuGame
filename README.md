# SUDOKU GAME
## Video Demo: 

https://youtu.be/aAy_zpy35TQ

## Description

The Sudoku Solver Web App is a dynamic and engaging platform developed using HTML, CSS, and powered by the Flask framework in Python. This application brings the classic game of Sudoku to the digital realm, offering users two distinct modes of play.

## Features

### Standard Mode

- In this mode, users are presented with a randomly selected Sudoku puzzle from the app's extensive database.
- Users can attempt to solve the puzzle by inputting their answers directly into the interface.
- Once the user submits their answers, the app evaluates the response against the correct solution and provides immediate feedback.
- The feedback includes information on the number of errors made or a confirmation of successful completion.

### Solver Mode

- This mode empowers users to input their own Sudoku puzzles that they are unable to solve.
- Behind the scenes, a powerful algorithm processes the puzzle and generates a solution, making even the most challenging puzzles solvable.

## Key Technologies

- **HTML & CSS:** The user interface is designed with clean and intuitive HTML for structure and CSS for styling, ensuring a seamless user experience.
- **Flask Framework:** The web application leverages Flask, a powerful Python framework, to handle routing, request handling, and data management.
- **Python Algorithm:** The app boasts a sophisticated Sudoku-solving algorithm, allowing users to crack the toughest puzzles effortlessly.

## How to Use

1. Visit the Sudoku Solver Web App through your preferred web browser.
2. Choose between the "Standard Mode" for a random puzzle or "Solver Mode" to input your own puzzle.
3. Engage with the interactive interface to solve or generate Sudoku puzzles effortlessly.
4. Receive immediate feedback on your progress and enjoy the satisfaction of mastering this mind-bending game.

## Benefits

- Enhances cognitive skills, including critical thinking and problem-solving abilities.
- Provides an enjoyable and challenging pastime for users of all ages.
- Offers a unique platform to test and improve Sudoku-solving skills.

Experience the Sudoku Solver Web App today and embark on a journey of mental stimulation and entertainment!

## File Descriptions

- **data/**
  - Contains a `data.csv` file with 1 million Sudokus and their solutions. This dataset was downloaded from [Kaggle](https://www.kaggle.com/datasets/bryanpark/sudoku).

- **static/**
  - Contains the CSS file responsible for styling the web pages.

- **templates/**
  - Contains all the HTML files:
    - `base.html`: Contains the basic configuration of the page, and all other HTML files extend from this one.

- **Solver.py**
  - Contains functions for the algorithm used to solve a given Sudoku. This file is utilized in the Solver Mode of the application.

- **Standard_game.py**
  - Contains functions responsible for loading random Sudokus from the CSV file, displaying them to the user, and checking the user's answers. This file is used in the Standard Game Mode.

- **App.py**
  - Contains all the routes of the web application and orchestrates the flow of the application.

