import os

import requests


def get_github_user():
    try:
        return os.environ["ISSUE_HUNT_GITHUB_USER"]
    except KeyError:
        pass


def get_github_token():
    try:
        return os.environ["ISSUE_HUNT_GITHUB_TOKEN"]
    except KeyError:
        pass


def get_issue(repo, labels):
    endpoint = f'/repos/{repo}/issues'
    params = {'labels': labels, 'state': 'open'}
    url = github_root_url + endpoint

    if (useAuth):
        r = requests.get(url, params=params, auth=(user, token))
    else:
        r = requests.get(url, params=params)
    return r.json()


def print_head(repo, labels):
    header = f'🤗 #repo: {repo} #labels:{labels}'
    bar = "=" * (len(header) + 3)
    print(bar)
    print(header)
    print(bar)


def print_issue(issue):
    has_pull_request = f'{("pull_requests" in issue)}'[0]
    print(f'#{str(issue["number"]).ljust(6, " ")}| {issue["title"]} | C:{issue["comments"]}/PR:{has_pull_request}')


github_root_url = 'http://api.github.com'

user = get_github_user()
token = get_github_token()
useAuth = (user and token)

search_list = [
    {'repo': 'netlify/netlify-cms', 'labels': {'area: api', 'area: api'}},
    {'repo': 'netlify/netlify-cms', 'labels': {'area: api', 'area: api'}},
]

if useAuth:
    print(f'Using auth token with username: {user}')
else:
    print("No auth mode")

for i, repo_to_check in enumerate(search_list):
    repo = repo_to_check['repo']
    labels = repo_to_check['labels']
    print_head(repo, labels)
    issues = get_issue(repo, labels)
    for issue in issues:
        print_issue(issue)
