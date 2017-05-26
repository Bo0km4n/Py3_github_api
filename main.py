from github import Github
from github.Repository import Repository
# ユーザー情報の入った.pyファイル
import credential

# Githubオブジェクトの作成
g = Github(credential.user_name, credential.password)

# Githubオブジェクトからリポジトリ名でリポジトリオブジェクトを作成
repo = g.get_user().get_repo(credential.repo_name)

# Repositoryオブジェクトからissueオブジェクトを作成と同時に投稿
print('create issue...')
issue = repo.create_issue('title', 'body')
print('finish!')
