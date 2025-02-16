import requests

class TestApi():
    base_url = "https://poetrydb.org"

    def test_authors_is_accessible(self):
        url = self.base_url + "/authors"

        response = requests.get(url)

        actual_status_code = response.status_code
        expected_status_code = 200

        assert expected_status_code == actual_status_code

    def test_count_of_authors(self):
        url = self.base_url + "/authors"

        response = requests.get(url)

        response_json = response.json()
        actual_authors_count = len(response_json['authors'])
        expected_count = 129

        assert expected_count == actual_authors_count

    def test_ernest_title(self):
        author = "Ernest Dowson"
        title_url = f"/author/{author}/title"

        url = self.base_url + title_url
        response = requests.get(url)

        expected_earnest_title = [{'title': "The Moon Maiden's Song"}]
        actual_earnest_title = response.json()

        assert expected_earnest_title == actual_earnest_title

    def test_author_exact_poem_count(self):
        author = "Dickinson"
        title_url = f"/author,poemcount/{author};2/title"

        url = self.base_url + title_url
        response = requests.get(url)

        expected_titles_for_author = [{'title': 'Not at Home to Callers'}, {'title': 'Defrauded I a Butterfly --'}]
        actual_titles_for_author = response.json()

        assert expected_titles_for_author == actual_titles_for_author
