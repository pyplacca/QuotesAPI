# Popular Quotes API

A simple a RESTful API built with Flask. This api was built for learning sake.

The quotes provided by this api were originally sourced from a resource I can't remember. Either way, all credits to the provider.

## API url
https://pplrq.herokuapp.com/quotes/

## Making requests
You can basically visit the url above to get a random quote or optionally enter `https://pplrq.herokuapp.com/quotes/<id>` in the address bar to get a quote with a specific id.

To get quotes by a specific author, you can simply append the author's name at the end of the url like so `https://pplrq.herokuapp.com/quotes/<author>`
PS: author names are case-sensitive

This `https://pplrq.herokuapp.com/quotes/Buddha` request for example would return
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

`https://pplrq.herokuapp.com/quotes/authors` returns and array of all available authors

`https://pplrq.herokuapp.com/quotes/all` returns an array of all available quotes.
