from flask import Blueprint, render_template, request, redirect, session
from database import db_session
from user import User
from build import Build

builder_blueprint = Blueprint("builder", __name__, template_folder="templates")

@builder.before_request
def before_request():
    if session.get('user_id') is not None:
        return redirect('/')


def find_user(username):
    user = db_session.query(User).filter_by(username=username).first()
    return user

def find_user_id(id=id):
    user = db_session.query(User).filter_by(id=id).first()
    return user


def find_build(id):
    build = db_session.query(Build).filter_by(id=id).first()
    return build


def find_user_builds(user_id):
    builds = db_session.query(Build).filter_by(user=user_id).all()
    return builds


@before_request
@builder_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        user = find_user(session.get('user_id'))
        build = Build('untitled build', 'voxel(0, 0, 0)', user.id)
        db_session.add(build)
        db_session.commit()
        return redirect('/builder/' +  str(build.id))

    user = find_user(session.get('user_id'))
    builds = find_user_builds(user.id)
    return render_template('profile.html', builds=builds)


@builder_blueprint.route('/builder/<build_id>', methods=['GET', 'PUT'])
def builder(build_id):
    build = find_build(build_id)
    user = find_user(session.get('user_id'))

    if request.method == 'PUT':
        build.title = request.form['title']
        build.code = request.form['code']
        db_session.commit()

    if build.user == user.id:
        return render_template('builder.html', build=build)
    else:
        return redirect('/')


@builder_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    pass
#needs implemeting



@builder_blueprint.route('/build/<build_id>')
def build(build_id):
    build = find_build(build_id)
    user = find_user_id(build.user)
    print(build.user)
    return render_template('build.html', build=build, user=user)
