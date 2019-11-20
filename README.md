# Sentry Logging Error

## Getting started

1. Download a copy from GitHub:

    ```
    $ git clone https://github.com/igornikanovich/logging-errors.git
    ```

2. Setup Django requirements:

    ```
    $ pipenv install
    $ pipenv shell
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    ```

3. Run the tests:

    ```
    $ python3 manage.py test
    ```

4. Run the server locally:

    ```
    $ python3 manage.py runserver
    ```


## API Endpoints

- *POST* `/api/crash/<token>/` - Create new error.
