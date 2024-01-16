from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":
        
        email = request.form.get('email')
         
        
        user = User.query.filter_by(email=email).first()

        
        if not user:
        
            password = request.form.get('password')
            hashed_salted_psw = generate_password_hash(password=password, 
                                                   method='pbkdf2:sha256', 
                                                   salt_length=8)
            new_user = User(
            name=request.form.get('name'),
            email=request.form.get('email'),
            password=hashed_salted_psw
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)

            user_name = request.form.get('name')

            return redirect(url_for("secrets", name=user_name))
        
        else:
            flash('You have already registered with that email, please try login')
            return redirect(url_for("login"))
    
    return render_template("register.html")


@app.route('/login',  methods=['GET', 'POST'])
def login():
    
    if request.method == "POST":
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        
        if user:
            if check_password_hash(user.password, password):
                
                login_user(user)
                
                return redirect(url_for("secrets"))
            
            else:
                flash('The password does not match the email, please try again')
            return redirect(url_for("login"))
                
        else:
            flash('This email does not exist, please try again')
            return redirect(url_for("login"))
    
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    name = request.args.get("name")
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    
    logout_user()
    
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory(directory="static/files/", path="cheat_sheet.pdf") # directory debe mostrar el camino relativo hacia el archivo sin mencionar al archivo
                                                                                  # path es la ubicacion del archivo ahora si mencionando el archivo, puede o no tener mas carpetas arriba. 


if __name__ == "__main__":
    app.run(debug=True)
