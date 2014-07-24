from flask import render_template
from app import app, pages

@app.route('/')
def home():
    return render_template('index.html', page=page)
    
@app.route('/<path:path>/')
def page(path):
    # path is the filename of the page without extension
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
    
@app.route('/projects/')
def projects():
    return render_template('projects.html', page=page)
    
@app.route('/travels/')
def travels():
    return render_template('travels.html', page=page)
    
@app.route('/blog/')
def blog():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('blog.html', pages=sorted_posts)