def css():
    return f'''
<title>Issue Hunter</title>
<link href="https://unpkg.com/material-components-web@v4.0.0/dist/material-components-web.min.css" rel="stylesheet">
<script src="https://unpkg.com/material-components-web@v4.0.0/dist/material-components-web.min.js"></script>
'''


def row(request_meta_json):
    rows = ''
    for repo in request_meta_json:
        for repo_issues in repo:
            for issue in repo_issues['data']:
                rows += f'''
<tr class="mdc-data-table__row">
    <td class="mdc-data-table__cell mdc-data-table__cell--numeric">{issue["number"]}</td>
    <td class="mdc-data-table__cell">{issue["title"]}</td>
    <td class="mdc-data-table__cell mdc-data-table__cell--numeric">{issue["comments"]}</td>
    <td class="mdc-data-table__cell mdc-data-table__cell--numeric"><a href="{issue["html_url"]}" target="_blank">Link</a></td>
</tr>
'''
    return rows


def render(issues):
    return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {css()}
</head>
<body>
<div class="mdc-data-table">
  <table class="mdc-data-table__table">
    <thead>
      <tr class="mdc-data-table__header-row">
        <th class="mdc-data-table__header-cell" role="columnheader" scope="col">#Number</th>
        <th class="mdc-data-table__header-cell" role="columnheader" scope="col">Title</th>
        <th class="mdc-data-table__header-cell" role="columnheader" scope="col">Comments</th>
        <th class="mdc-data-table__header-cell" role="columnheader" scope="col">Link</th>
      </tr>
    </thead>
    <tbody class="mdc-data-table__content">
      {row(issues)}
    </tbody>
  </table>
</div>
</body>
</html>'''
