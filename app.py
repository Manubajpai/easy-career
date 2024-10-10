from flask import Flask , render_template , jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Scientist',
        'location' : 'Bengaluru , India',
        'salary' : 'Rs 20,00,000'
    },
    {
        'id' : 2,
        'title' : 'Data Analyist',
        'location' : 'Bengaluru , India',
        'salary' : 'Rs 10,00,000'
    },
    {
        'id' : 3,
        'title' : 'Frontend Engineer',
        'location' : 'Delhi , India',
        'salary' : 'Rs 15,00,000'
    },
    {
        'id' : 4,
        'title' : 'Backend Engineer',
        'location' : 'Bengaluru , India',
        'salary' : 'Rs 18,00,000'
    },
    {
        'id' : 5,
        'title' : 'Data Scientist',
        'location' : 'New York, USA',
        'salary' : '$ 140,000'
    },
    {
        'id' : 6,
        'title' :' Data Scientist',
        'location' : 'San Fransico, USA',
        'salary' : '$ 120,000'
    }
]

@app.route("/")
def easy():
    return render_template("home.html" , 
                           jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)