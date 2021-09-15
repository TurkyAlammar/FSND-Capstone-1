# Udacity MovieApp Project
This venture models an organization that is answerable for making films and overseeing and relegating entertainers to those motion pictures. The framework improve and smooth out the course of Executive Producer inside the organization. It was done as capstone project for full stack nanodgree. this task test backend information outsider administrations intgration.

#Tokens 
CASTING_ASSISTANT='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1ocTV0WEZoYTJtcXlpd2Z2dFBuZyJ9.eyJpc3MiOiJodHRwczovL2Rldi01cG55YnA4bS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYzdkMmU5NTE4MzkwMDcwODM3ZjA4IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjMxNjE3ODAwLCJleHAiOjE2MzE2MjUwMDAsImF6cCI6IkRGbTNobTVGamtzSmV1WVpvbnRKd0JFYUUzZXN0ODNUIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.WXTWoB_Mooxn6aU2TSY_ALsF_9qzhgttyvdK8vJEZEjY3V3Qd9j49_V5P0BW6uC1x0bYhdBEBsILl388SRDeiS85YEANSIlckHrKkKnmSjaIV8UFvFTB4rnvxv3lz9HvPKwjaPJnH1uexiWaZvg252py-4Ga_cUL1Ggql1mXpdkwQ7CoqM0Y5EMsxq0ky0Y-mYoqKOYJpKB9ruehL7TfpT1ah55JDa7v6UkTIlkl6tpTwPYEED3-MisfUMh7zWNLQNT0Pm2vhZfKZOkwaFSLaqDOlqbkccNfbYHBT56BmS0ZhOct0_kIQWr7Mj5UW_y5WN31Vqb52YCZ4xKuuc5W-g'

CASTING_DIRECTOR='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1ocTV0WEZoYTJtcXlpd2Z2dFBuZyJ9.eyJpc3MiOiJodHRwczovL2Rldi01cG55YnA4bS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYzdkNDg1Y2FlNDYwMDY5MGIxNjljIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjMxNjE3ODU3LCJleHAiOjE2MzE2MjUwNTcsImF6cCI6IkRGbTNobTVGamtzSmV1WVpvbnRKd0JFYUUzZXN0ODNUIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.WJeDRkpMErw4QZFWa0dsLWCiISEc_hbCKl8lxcghx-0BtGkGWB0hbfwdOdyRJg-SBb7K_wDKyJXBS-7up-imJq4d-jxRDvO0MjNLUh1o1ZP0BTQ0k6Hiq7nD7A5f-K_w4quIqtIimyzgOnF2h5TG7_ShhFDs-ZEO0OyEazO666tKW1JV7LG7gVcZtHY_QL8plEUPiSyt8z4EDi4OI3g7aSqhSzCQut07AsIa3QrsjaFvOvEWrh_kR1B_vO-S9kvS_7hROJlYmKbefmK5bK_C1T0lM_ma5zZcZTaE2pnpXE2Zkhv2lFG_qjF_fWAxJfPgTT54l3sg48C4EQQbZ6_N4w'

EXECUTIVE_PRODUCER=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1ocTV0WEZoYTJtcXlpd2Z2dFBuZyJ9.eyJpc3MiOiJodHRwczovL2Rldi01cG55YnA4bS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYzdkNWU2MWJkMWUwMDY4MDJjZDFlIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjMxNjc4MDk5LCJleHAiOjE2MzE2ODUyOTksImF6cCI6IkRGbTNobTVGamtzSmV1WVpvbnRKd0JFYUUzZXN0ODNUIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.YqyKiJot1mUrSyKbANW32HZHNQS-2Nd55CD3E0nt2UsV-oW55WwSPUqMticN9reKQqCcUvdaF0godIfsiLSwkYyRpBVpEkfbKGp3GQq6798vwu-VgGYtORsUVXbeIbIbZsyDtWqPBtJc6q2UZqxDeu86d34juxpoMmFwWNXZfHCjvntS8wOLWMvhR5dCrYXgnse9Ma3T19P_Ql5NKz5iyYl5JWnLh3bJ3xTSIRkflIdnCQrTi_qVSqPhN-PG70oUmG2OsZakfwOQQfMFzAHbcyAdTCFmpS0ES9iMBpRfR_iLZSPbW2DX3m1gjiFfNmXv0qccxHxI1ldZBoa1bzWV4Q'


## let' started!

### Installing Dependencies

To begin the task locally, you need to have the accompanying apparatuses:
1. Python3 and PIP (Back-end)

#### Python 3.7

