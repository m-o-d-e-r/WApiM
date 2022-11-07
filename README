This API service will return random numbers based on the weather.

Follow `/docs` to get more info about api.

## Project structure
* WApiM/ - project folder

    * apps/ - contain applications folders (apps like Django)

        * random/ - application that allows to get a random number using a Python library or a number based on weather
            * app.py - contain APIRouter object
            * models.py - models definition
            * validators.py - contains data validators for checking the data entered by the user
            * views.py - main logic of api

        * weather/ - application allows to work with weather data (using OWM)
            * app.py
            * models.py
            * validators.py
            * views.py

    * utils/ - contains common things for apps (models and validators)
        * base_models.py - contains a description of the models
        * base_validators.py - contains definition of validators

    * main.py - entry point (it's similar to the main function in C++)