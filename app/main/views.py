from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import  User,Blog,Comment
from .. import db,photos
from .forms import UpdateProfile,BlogForm,CommentForm
from flask_login import login_required,current_user
import datetime

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Blogging Website'

    # Getting reviews by category
    lifestyle_blog = Blog.get_blog('lifestyle')
    motivation_blog = Blog.get_blog('motivation')
    mentalhealth_blog = Blog.get_blog('mentalhealth')


    return render_template('profile/index.html',title = title, lifestle = lifestyle_blog, motivation = motivation_blog, mentalhealth = mentalhealth_blog)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    blogs_count = Blog.count_blogs(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches = blogs_count,date = user_joined)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.text.data
        category = blog_form.category.data

        # Updated pitch instance
        new_blog = Blog(blog_title=title,blog_content=blog,category=category,user=current_user,likes=0,dislikes=0)

        # Save pitch method
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title = 'New blog'
    return render_template('new_blog.html',title = title,blog_form=blog_form )

@main.route('/blogs/lifestyle_blogs')
def lifestyle_blogs():

    blogs = Blog.get_blog('lifestyle')

    return render_template("lifestyle_blogs.html", blogs = blogs)

@main.route('/blogs/motivation_blogs')
def motivation_blogs():

    blogs = Blog.get_blog('motivation')

    return render_template("motivation_blogs.html", blogs = blogs)

@main.route('/blogs/mentalhealth')
def mentalhealth():

    blogs = Blog.get_blog('mentalhealth')

    return render_template("mentalhealth.html", blogs = blogs)

@main.route('/blog/<int:id>', methods = ['GET','POST'])
def blog(id):
    blog = Blog.get_blog(id)
    posted_date = blog.posted.strftime('%b %d, %Y')

    if request.args.get("like"):
        blog.likes = blog.likes + 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    elif request.args.get("dislike"):
        blog.dislikes = blog.dislikes + 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment = comment,user = current_user,pitch_id = blog)

        new_comment.save_comment()


    comments = Comment.get_comments(blog)

    return render_template("blog.html", blog = blog, comment_form = comment_form, comments = comments, date = posted_date)

@main.route('/user/<uname>/blogs')
def user_blogs(uname):
    user = User.query.filter_by(username=uname).first()
    blogs = Blog.query.filter_by(user_id = user.id).all()
    blogs_count = Blog.count_blogs(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("profile/blogs.html", user=user,blogs=blogs,blogs_count=blogs_count,date = user_joined)
