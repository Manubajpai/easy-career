from flask import Flask , render_template , jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql

# use pymysql instead of mysqldb
pymysql.install_as_MySQLdb()


app = Flask(__name__)


# config for mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:manubajpai%40123@34.132.12.183:3306/easy-career'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

# initialise the database
db = SQLAlchemy(app)

# defining the job model
class Jobs(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(200) , nullable = False)
    location = db.Column(db.String(200) , nullable = False)
    salary = db.Column(db.Integer)
    currency = db.Column(db.String(10))
    responsibilities = db.Column(db.String(2000))
    requirements = db.Column(db.String(2000))

# route to render jobs on home
@app.route("/")
def easy():
    jobs = Jobs.query.all() # fetch all jobs from database
    return render_template("home.html" , jobs = jobs)

# api route to return jobs in json format
@app.route("/api/jobs")
def list_jobs():
    jobs = Jobs.query.all()
    jobs_list = [
        {
            'id':job.id,
            'title':job.title,
            'location':job.location,
            'salary':job.salary,
            'currency':job.currency,
            'responsibilities':job.responsibilities,
            'requirements':job.requirements
        } for job in jobs
    ]
    return jsonify(jobs_list)

if __name__ == "__main__":
    app.run(debug=True)