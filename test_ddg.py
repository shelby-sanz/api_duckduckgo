import requests
import pytest


# make api call to duckduckgo
def make_call():
    # make api request and read as json (dict)
    search_string = 'presidents of the united states'
    resp = requests.get(f'http://api.duckduckgo.com/?q={search_string}&format=json')
    rsp_data = resp.json()

    # get texts from related topics and put them in a large string for easy iteration
    texts = ''
    for i in rsp_data['RelatedTopics']:
        texts += i['Text']

    # return texts
    return texts


# list of president last names
president_last_names = ['washington', 'adams', 'jefferson', 'madison', 'monroe', 'adams', 'jackson', 'buren',
                        'harrison', 'tyler', 'polk', 'taylor', 'fillmore', 'pierce', 'buchanan', 'lincoln',
                        'johnson', 'grant', 'hayes', 'garfield', 'arthur', 'cleveland', 'harrison', 'cleveland',
                        'mckinley', 'roosevelt', 'taft', 'wilson', 'harding', 'coolidge', 'hoover', 'roosevelt',
                        'truman', 'eisenhower', 'kennedy', 'johnson', 'nixon', 'ford', 'carter', 'reagan', 'bush',
                        'clinton', 'bush', 'obama', 'trump', 'biden']


# pytest to assert if each president last name is found in duckduckgo response
@pytest.mark.parametrize("item", president_last_names)
def test_president_names(item):
    texts = make_call()
    assert item in texts.lower()
