from github import Github

# Githubアカウント情報の入力
print('Github user_name: ', end='')
user_name = input()
print('Github password: ', end='')
password = input()

# GitHubオブジェクトの作成
g = Github(user_name, password)

print('Authentication OK')

# リポジトリ名を入力
print('Repository name: ', end='')
repo_name = input()

# リポジトリ名からRepositoryオブジェクトを生成
repo = g.get_user().get_repo(repo_name)

# issueのタイトルと本文を入力
print('issue title: ', end='')
issue_title = input()
print('issue body: ', end='')
issue_body = input()

# issueの投稿とオブジェクトの生成
issue = repo.create_issue(issue_body, issue_title)

print('issue created')
