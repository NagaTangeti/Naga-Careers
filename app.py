from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
  {
    "id":1,
    "title": "Data Analyst",
    "location": "Newcastle",
    "salary": "£28,000 per Annum"},

   { "id":2,
    "title": "Data Scientist ",
    "location": "Manchester",
    "salary": "£29,000 per Annum"
  },
  {
    "id":1,
    "title": "Data Analyst",
    "location": "Remote",
    }
  
]
@app.route("/")
def hello_world():
  
    return render_template("home.html", jobs=JOBS, company_name="Naga's")
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True )

