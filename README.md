Flask-Docker API
---

### Docker Instruction

**To Build** `docker build -t flask-docker .`  
**To Run** `docker run --name flask-docker-priti -d -e TARGET_YEAR=<YEAR> -p 8000:8000 flask-docker`  
**To Delete running container** `docker rm -f flask-docker-priti`  

`YEAR` can be in range `[1999,2018]`

## API Instruction
**Base URL** `http://localhost:8000/`  
## API Endpoint

* GET     `/journal/<id>`  
`id` represents ID of the `Journal`
        
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
            rank
        }
        }
    }
}
```