Adhere to guidelines to introduce the most recent variant of python for your foundation in the python docs (https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Enviornment

We suggest working inside a virtual climate at whatever point utilizing Python for projects. This saves your conditions for each venture independent and organaized. Directions for setting up a virual enviornment for your foundation can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP installations

When you have your virtual climate arrangement and running, introduce conditions by exploring to the base of the index and run:

```bash
pip install -r requirements.txt
```

This will introduce the entirety of the necessary bundles we chose inside the 'requirements.txt' record.

## Running the server locally in development environment

From within the `root` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
pip install -r requirements.txt
source setup.sh
python app.py
```

the `source setup.sh` will prepare all the needed environment variables to run the server.


## API Reference

### Introduction
The API builded to make clients eable to perform CRUD procedure on TurkyMovies information base without any problem. It have been builded utilizing Flask miniature structure, which is Python system. 

This API was builded for the requirments of graduating of the FSND nanodegree of Udactiy. 

Every one of the reactions of the API is in JSON design.

### Getting Started

#### Base URL

This project is deployed and available on Heroku:
```
https://tralapp.herokuapp.com
```

### Endpoints Library

This section will contain all the endpoints with their response examples to make everything clear for the users of our API

#### GET /actors

- Return: return list of all the available actors.

- Sample Response:
    ```
    {
  "actors": [
    {
      "age": "20",
      "gender": "male",
      "id": 3,
      "name": "khaled"
    },
    ```
#### GET /movies

- Return: return list of all the available movies.

- Sample Request: ```curl https://tralapp.herokuapp.com/movies```

    ```
    {
  "movies": [
    {
      "id": 1,
      "release date": "Fri, 07 Feb 2020 00:00:00 GMT",
      "title": "movie 3"
    },
    ```

#### DELETE /actors/id

- Return: 
    - the deleted actor ID and result of success state.

- Sample Request: ```curl -X "DELETE" https://tralapp.herokuapp.com/actors/4```

- Arguments: 
    - it take the id of the actor in the URL after the ```actors/```

- Sample Response:
    ```
    {
        "success": True,
        "actor_id": 4
    }
    ```

#### DELETE /movies/id

- Return: 
    - the deleted movie ID and result of success state.

- Sample Request: ```curl -X "DELETE" https://tralapp.herokuapp.com/movies/5```

- Arguments: 
    - it take the id of the movie in the URL after the ```movies/```

- Sample Response:
    ```
    {
        "success": True,
        "movie_id": 5
    }
    ```

#### POST /actors

- Return: 
    - the request success state.
    - the created actor object.
    - the ID of the created actor.

- Sample Request: 
    ```curl -d '{"name": "Fahad", "age": 23, "gender": "Male"}' -H "Content-Type: application/json" -H "Authorization: Bearer <put the token here!>" -X "POST" https://tralapp.herokuapp.com/actors```

no argument

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 15,
            "name": "Fahad",
            "gender": "Male",
            "age": 23
        },
        "actor_id": 15
    }
    ```

#### POST /movies

- Return: 
    - the request success state.
    - the created movie object.
    - the ID of the created movie.

- Sample Request: 
    ```curl -d '{"title": "JungleBirds"}' -H "Content-Type: application/json" -H "Authorization: Bearer <putTheTokenHere>" -X "POST" https://tralapp.herokuapp.com/movies```

- Arguments: 
    - None

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 23,
            "title": "JungleBirds",
            "release": "2 Sep, 2021"
        },
        "movie_id": 23
    }
    ```

#### PATCH /actors

- Return:
    - the request success state.
    - the modified actor object.
    - the ID of the modified actor.

- Sample Request: 
    ```curl -d '{"name": "Fahad", "age": 23, "gender": "male"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://tralapp.herokuapp.com/actors/15```

- Arguments: 
    - the ID of the actor that need to modified.

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 15,
            "name": "Fahad",
            "gender": "male",
            "age": 23
        },
        "actor_id": 15
    }
    ```

#### PATCH /movies

- Return:
    - the request success state.
    - the modified movie object.
    - the ID of the modified movie.

- Sample Request: 
    ```curl -d '{"title": "JungleBirds"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://tralapp.herokuapp.com/movies/87```

- Arguments: 
    - the ID of the movie that need to modified.

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 23,
            "title": "lockdown",
            "release": "7 Oct, 2020"
        },
        "movie_id": 23
    }
    ```

## Authentication and Permissions

Authentication is handled via [Auth0](https://auth0.com).

All endpoints require authentication, and proper permission. 

For testing, you can use the Tokens that available in the .env file.

API endpoints use these roles and permissions:

- Casting Assistant:
    * 'get:actors' (remove actor from the casting agency database).
    * 'get:movies' (edit or modify actor data that exist in the casting agency database).

- Casting Director:
    * Same as the Casting Assistant permissions, plus
    * 'delete:actors' (remove actor from the casting agency database).
    * 'patch:actors' (edit or modify actor data that exist in the casting agency database).
    * 'patch:movies' (edit or modify actor data that exist in the casting agency database).
    * 'post:actorss' (create new actors in the casting agency database).

- Executive Director:
    * Same as the Casting Director permissions, plus
    * 'delete:movies' (remove movie from the casting agency database).
    * 'post:moviess' (create new movies in the casting agency database).