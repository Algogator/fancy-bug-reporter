import requests
# POST /repos/:owner/:repo/issues
API = "https://api.github.com"
head = {'Authorization': 'token '}

def postIssue(owner, repo, title, body):
    URL = "{0}/repos/{1}/{2}/issues".format(API, owner, repo)
    r = requests.post(URL, json={
        "title": title,
        "body": body},
        headers=head)


def searchIssue(query, repo):
    params = {"q": repo + " " + query}
    r = requests.get("{0}/search/issues".format(API),
                     headers=head, params=params)
    results = r.json()
    return(results["items"])
