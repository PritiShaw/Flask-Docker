Flask Docker Example
---


[Pipenv](https://pypi.org/project/pipenv/) has been used for creating virtual environment.

## Installation Process

``` bash
# Activate venv
pipenv shell

# Install dependencies
# Skip if already installed for ingesting XML file
pipenv install

# Run REST API Server (http://localhost:5000)
python app.py
```

## API Endpoint

* GET     `/journal/<id>`  
`id` represents ID of the journal
        
* GET     `/journals`  
Parameters to be sent as URL query string  

**Parameters**

* *search*
	It searches the provided string (case insensitive) in the `title` attribute of the `Journals`. 
	For example `/journals?search=Bio`
        
##  GraphQL API

GraphiQL is visible in browser when a **GET** request is sent to endpoint `/graphql`  
Sending **POST** request to this endpoint will give response in JSON
Example GraphQL query
```
{
    allJournals {
        edges {
        node {
            id
            title
            ranl
        }
        }
    }
}
```
