from app import app, db
from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.forms import SignUpForm, PostForm, LoginForm
from app.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def index():
    posts = db.session.execute(db.select(Post).order_by(Post.date_created.desc())).scalars().all()
    return render_template('index.html', posts=posts)

@app.route('/photography')
def photography():
    image_list = [
        {"src": "https://picsum.photos/500/500?random=1", "alt": "Image 1"},
        {"src": "https://picsum.photos/500/500?random=2", "alt": "Image 2"},
        {"src": "https://picsum.photos/500/500?random=3", "alt": "Image 3"},
        {"src": "https://picsum.photos/500/500?random=4", "alt": "Image 4"},
        {"src": "https://picsum.photos/500/500?random=5", "alt": "Image 5"},
        {"src": "https://picsum.photos/500/500?random=6", "alt": "Image 6"}
    ]
    return render_template('photography.html', image_list = image_list)


@app.route('/music')
def music():
    image_list = [
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692060931/61TLq3DLxXL._UF1000_1000_QL80__s0hu3h.jpg", "alt": "Image 1"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692063419/ab67616d0000b27366eed0cb14c4a0523ff283bc_wteign.jpg", "alt": "Image 2"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692061071/51q8eDX-YbL_ckkssi.jpg", "alt": "Image 3"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692060905/Pentatonix__28album_29_daamw1.png", "alt": "Image 4"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692060983/715ljFIwX2L._UF1000_1000_QL80__rfunut.jpg", "alt": "Image 5"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692060956/7163tf7rbLL._UF1000_1000_QL80__hgiskv.jpg", "alt": "Image 6"}
    ]
    return render_template('music.html', image_list = image_list)

@app.route('/nature')
def nature():
    image_list = [
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500,g_auto/v1692064900/Hillier_Lake_Western_Australia_fvpy3b.jpg", "alt": "Hillier Lake, Western Australia"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692064632/Ha-Long-Bay-Vietnam_exaxgx.jpg", "alt": "Ha Long Bay, Vietnam"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692064632/Galapagos-Islands_zwdbly.jpg", "alt": "Galápagos Islands, Ecuador"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692064546/Giants-Causeway_z3seyf.jpg", "alt": "Giant's Causeway, Ireland"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/v1692064393/2b877476d2fb4bf1dda4a34c3638bb761451e223efeed5b41e8a232dfa1c7aa3-500_z5uvvf.jpg", "alt": "Wallowa Lake, Oregon"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692064388/hanauma-bay-nature-preserve_mhchcw.jpg", "alt": "Hanauma Bay, Hawaii"}
    ]
    return render_template('nature.html', image_list = image_list)

@app.route('/food')
def food():
    image_list = [
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692065479/200402101927-18-best-turkish-foods-lahmacun_owxcfb.jpg", "alt": "Lahmacun"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692065479/delish-230307-sopes-328-rv-lead-6418de26e5178_q40gi4.jpg", "alt": "Sopes"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692065479/35c1c89e-408c-4449-9abe-f109068f40c0_rpgoxu.jpg", "alt": "Cheeseburger & Fries"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692065479/Fried-eggs_du5vuf.jpg", "alt": "Fried Eggs"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692065480/PalmettoSeafoodCo_20web_nyq3if.jpg", "alt": "Palmetto Seafood"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692065794/Sushi-Hero-iStock-1286622470_qdijpk.jpg", "alt": "Sushi"}
    ]
    return render_template('food.html', image_list = image_list)

@app.route('/programming')
def programming():
    image_list = [
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692066220/87-code-reuse_hfmcoy.gif", "alt": "Dev Humor"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692066221/mwo_x1000_ipad_2_snap-pad_750x1000_f8f8f8.u6_i42s3q.jpg", "alt": "Dev Humor"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692066008/software-engineer-freaking-awesome-funny-gift-for-coworker-job-prank-gag-idea-funny-gift-ideas_xws9ys.jpg", "alt": "Dev Humor"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692066221/software-engineer-i-cant-fix-stupid-funny-coworker-gift-funny-gift-ideas_iazfhm.jpg", "alt": "Dev Humor"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692066221/computers-computer_algorithm-algorithms-business_problems-programming-problem_solving-aban569_low_ixxtob.jpg", "alt": "Dev Humor"},
        {"src": "https://res.cloudinary.com/djvpgim4w/image/upload/c_thumb,w_500,h_500/v1692066221/6JJxGdV5Mcw7F88rLU582psGFKzf2j-right_zjngmr.png", "alt": "Dev Humor"}
    ]
    return render_template('programming.html', image_list = image_list)


@app.route('/signup', methods = ["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Get the data from the form
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        check_user = db.session.execute(db.select(User).where( (User.username==username) | (User.email==email) )).scalar()
        if check_user:
            flash('A user with that username/password already exists', 'error')
            return redirect(url_for('signup'))

        new_user = User(first_name = first_name, last_name = last_name, username = username, email = email, password = password)

        db.session.add(new_user)
        db.session.commit()
        flash(f'{new_user.username} has been created', 'success')

        login_user(new_user)      

                # redirect back to the home page
        return redirect(url_for('index'))
    elif form.is_submitted():
        flash("Your passwords do not match", 'error')
        return redirect(url_for('signup'))
                        
    return render_template('signup.html', form = form)

@app.route('/create', methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        # Get the data from the form
        title = form.title.data
        body = form.body.data
        image_url = form.image_url.data or None
        
        new_post = Post(title=title, body=body, image_url=image_url, user_id=current_user.id)

        db.session.add(new_post)
        db.session.commit()

        flash(f"{new_post.title} has been created", 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have successfully logged out", 'success')
    return redirect(url_for('index'))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = db.session.execute(db.select(User).where(User.username==username)).scalar()
        if user is not None and user.check_password(password):
            login_user(user)
            flash("You have successfully logged in", 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username and/or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html', form = form)
