from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as DT

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
  
##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")   

@app.route('/')
def get_all_posts():
    
    posts = BlogPost.query.all()


    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index): 
    requested_post = BlogPost.query.get(index)
    return render_template("post.html", post=requested_post)


@app.route("/edit-post/<int:index>", methods=["GET", "POST"])
def edit_post(index):
    
    post = BlogPost.query.get(index)
    
    edit_form = CreatePostForm(
    title=post.title,
    subtitle=post.subtitle,
    img_url=post.img_url,
    author=post.author,
    body=post.body
    )
    
    
    
    if edit_form.validate_on_submit():
        
        
        
        new_title = edit_form.title.data
        new_subtitle = edit_form.subtitle.data
        new_img_url = edit_form.img_url.data
        new_author = edit_form.author.data
        new_body = edit_form.body.data
        
        update = BlogPost.query.get(index)
        
        update.title = new_title
        update.subtitle = new_subtitle
        update.img_url = new_img_url
        update.author = new_author
        update.body = new_body
        
        db.session.commit()
        
        return redirect('/')
         
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/new-post/", methods=['GET', 'POST'])
def newPost():
   
    form = CreatePostForm()
    
    if form.validate_on_submit():
 
        title_data = request.form.get('title')
        subtitle_data = request.form.get('subtitle')
        author_data = request.form.get('author')
        img_url_data = request.form.get('img_url')
        body_data = request.form.get('body')
        date_data = DT.datetime.now().strftime("%B %d, %Y")

        new_post = BlogPost(
            title = title_data,
            subtitle = subtitle_data,
            author = author_data,
            img_url = img_url_data,
            body = body_data,
            date = date_data
        )

        db.session.add(new_post)
        db.session.commit()
        
        return redirect('/')
    
    return render_template("make-post.html", form=form)

@app.route("/delete/<int:index>", methods=["GET", "POST"])
def delete(index):
    
    post_to_eliminate = BlogPost.query.get(index)
    
    db.session.delete(post_to_eliminate)
    db.session.commit()
    
    return redirect('/')
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)