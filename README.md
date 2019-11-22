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

## Using 

1. Choose or create application.
2. Go to application and copy a token.
3. Go to API Endpoint and send errors to the application through the token.

## Using crashlytics SDK

To use crashlytics SDK, you need to transfer the URL and application token to the settings SDK:
`crashlytics/configSDK.py`
after that add the decorator @error_handler to the necessary function.

#### For example to test crashlytics SDK:
now in logging_error/api/view.py for example, the working code is commented out - the token is not checked for correctness. 
Try to send an error by an incorrect token - an error will be caught by the decorator @error_handler and transferred to the application.

```
crashlytics/configSDK.py:
    url = 'http://127.0.0.1:8000/api/crash/'
    token = '<token>'
```
in API:

```
url = 'http://127.0.0.1:8000/api/crash/123456654321nettakogotokena/'
```
POST:

```
{
    "type": "TestError",
    "date": "2019-10-31T10:10:10Z",
    "message": "TestMessage",
    "stacktrace": "TestStacktrace"
}
```
After that, error DoesNotExist will appear in your application with a token.

