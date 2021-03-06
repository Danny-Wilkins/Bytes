<h1>Bytes</h1>

<h2>Inspiration</h2>

"I never actually know if I'm getting a good deal anymore..."

While enjoying some free pizza, we began to discuss the struggles of being broke students in New York City.

"The food is good, but it's also really expensive."

"How much is too much for good food?"

"Bad food is cheap food and that's all that matters."

There are countless websites to check out food in your area, but they're all missing a critical element: a comparison with other local restaurants to determine if the food is a good value.

<h2>What it does</h2>

Bytes compares the ratings and cost of a restaurant to other restaurants around you to help you get the best food for your money. Bytes, taking into account cost/rating ratio of local restaurants, calculates a score and assigns a letter grade determining the quality of the deal. The higher the score, the better the deal!

<h2>How we built it</h2>

Back-end dependencies: Requests, BeautifulSoup, NumPy, SciPy, GeoPy

Bytes is written in Python, using the TripAdvisor and Yelp APIs. GeoPy was used to get location; its ability to easily acquire latitude and longitude coordinates worked well with TripAdvisor's map request. From there, the TripAdvisor API generates a list of restaurants within the specified distance feeds their cost and rating into SciPy, which calculates a linear regression based on this data. From there, the restaurants are rated based on their actual position either above or below the regression line; above meaning a better than average deal, and below meaning worse than average. NumPy is used to simplify some of the mathematical work behind this. The data is returned with the name of the restaurant, the score, and the letter grade. The Yelp API is used to relevant information factoring into our formula and search results. Information not accessible through the Yelp API was obtained through web scraping using the requests and beautifulsoup libraries. It allows for searching through keywords, with flexibility for a smoother user experience. The front end was written mostly in HTML. JavaScript and Flask was used to integrate front end (mostly user input) with the back end. Bootstrap was used for a sleek interface and compatibility with mobile devices.

<h2>Challenges we ran into</h2>

Making the front end was challenging because none of us actually knew how to do it or had any real experience with that. The greatest challenge by far has been using Flask to tie the front and back ends together, with the largest obstacle being getting user input into the back end.

<h2>Accomplishments that we're proud of</h2>

The front end came out very nicely considering our lack of previous experience. At present, Bytes is extensible (to hotels, attractions, and other things under the TripAdvisor and Yelp APIs), and it is good at error handling. Being able to learn new APIs quickly is a skill we gladly continue to improve upon. We are also proud of the idea we used for rating the restaurants: it makes sense, is efficient, and is something other than coding that we came up with.

#What we learned
We learned how to use HTML and JavaScript, how to use a number of APIs and libraries to obtain and process data, and we learned a bit about how Flask works to tie the front and back ends together.

#What's next for Bytes
Bytes, in its current state, works very efficiently for finding local deals on food. However, this behavior could easily be extended to other areas such as hotels, attractions, and other things. Adding other features such as displaying menus, having user accounts to allow users to save favorites and view eating history, share recommendations with friends, etc. Bytes could also (in a non-evil way) collect data about its users, using this information to improve user experience and perhaps even local food options. Most importantly, cleaning up the integration between the front and back ends using Flask would be great (as in do it right this time).
