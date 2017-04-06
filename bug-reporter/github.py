import requests
import subprocess
import os

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
    if results:
        return(results["items"])
    else:
        return(None)

def getReleaseVersion():
    loc = os.getcwd()
    process = subprocess.run(["git", "-C", loc, "describe"], stdout=subprocess.PIPE)
    output = process.stdout.decode('utf-8')
    if('fatal' in output):
        return(False)
    return(output.rstrip('\n'))

def getRemotes():
    loc = os.getcwd()
    process = subprocess.run(["git", "-C" ,loc, "remote" ,"-v"], stdout=subprocess.PIPE)
    output = process.stdout.decode('utf-8')
    output = output.decode('utf-8')
