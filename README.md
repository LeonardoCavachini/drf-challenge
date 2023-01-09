# DRF-challenge

## Application Architecture

#### Django Apps

- contas (usuários)
- imovéis
- anúncios
- reservas

#### Other Root Folders

- settings: Django project settings

## Requirements

- [Python 3.9](https://www.python.org)
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

## Instructions to Run

#### Setup Codebase

- Clone this repo: `git clone https://github.com/LeonardoCavachini/drf-challenge.git`

This project needs docker to upload the database and application, in your terminal type `docker compose up `.
Ready now you can play with the application.
if you don't have the **Docker** installed, access [Docker](https://www.docker.com/) for more details.

#### Token

- On `http://localhost:8000/api/v1/register/` with email and password1 and password2 on the body, you can register in the application and receive a key as a token.

## Documentation

- On `http://localhost:8000/doc/`

## Endpoints imoveis

- Create Users (POST)

```
http://localhost:8000/api/v1/register/

body = { 
  "email": "user@user.com",
  "password1": "a1s2d3f5g",
  "password2": "a1s2d3f5g",
}
```

- Show imoveis (GET)

```
http://localhost:8000/api/v1/imoveis

```

- Create imoveis (POST)

```
http://localhost:8000/api/v1/imoveis

headers: {Authorization: Token your_token}

body = { 
  "limit_guests": 2,
  "bathroom_quantity": 3,
  "accept_animal": True,
  "housekeeping_price": 25.88,
  "activate_date":"2022-11-25"
}

```

- Get imóveis (GET)

```
http://localhost:8000/api/v1/imoveis/:property_code/
```

- Update imóveis (PATCH)

```

http://localhost:8000/api/v1/imoveis/:property_code/

body = { "limit_guests": 50 };

```

- Delete imóveis (DELETE)

```
http://localhost:8000/api/v1/imoveis/:property_code/
```

## Endpoints anúncios

- Show anúncios (GET)

```
http://localhost:8000/api/v1/anuncios

```

- Create anúncios (POST)

```
http://localhost:8000/api/v1/anuncios

headers: {Authorization: Token your_token}

body = { 
  "property_code": "f98afcbc-b9e5-4c69-bc88-2145a69ee85a",
  "platform_name": "zapimoveis",
  "platform_tax": 25.58,
}

```

- Get anúncios (GET)

```
http://localhost:8000/api/v1/anuncios/:id/

```

- Update anúncios (PATCH)

```

http://localhost:8000/api/v1/anuncios/:id/

body = { "platform_name": "OLX" };

```


## Endpoints reservas

- Show reservas (GET)

```
http://localhost:8000/api/v1/reservas

```

- Create reservas (POST)

```
http://localhost:8000/api/v1/reservas

headers: {Authorization: Token your_token}

body = { 
  "ads_code": 1,
  "guests": 8,
  "comments": "typing comments here",
  "total_price": 58.91,
  "check_in": "2022-11-15",
  "check_out": "2022-11-25"
}

```

- Get reservas (GET)

```

http://localhost:8000/api/v1/reservas/:reservation_code/


```

- Delete reservas (DELETE)

```

http://localhost:8000/api/v1/reservas/:reservation_code/


```
