from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Chicago, IL',
    'salary': '150,000'
  },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Chicago, IL',
    'salary': '175,000'
  },
    {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': '150,000'
  },
    {
    'id': 4,
    'title': 'Fronted Engineer',
    'location': 'Remote'
  }
]

@app.route("/")
def helloWorld():
  return render_template('home.html', jobs=JOBS, company_name="Tutorian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)