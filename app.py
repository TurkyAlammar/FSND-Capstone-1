import os
import sys
from flask import Flask, json, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actors, Movies
from auth import AuthError, requires_auth
from datetime import datetime


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def HelloPage():
        
        return "Welcome to Turky Website !!!"

    def lengthCheaker(value):
        if len(value) == 0:
            abort(404)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def view_movies(jwtToken):
        get_movie_with_id = Movies.query.order_by(Movies.id).all()
        lengthCheaker(get_movie_with_id)
        query2 = [movie.format() for movie in get_movie_with_id]

        json = jsonify({
            "success": True,
            "movies": query2
        }), 200

        return json

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movies(jwtToken):
        try:
            get_json_data = request.get_json()
            rel = datetime.utcnow()
            return HelpingMethod1(get_json_data,rel)

        except Exception:
            print(sys.exc_info())
            abort(500)


    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movies(jwtToken, movie_id):
        get_Json_data = request.get_json()
        get_all_movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        print(get_all_movie)
        if get_all_movie is None:
            abort(404)

        helpingMethod2(get_all_movie,get_Json_data)


    def HelpingMethod4(get_actor_data,query_actors):
        new_name = get_actor_data.get('name', None)
        new_age = get_actor_data.get('age', None)
        new_gender = get_actor_data.get('gender', None)

        if new_name is not None:
            query_actors.name = new_name
        else:
            query_actors.name = query_actors.name

        if new_age is not None:
            query_actors.age = new_age
        else:
            query_actors.age = query_actors.age

        if new_gender is not None:
            query_actors.gender = new_gender
        else:
            query_actors.gender = query_actors.gender

        try:
            query_actors.update()
        except Exception:
            abort(422)
        json = jsonify({
                "success": True,
                "Actor": query_actors.format()
            }), 200
        return json


    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(jwtToken, movie_id):
        try:
            get_all_movie = Movies.query.filter(
                                    Movies.id == movie_id).one_or_none()
            if get_all_movie is None:
                abort(404)

            get_all_movie.delete()
            return jsonify({
                'success': True,
                'deleted': movie_id}), 200

        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def view_actors(jwtToken):
        get_all_actors = Actors.query.all()
        lengthCheaker(get_all_actors)
        json = jsonify({'success': True, 'actors': [actor.format()
                        for actor in get_all_actors]}), 200
        return json

    
    def HelpingMethod1(jsonFile, rel):
        if 'title' not in jsonFile:
            abort(400)

        if 'release_date' in jsonFile:
            release = jsonFile['release_date']

            InserMovie = Movies(title=jsonFile['title'], release_date=rel)
            InserMovie.insert()
            json = jsonify({'success': True, 'movie': InserMovie.format(),
                        'movie_id': InserMovie.id})
            return json


    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actors(jwtToken):
        try:
            return HelpingMethod3()

        except Exception:
            print(sys.exc_info())
            abort(500)
    

    def helpingMethod2(get_all_movie,get_Json_data):
        new_title = get_Json_data.get('title', None)
        new_release_date = get_Json_data.get('release_date', None)

        if new_title is not None:
            get_all_movie.title = new_title
        else:
            get_all_movie.title = get_all_movie.title

        if new_release_date is not None:
            get_all_movie.release_date = new_release_date
        else:
            get_all_movie.release_date = get_all_movie.release_date

        try:
            get_all_movie.update()
        except Exception:
            abort(422)

        json = jsonify({
                "success": True,
                "Movie": get_all_movie.format()
            }), 200

        return json

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actors(jwtToken, actor_id):
        get_actor_data = request.get_json()
        query_actors = Actors.query.filter(Actors.id == actor_id).one_or_none()
        print(query_actors)
        if query_actors is None:
            abort(404)


        return HelpingMethod4(get_actor_data, query_actors)


    def HelpingMethod5(actor_id):
            actor = Actors.query.filter(
                                    Actors.id == actor_id).one_or_none()
            if actor is None:
                abort(404)

            actor.delete()
            return jsonify({
                'success': True,
                'deleted': actor_id}), 200

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwtToken, actor_id):
        try:
            json = HelpingMethod5(actor_id)

        except Exception:
            print(sys.exc_info())
            abort(422)


    def HelpingMethod3():
        get_all_req = request.get_json()
        if get_all_req is None:
            abort(422)
        create_actor = Actors(
            get_all_req['name'],
            get_all_req['age'],
            get_all_req['gender']
            )
        create_actor.insert()
        json = jsonify({'success': True}), 200
        return json

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(400)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'unauthorized'
        }), 401


    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500


    @app.errorhandler(AuthError)
    def auth_errors(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
