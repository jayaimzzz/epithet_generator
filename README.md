# Epithet Generator

This is a Flask API to serve random epithets from the [Shakespeare Insult Kit](http://www.pangloss.com/seidel/shake_rule.html).

## Running the API locally

* Git clone this repo to your PC and CD into the project dir

* Install the dependencies
    ```
    $pipenv install
    ```

* Start a PIPENV shell
    ```
    $ pipenv shell
    ```
* Run the tests
    ```
    $ pytest
    ```
* Run the API
    ```
    flask run
    ```

## Using the API's endpoints
    
    * GET '/'
    Returns one epithet

    * GET '/vocabulary'
    Returns the vocab used to generate the epithets

    * GET '/epithets/QTY
    Returns a defined quantity of epithets
    args:
        QTY (integer): quantity of epithets desired

    * GET '/randomquantity'
    Returns a random quantity of epithets
