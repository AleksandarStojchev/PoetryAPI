# PoetryAPI

**test_authors_is_accessible**

Sends a GET request to /authors to check if the endpoint is accessible (expects a 200 status code).

**test_count_of_authors**

Fetches the list of authors from /authors and verifies that the number of authors matches the expected 129.

**test_ernest_title**

Retrieves poem titles by Ernest Dowson and checks if the response contains the expected title: "The Moon Maiden's Song".

**test_author_exact_poem_count**

Requests exactly 2 poems by Emily Dickinson and verifies if the API returns the expected poem titles.
