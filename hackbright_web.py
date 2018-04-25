"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    project_grade = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
         first=first, last=last, github=github, project_grade=project_grade)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/add-form")
def go_to_form():

	return render_template('new_student.html')

@app.route("/student-add", methods=['POST'])
def student_add():
	"""Add student"""
	first = request.form.get("firstname")
	last = request.form.get("lastname")
	github = request.form.get("github")
	hackbright.make_new_student(first, last, github)

	return render_template('student_added.html',first=first, last=last, github=github)

@app.route('/project')
def project_info():
    """Given project title, return project's description and max grade"""

    title = request.args.get('title')

    print title

    title, description, max_grade = hackbright.get_project_by_title(title)

    return render_template("project_info.html", title=title, description=description, max_grade=max_grade)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
