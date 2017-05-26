from github import Github
from github.Repository import Repository

# Githubオブジェクトの作成
g = Github.("user_name", "password")

# Githubオブジェクトからリポジトリ名でリポジトリオブジェクトを作成
repo = g.get_user().get_repo("your repository name")

# Repositoryオブジェクトからissueオブジェクトを作成と同時に投稿
issue = repo.create_issue('title', 'body')




