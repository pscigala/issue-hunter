import requests

github_root_url = 'http://api.github.com'
github_token = ''
github_username = ''


def get_issue(repo, labels):
    endpoint = f'/repos/{repo}/issues'
    params = {'labels': labels, 'state': 'open'}
    url = github_root_url + endpoint
    r = requests.get(url, params=params, auth=(github_username, github_token))
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


search_list = [
    {'repo': 'netlify/netlify-cms', 'labels': {'area: api', 'area: api'}},
    {'repo': 'netlify/netlify-cms', 'labels': {'area: api', 'area: api'}},
]

for i, repo_to_check in enumerate(search_list):
    repo = repo_to_check['repo']
    labels = repo_to_check['labels']
    print_head(repo, labels)
    issues = get_issue(repo, labels)
    for issue in issues:
        print_issue(issue)
