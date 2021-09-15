import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import create_app
from models import setup_db, Movies, Actors


class MovieApp(unittest.TestCase):
    """This class represents the Agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.json_database_path = 'postgres://timjcpwcrvoyjm:9c9893f05df1fe964295d8827cb83e01c772edf215457c6f65e2b9bf789e373c@ec2-3-219-111-26.compute-1.amazonaws.com:5432/dcosc463uh5uk3'

        setup_db(self.app, self.json_database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()

        self.new_actor = {'name': 'Turky alammar', 'age': 20,
                          'gender': 'male'}
        
        self.new_actor = {'name': 'sara', 'age': 20,
                          'gender': 'female'}
        
        self.new_actor = {'name': 'sale', 'age': 20,
                          'gender': 'male'}
        
        self.new_actor = {'name': 'khaled', 'age': 20,
                          'gender': 'male'}
        
        self.new_movie = {'title': 'movie1',
                          'release_date': '4/4/2021'}
        self.new_movie = {'title': 'movie2 ',
                          'release_date': '7/9/2021'}
        self.new_movie = {'title': 'movie 3',
                          'release_date': '2/7/2020'}

        
        for i in range(8):
            actor = Actors(name=self.new_actor['name'],
                          age=self.new_actor['age'],
                          gender=self.new_actor['gender'])
            actor.insert()
        for i in range(8):
            movie = Movies(title=self.new_movie['title'],
                          release_date=self.new_movie['release_date'])
            movie.insert()

        self.casting_assistant = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1ocTV0WEZoYTJtcXlpd2Z2dFBuZyJ9.eyJpc3MiOiJodHRwczovL2Rldi01cG55YnA4bS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYzdkMmU5NTE4MzkwMDcwODM3ZjA4IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjMxNjc4MjM2LCJleHAiOjE2MzE2ODU0MzYsImF6cCI6IkRGbTNobTVGamtzSmV1WVpvbnRKd0JFYUUzZXN0ODNUIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.gUe84_uhE_aWU5LfgFa8-lEP7nSA0miZIfdQDPEQeRmZ24LKYtDHuVjYe_pYA-w_AHNdmSnPQqII2UmHuX2RqIFOQ0hTkt_w2MeBGza9O5gwKmGeKcChl7qrz5UYFIxr87W01ELEY89z4BPO24O_TpXGYKAvjh3bhg_2sviutH7KtqHna2IoU7vLQz8o5ESNDuWahRbFBhimJ8QlJpXMt55zAMv9bhf9cZ21tTC0CBF50moLqn2x4No33VVMDz_M0Ng4dD8_HNADMO0YQCPIk9dVPMutBvyLZf6CkM6-TA7B82jD6LXPdvKlBbwCIH1rwkFyZM61nQ9wvXA4FT_2QQ"
        }
        self.casting_director = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1ocTV0WEZoYTJtcXlpd2Z2dFBuZyJ9.eyJpc3MiOiJodHRwczovL2Rldi01cG55YnA4bS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYzdkNDg1Y2FlNDYwMDY5MGIxNjljIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjMxNjc4MTczLCJleHAiOjE2MzE2ODUzNzMsImF6cCI6IkRGbTNobTVGamtzSmV1WVpvbnRKd0JFYUUzZXN0ODNUIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.iGQClxxcsGZlV-FsuizOrjb_hr8uLKHp62HOWJVAGqqAwO2k86ejpxA5XTK7xiP-A9fXEPffKoEjd87hmG8H8NBfS5XIs0k9ULUEa3frl7zeA-to6ElXfyDwMLKBihvSrXSFCoRYW3KDxEE1v-Xg2Ccw1qz0D--yvEuaiYIEWafp73z9SctpwbhvBJLaSVReltNwnvqV3oAnvdJ6vL0ekAf12_z910yk6-EMl0AlUQ6YxfcupVaKWX6cj75ybXOFQpEkdb47DRQ7EBc8RHJ3IVe5VC81CnlvatIc-KWUNk0ykg83Tg6jduyl80eWVXPi6R04OZRTuJc9XgGGBa3z0g"
        }
        self.executive_producer = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1ocTV0WEZoYTJtcXlpd2Z2dFBuZyJ9.eyJpc3MiOiJodHRwczovL2Rldi01cG55YnA4bS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYzdkNWU2MWJkMWUwMDY4MDJjZDFlIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjMxNjc4MDk5LCJleHAiOjE2MzE2ODUyOTksImF6cCI6IkRGbTNobTVGamtzSmV1WVpvbnRKd0JFYUUzZXN0ODNUIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.YqyKiJot1mUrSyKbANW32HZHNQS-2Nd55CD3E0nt2UsV-oW55WwSPUqMticN9reKQqCcUvdaF0godIfsiLSwkYyRpBVpEkfbKGp3GQq6798vwu-VgGYtORsUVXbeIbIbZsyDtWqPBtJc6q2UZqxDeu86d34juxpoMmFwWNXZfHCjvntS8wOLWMvhR5dCrYXgnse9Ma3T19P_Ql5NKz5iyYl5JWnLh3bJ3xTSIRkflIdnCQrTi_qVSqPhN-PG70oUmG2OsZakfwOQQfMFzAHbcyAdTCFmpS0ES9iMBpRfR_iLZSPbW2DX3m1gjiFfNmXv0qccxHxI1ldZBoa1bzWV4Q"
        }
    def tearDown(self):
        """Executed after reach test"""

        pass

    def test_get_all_movies(self):
        res = self.client().get('/movies', headers= self.casting_assistant)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['success'], True)
    

    def test_create_new_movie(self):
        res = self.client().post(
                                      '/movies',
                                      headers=self.executive_producer,
                                      json=self.new_movie)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['success'], True)
    

    def test_remove_movie(self):
        movie = Movies.query.all()[0]
        res = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=self.executive_producer)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['success'], True)


    def test_edit_movie(self):
        movie = Movies.query.all()[0]
        res = self.client().patch('/movies/{}'.format(movie.id),
                                       headers=self.executive_producer,
                                       json=self.new_movie)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['success'], True)


    def test_take_all_actors(self):
        res = self.client().get('/actors', headers= self.casting_assistant)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['success'], True)

    # the user have enough permissions
    def test_create_new_Actor(self):
        res = self.client().post('/actors',
                                      headers=self.executive_producer,
                                      json=self.new_actor)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['success'], True)
    

    def test_remove_actor(self):
        actor = Actors.query.all()[0]
        res = self.client().delete('/actors/{}'.format(actor.id),
                                        headers=self.executive_producer)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['success'], True)

    def test_edit_actor(self):
        actor = Actors.query.all()[0]
        res = self.client().patch('/actors/{}'.format(actor.id),
                                       headers=self.executive_producer,
                                       json=self.new_actor)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data['success'], True)


    def test_create_new_movie_erorr(self):
        res = self.client().post(
                                    '/movies',
                                    headers=self.casting_director,
                                    json=self.new_movie)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(json_data['success'], False)

    # the user does not have permissions   
    def test_remove_movie_erorr(self):
        movie = Movies.query.all()[0]
        res = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=self.casting_director)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(json_data['success'], False)


    def test_edit_movie_erorr(self):
        movie = Movies.query.all()[0]
        res = self.client().patch('/movies/{}'.format(movie.id),
                                       json=self.new_movie)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(json_data['success'], False)
    
    def test_create_actor_erorr(self):
        res = self.client().post('/actors', json=self.new_actor)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(json_data['success'], False)


    def test_remove_actor_erorr(self):
        actor = Actors.query.all()[0]
        res = self.client().delete('/actors/{}'.format(actor.id))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(json_data['success'], False)


    def test_edit_actor_erorr(self):
        actor = Actors.query.all()[0]
        res = self.client().patch('/actors/{}'.format(actor.id),
                                       json=self.new_actor)
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(json_data['success'], False)


if __name__ == "__main__":
    unittest.main()


