import datetime
import json
import os

import requests

import config
import template


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

if useAuth:
    print(f'Using auth token with username: {user}')
else:
    print("No auth mode")


def store_request_meta_json(request_meta_json):
    with open(f'out-{str(datetime.datetime.now().timestamp())}.json', 'a') as json_file:
        json.dump(request_meta_json, json_file)


issues_from_all_repos = []


def create_request_meta(repo, labels, issues):
    issues_from_all_repos.append(
        [{'repo': repo, 'labels': labels, 'request_date': str(datetime.datetime.today()), 'count': len(issues),
          'data': issues}])


def store_html(request_meta_json):
    with open(f'out-{str(datetime.datetime.now().timestamp())}.html', 'a') as file:
        file.write(template.render(request_meta_json))


for i, repo_to_search in enumerate(config.search_list):
    repo = repo_to_search['repo']
    labels = repo_to_search['labels']
    print_head(repo, labels)
    issues = get_issue(repo, labels)
    create_request_meta(repo, labels, issues)
    for issue in issues:
        print_issue(issue)

store_request_meta_json(issues_from_all_repos)

store_html(issues_from_all_repos)
