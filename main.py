from github import Github

# Githubオブジェクトの作成
print('Github user_name: ', end='')
user_name = input()
print('Github password: ', end='')
password = input()
g = Github(user_name, password)

print('Authentication OK')

# Githubオブジェクトからリポジトリ名でリポジトリオブジェクトを作成
print('Repository name: ', end='')
repo_name = input()
repo = g.get_user().get_repo(repo_name)

# Repositoryオブジェクトからissueオブジェクトを作成と同時に投稿
print('issue title: ', end='')
issue_title = input()
print('issue body: ', end='')
issue_body = input()

issue = repo.create_issue(issue_body, issue_title)
print('issue created')
