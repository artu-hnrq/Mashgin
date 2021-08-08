# Comunication layer
The data transfer between the front end application and backend services
is made through an [REST][>1] API. 

[>1]: https://en.wikipedia.org/wiki/Representational_state_transfer "Representational state transfer"
[>2]: https://app.getpostman.com/join-team?invite_code=bf91c969246261a2b3d423cb0390d112&ws=50e0f2a1-eb23-467c-bcd7-78f231f9d783 "Postman workspace"


## Endpoints
The developed API exposes endpoints, under `/` path, in line with the following specification:

### menu/
Request the list of dishes offered by the restaurant

| Allowed HTTP methods | Required inputs | Optional inputs | Authentication required | Permission required |
| --- | --- | --- | --- | --- |
| `GET` | - | - | - | - |


## API clients
There are several ways to interact with the API.
**Django REST Framework** itself will render a GUI if you access some endpoint via browser.
There you'll be able to check more information over that endpoint and even trigger requests.

You also can use [Postman][>2] HTTP client to do so.
Inside [repository][-2]'s `data` folder you'll find its workspace-configuration directory, 
which can be imported to set up the context used during development.

Or you can also ingress into [project's Postman configured workspace][>3].
