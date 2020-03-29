# Movies Register Service

## Usage

All responses will have this from

```json
{
	"data": "The content of the response",
	"message": "Description of the response"
}

```

### List all movies

**Definitions**

`GET /movies`

- `200 OK` on success

```json
[
    {
        "identifier": "godfather",
        "name": "The Godfather",
        "movie_type": "Crime",
        "movie_year": 1972
    },
    {
        "identifier": "lord-of-the-rings",
        "name": "The Lord of the Rings",
        "movie_type": "Fantasy",
        "movie_year": 2002
    }
]
```

### Registering a new movie

**Definition**

` POST /movies`

**Arguments**

- `"identifier":string` a globally unique identifier for this movie
- `"name":string` a friendly name for this movie
- `"movie_type":string` the type of the movie
- `"movie_year":integer` the year of the movie

If a movie with the given identifier already exists, the existing movie will be overwritten.

- `201 Created` on success

```json
    {
        "identifier": "godfather",
        "name": "The Godfather",
        "movie_type": "Crime",
        "movie_year": 1972
    }
```
## Lookup movie details

`GET /movies/<identifier>`

**Responses**

- `200 OK` on success
- `404 Not Found` if the movie does not exist

```json
    {
        "identifier": "godfather",
        "name": "The Godfather",
        "movie_type": "Crime",
        "movie_year": 1972
    }
```

## Update movie details

`PUT /movies/<identifier>`

You can update a single or multiple fields

**Responses**

- `200 OK` on success
- `404 Not Found` if the movie does not exist

```json
    {
        "name": "The Godfather",
        "movie_type": "Crime",
        "movie_year": 1972
    }
```

## Delete a movie

**Definition**

`DELETE /movies/<identifier>`

**Responses**

- `200 OK` on success
- `404 Not Found` if the movie does not exist
