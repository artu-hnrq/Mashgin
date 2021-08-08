# Configuration
Project execution can be configured through environment variables. 
Below each expected variable is described.

[1]: management.md

[>1]: https://docs.djangoproject.com/en/3.1/topics/settings/


## General
#### ENVIRONMENT
It defines instance's *running mode*, impacting in default value supplied for other configurations,
as well as in expected environment variables. See more details in each configuration description.

| type | default |
| --- | --- |
| `string` | `'DEVELOPMENT'` |

-----

## Database
When **ENVIRONMENT** is set to `'PRODUCTION'`, application expects the following configurations. 
Otherwise, it uses a not-configurable `sqlite3` database.

#### DB_ENGINE
Defines Django's database `ENGINE` setting

| type | default |
| --- | --- |
| `string` | `'django.db.backends.postgresql_psycopg2'` |

-----

#### DB_NAME
Defines Django's database `NAME` setting

| type | default |
| --- | --- |
| `string` | required |

-----

#### DB_USERNAME
Defines Django's database `USER` setting

| type | default |
| --- | --- |
| `string` | required |

-----

#### DB_PASSWORD
Defines Django's database `PASSWORD` setting

| type | default |
| --- | --- |
| `string` | required |

-----

### DB_HOST
Defines Django's database `HOST` setting

| type | default |
| --- | --- |
| `string` | required |

-----

#### DB_PORT
Defines Django's database `PORT` setting

| type | default |
| --- | --- |
| `string` | required |

-----


## Django settings
Beside some, most of the following configuration variables are direct forwarded to same-name Django settings.
And their effect over launched service can be found in [proper documentation][>1].

#### ALLOWED_HOSTS

| type | default |
| --- | --- |
| space-separated list | `'*'` |

-----

#### DEBUG

| type | default |
| --- | --- |
| `bool` | `ENVIRONMENT != 'PRODUCTION'` |

-----

#### LOADDATA
Define fixture files to be loaded after application boots up

| type | default |
| --- | --- |
| space-separated list | `''` |

-----

#### MEDIA_ROOT

| type | default |
| --- | --- |
| path | `'media'` |

-----

#### SECRET_KEY

| type | default |
| --- | --- |
| `string` | Dynamically generated through `django.core.management.utils.get_random_secret_key` function |

-----


## Development management
Environment variables are also used by Make in order to provide flexibility
to its provisioned [development management][1] facilities.
Some of them are described above.

#### PROJECT_NAME
Used to compose `make` outputs

| type | default |
| --- | --- |
| `string` | Dynamically retrieved by project root directory name |

-----

#### PYTHON
Define where to find the `python3` binary to be used in Make targets.
If supplied value not refer to the full path of an executable script,
a python virtual environment will be created inside the current working directory.

| type | default |
| --- | --- |
| path | `$(VENV_ROOT)/bin/python3` |

-----

#### VENV
Define if python virtual environment should be used and its folder name

| type | default |
| --- | --- |
| string | `'venv'` |
