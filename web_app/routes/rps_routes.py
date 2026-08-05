# this is the "web_app/routes/rps_routes.py" file...

from flask import Blueprint, request, render_template
from app.rps import determine_winner, generate_random_choice

rps_routes = Blueprint("rps_routes", __name__)

@rps_routes.route("/rps/form")
def form():
    print("RPS FORM...")
    return render_template("rps_form.html")

@rps_routes.route('/rps/results', methods=['POST'])
def results():
    print("RPS RESULTS...")
    print(dict(request.form))

    # Get the user's choice from the form data
    user_choice = request.form.get('user_choice')
    computer_choice = generate_random_choice()
    outcome = determine_winner(user_choice, computer_choice)

    return render_template("rps_results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        outcome=outcome
    )
