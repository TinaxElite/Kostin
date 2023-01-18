from flask import Flask, render_template
from models import db, Categories, ContactsInfo, Posts
from datetime import datetime


app = Flask(__name__)

# Конфиг приложения загружаем из другого файла
app.config.from_pyfile('config.py')


# Инициализируем БД
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    posts = db.session.query(Posts).filter(Posts.id_category==1).all()
    posts_interest = db.session.query(Posts).filter(Posts.id_category==2).all()
    
    return render_template('index.html', posts=posts, posts_interest=posts_interest)


@app.route('/post/<int:post_id>', methods=['POST', 'GET'])
def post(post_id):
    
    last_posts = db.session.query(Posts).filter(Posts.id_category==1).limit(5).all()
    posts = db.session.query(Posts).filter(Posts.id_category==1).all()
    post = db.session.query(Posts).filter(Posts.id==post_id).first()
    
    return render_template('post.html', post=post, posts=posts, last_posts=last_posts)


@app.route('/news')
def news():
    posts = db.session.query(Posts).filter(Posts.id_category==1).all()
    posts_cat = db.session.query(Posts).filter(Posts.id_category==1).all()
    
    return render_template('category.html', cat="РУБРИКА: НОВОСТИ ДНЯ", posts=posts, posts_cat=posts_cat)



@app.route('/interesting')
def interesting():
    posts = db.session.query(Posts).filter(Posts.id_category==1).all()
    posts_cat = db.session.query(Posts).filter(Posts.id_category==2).all()
    
    return render_template('category.html', cat="РУБРИКА: ИНТЕРЕСНОЕ", posts=posts, posts_cat=posts_cat)


@app.route('/organisation')
def organisation():
    posts = db.session.query(Posts).filter(Posts.id_category==1).all()
    
    return render_template('organisation.html', posts=posts)


@app.route('/contacts')
def contacts():
    posts = db.session.query(Posts).filter(Posts.id_category==1).all()
    
    return render_template('contacts.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
