import os
from flask import Flask, render_template, request, session
from flask_session import Session
import numpy as np
from tempfile import mkdtemp

from solver import solve
from standard_game import get_puzzle, grid2string, string2grid, check_answer

app = Flask(__name__)
 
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.secret_key = 'BAD_SECRET_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solver', methods=['POST','GET'])
def input():
    return render_template('input.html')

@app.route("/solution", methods=['GET','POST'])
def solution():
    if request.method == 'POST':
        board_zeroes = np.zeros([9,9], dtype=int)
        board_init = board_zeroes.copy()
        for i in range(9):
            for j in range(9):
                
                try:
                    number = int(request.form.get(f"cell-{ i*9 + j }"))

                    # render error template if out of range inputs
                    if number in range(0,10): 
                        board_init[i,j] = number
                    else:
                        return render_template("error.html", error_string="Please, check that the numbers introduced are correct.")
                    
                except ValueError:
                    board_init[i,j] = 0 # deals with empty spaces

        final, zeroes_remaining = solve(board_init)

        # render error template if the puzzle wasn't solved in 100 iterations
        if zeroes_remaining > 0:
            return render_template("error.html", error_string="Could not find the solution to the puzzle:(")

    return render_template("result.html", final=final)

@app.route("/standard-game")
def standard():
    string_puzzle, string_solution = get_puzzle("data/sudoku.csv")
    session['solution'] = string_solution
    session['puzzle'] = string_puzzle

    board_init = string2grid(string_puzzle)

    return render_template("puzzle.html", board=board_init)

@app.route("/check", methods=['GET','POST'])
def check():
    if request.method == 'POST':
        
        string_puzzle = session['puzzle']
        answer = string2grid(string_puzzle) # initialize grid with initial default numbers
    
        for i in range(9):
            for j in range(9):
                if answer[i,j] == 0: 
                    try:
                        number = int(request.form.get(f"cell-{ i*9 + j }"))
                        print('hay algun numero', number)

                        # render error template if out of range inputs
                        if number in range(0,10): 
                            answer[i,j] = number
                        else:
                            return render_template("error.html", error_string="Please, check that the numbers introduced are correct.")
                        
                    except ValueError:
                        answer[i,j] = 0 # deals with empty spaces

        # check the answer with the solution
        string_answer = grid2string(answer)
        string_solution = session['solution']

        errors = check_answer(string_answer, string_solution)
        
        if errors == 0:
            return render_template("stats.html", stats_string="Congratulations, you have successfully solved the sudoku:)")
        else:
            return render_template("stats.html", stats_string=f"You have made {errors} mistakes, try again:(")



if __name__ == '__main__':
    app.run(debug=True)
