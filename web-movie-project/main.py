from turtle import update
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# DECLARACION DE VAR, KEYS & CONFIGS

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# The movie database

API_KEY = "d5958c5af12525faaf56e157ef3a55a9"
MOVIE_URL = "https://api.themoviedb.org/3/search/movie"

# -------------------------------------------------------------------------

# -- SqlAlchemy

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float(300), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(300), nullable=False)
    img_url = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

# Flask form

class EditForm(FlaskForm):
    rating = StringField('rating')
    review = StringField('review')
    submit = SubmitField('submit')

class AddForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submmit = SubmitField('sumbmit')
    
# FLASK

@app.route("/", methods=['GET'])
def home():
    
    movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    
    standar_ranking = 0
    current_rating = -1
    
    for i in range(len(movies)):
        
        print(movies[i])
        
        if movies[i].rating > current_rating:    
                        
            movies[i].ranking = 1
            print(movies[i].ranking)
            current_rating = movies[i].rating
            standar_ranking = movies[i].ranking
            
        else:
            movies[i].ranking = standar_ranking + 1
            current_rating = movies[i].rating
            standar_ranking = movies[i].ranking
        
        
    db.session.commit()
    
    return render_template("index.html", movies=movies)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    form = EditForm()
    
    form.validate_on_submit()
    
    if form.validate_on_submit():
        new_rating = form.rating.data
        new_review = form.review.data
        
        update = Movie.query.get(id)
        
        if new_rating != "":
            update.rating = new_rating
        if new_review != "":
            update.review = new_review
        
        db.session.commit()
        return redirect('/')
    
    return render_template('edit.html', form=form, id=id)

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    
    return redirect('/')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    
    form.validate_on_submit()
    
    title = form.movie_title.data
    
    if form.validate_on_submit():
        movie_parameters = {
        "api_key": API_KEY,
        "query" : title,
        }
        
        movie_api = requests.get(MOVIE_URL, params=movie_parameters)
        movie_data = movie_api.json()
    
        new_title = movie_data['results'][0]['original_title']
        new_description = movie_data['results'][0]['overview']        
        new_year = movie_data['results'][0]['release_date'][:4]
        new_rating = movie_data['results'][0]['vote_average']
        new_img_url = f"https://image.tmdb.org/t/p/w500{movie_data['results'][0]['poster_path']}"
        
        new_movie = Movie(title=new_title, description=new_description, year=new_year, rating=new_rating, img_url=new_img_url, review="", ranking=0)
        db.session.add(new_movie)
        db.session.commit()
        
        new_id = new_movie.id
        
        return redirect(f'/edit/{new_id}')
        
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    
