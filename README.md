# Popular Quotes API

A simple a RESTful API built with Flask. This api was built for learning sake.

The quotes provided by this api were originally sourced from a resource I can't remember. Either way, all credits to the provider.

## API url
https://.../popular-quotes/

## Making requests
You can basically visit the url above to get a random quote or optionally enter `https://.../popular-quotes/<id>` in the address bar to get a quote with a specific id.

To get quotes by a specific author, you can simply append the author's name at the end of the url like so `https://.../popular-quotes/<author>`;

This `https://.../popular-quotes/` request for example would return
```
[
    {
        "id": 2,
        "author": "Yogi Berra",
        "quote": "You can observe a lot just by watching."
    },
    {
        "id": 9,
        "author": "Yogi Berra",
        "quote": "Life is a learning experience, only if you learn."
    },
    {
        "id": 437,
        "author": "Yogi Berra",
        "quote": "You got to be careful if you don't know where you're going, because you might not get there."
    }
]
```

Enter `https://.../popular-quotes/all` to get all available quotes.

*All valid responses returned are in a json format.*
