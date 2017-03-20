from flask import Blueprint, render_template, request, redirect, session, g
from database import db_session
from user import User
from build import Build
from functools import wraps

builder_blueprint = Blueprint("builder", __name__, template_folder="templates")



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


@builder_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    if session["user_id"] is not None:
        if request.method == 'POST':
            user = find_user(session.get('user_id'))
            build = Build('untitled build', 'voxel(0, 0, 0)', user.id)
            db_session.add(build)
            db_session.commit()
            return redirect('/builder/' +  str(build.id))

        user = find_user(session.get('user_id'))
        builds = find_user_builds(user.id)
        print('panda')
        print(builds)
        print('panda')
        return render_template('profile.html', builds=builds)
    else:
        print("pandas")
        print("pandas")
        redirect('/')


@builder_blueprint.route('/builder/<build_id>', methods=['GET', 'PUT'])
def builder(build_id):
    if session["user_id"] is not None:
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
    else:
        redirect('/')


def find_results(query):
    builds = db_session.query(Build).filter_by(title=query).first()
    return builds


def find_builds():
    builds = db_session.query(Build).all()


@builder_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    if session["user_id"] is not None:
        results = find_builds()
        if request.method == 'POST':
            results = find_results(request.form['query'])
        return render_template('results.html', results=results)
    else:
        redirect('/')


@builder_blueprint.route('/build/<build_id>')
def build(build_id):
    if session["user_id"] is not None:
        build = find_build(build_id)
        user = find_user_id(build.user)
        return render_template('build.html', build=build, user=user)
    else:
        redirect('/')
