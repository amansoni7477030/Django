# Django
The API endpoints provided are used to access and manipulate data stored in the backend database.

/api/works - This endpoint returns a list of all the works stored in the database.

/api/works?artist=[Artist Name] - This endpoint allows you to search for works by the artist's name. The [Artist Name] should be replaced with the actual name of the artist.

/api/works?work_type=Youtube or pk of YouTube - This endpoint allows you to filter the list of works based on the work type. The Youtube value should be replaced with either Youtube, Instagram, or Other depending on the desired work type. The pk of YouTube should be replaced with the primary key of the desired work type.

/api/register - This endpoint is used to register new users. The request should include a body with the following parameters: username and password. An example request body would be {username: "testuser", password: 123123}.
