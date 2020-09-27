# Popular Quotes API

A simple RESTful API built with Flask. This api was built for practice sake.

The quotes provided by this api were originally sourced from a resource I can't remember. Either way, all credits to the provider.

## API url
https://pplrq.herokuapp.com/quotes/


## Making requests
### General
You can basically visit the base url to get a random quote, or optionally append an id number to get a quote matching the specified id.
Eg; https://pplrq.herokuapp.com/quotes/200.

### By author
To get quotes by a specific author, append the author's name to the url 
```
https://pplrq.herokuapp.com/quotes/<author>
```

**PS: author names are case-sensitive**

This https://pplrq.herokuapp.com/quotes/Buddha request for example would return
```
[
    {
        "id": 11,
        "author": "Buddha",
        "quote": "Peace comes from within. Do not seek it without."
    },
    {
        "id": 32,
        "author": "Buddha",
        "quote": "Work out your own salvation. Do not depend on others."
    },
    {
        "id": 48,
        "author": "Buddha",
        "quote": "He is able who thinks he is able."
    },
    ...
]
```

### List of Authors
https://pplrq.herokuapp.com/quotes/authors returns an array of all available authors

### All quotes
https://pplrq.herokuapp.com/quotes/all returns an array of all available quotes.
