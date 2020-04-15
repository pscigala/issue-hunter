import requests

github_root_url = 'http://api.github.com'


def get_issue(repo, labels):
    endpoint = f'/repos/{repo}/issues'
    params = {'labels': labels, 'state': 'open'}
    url = github_root_url + endpoint
    r = requests.get(url, params=params)
    return r.json()


repo = 'netlify/netlify-cms'
labels = {'area: api', 'area: api'}
print("=====================================")
print(f'#repo: {repo} #labels:{labels}')
print("=====================================")
issues = get_issue('netlify/netlify-cms', labels)
for issue in issues:
    print(issue)
    print(issue['title'])
