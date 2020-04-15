import requests

github_root_url = 'http://api.github.com'


def get_issue(repo, labels):
    endpoint = f'/repos/{repo}/issues'
    params = {'labels': labels, 'state': 'open'}
    url = github_root_url + endpoint
    r = requests.get(url, params=params)
    return r.json()


def print_head(repo, labels):
    header = f'#repo: {repo} #labels:{labels}'
    bar = "=" * (len(header) + 3)
    print(bar)
    print(header)
    print(bar)


def print_issue(issue):
    has_pull_request=f'{("pull_requests" in issue)}'[0]
    print(f' C:{issue["comments"]}/PR:{has_pull_request} 🤗 #{issue["number"]} {issue["title"]}')


repo = 'netlify/netlify-cms'
labels = {'area: api', 'area: api'}

issues = get_issue('netlify/netlify-cms', labels)

print_head(repo, labels)
for issue in issues:
    print_issue(issue)
