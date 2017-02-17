import argparse
from github import postIssue, searchIssue
from sys_info import sys_info

parser = argparse.ArgumentParser()
parser.add_argument("repo",  help="Repository name")
parser.add_argument("owner",  help="Repository owner name")
args = parser.parse_args()
repo = args.repo
owner = args.owner

title = input("Descriptive title of the bug: (5 - 10 words) ")
query = 'repo:{0}/{1}'.format(owner, repo)
search_results = searchIssue(title, query)
for i in search_results:
    print(i["title"], " | ", i["html_url"])
ans = input("Are you sure this bug isn't already there? [y/n] ")
if(ans == 'y'):
    print("Steps to reproduce the error: (Type end to stop) ")
    steps = []
    i = 0
    while(True):
        x = input("Step {0}: ".format(i))
        if x == 'end':
            break
        steps.append(x)
        i += 1
    e_outcome = input("Expected outcome: ")
    a_outcome = input("Actual outcome: ")
    sys = sys_info()
    body = "#### Steps to reproduce:\n"
    s = '\n'.join('{}. {}'.format(*k) for k in enumerate(steps, start=1))
    body = body + s
    body = "{0}\n#### Expected outcome:\n{1}\n#### Actual outcome:\n{2}\n#### System info:\n- {3} {4}\n- {5}".format(
        body, e_outcome, a_outcome, *sys)
    postIssue(owner, repo, title, body)
