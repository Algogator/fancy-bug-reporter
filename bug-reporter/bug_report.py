import argparse
from github import postIssue, searchIssue, getReleaseVersion
from sys_info import sys_info
import sys

ans = 'y'

parser = argparse.ArgumentParser()
parser.add_argument("repo", nargs='?', help="Repository name")
parser.add_argument("owner", nargs='?', help="Repository owner name")
args = parser.parse_args()
repo = args.repo
owner = args.owner
# if not (repo and owner):

query = 'repo:{0}/{1}'.format(owner, repo)

title = input("Descriptive title of the bug: (5 - 10 words): ")
search_results = searchIssue(title, query)
if search_results:
    for i in search_results:
        print(i["title"], " | ", i["html_url"])
        ans = input("Are you sure this bug isn't already there? [y/n] ")
if(ans == 'y'):
    # Find the version of project used
    project_version = getReleaseVersion()
    if not project_version:
        project_version = input("Project version: ")

    # Find version of tech used
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
    body = "{0}\n#### Expected outcome:\n{1}\n#### Actual outcome:\n{2}\n#### Info:\n Release version: {3}\n#### System info:\n- {4} {5}\n- {6}".format(
        body, e_outcome, a_outcome, project_version, *sys)
    postIssue(owner, repo, title, body)
