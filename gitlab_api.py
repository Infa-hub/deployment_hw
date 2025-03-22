import requests
from config import GITLAB_TOKEN

GITLAB_URL = 'https://git.miem.hse.ru/api/v4'

headers = {
    'Authorization': f'Bearer {GITLAB_TOKEN}',
    'Content-Type': 'application/json'
}

def get_user_info():
    user_url = f'{GITLAB_URL}/user'
    response = requests.get(user_url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_data['repos_count'] = len(get_user_projects(user_data['id']))
        user_data['followers'] = get_user_followers(user_data['id'])
        user_data['following'] = get_user_following(user_data['id'])
        return user_data
    else:
        print(f"Ошибка: {response.status_code}")
        return None

def get_user_projects(user_id):
    projects_url = f'{GITLAB_URL}/users/{user_id}/projects'
    response = requests.get(projects_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: {response.status_code}")
        return None

def get_user_followers(user_id):
    followers_url = f'{GITLAB_URL}/users/{user_id}/followers'
    response = requests.get(followers_url, headers=headers)
    if response.status_code == 200:
        return len(response.json())
    else:
        print(f"Ошибка: {response.status_code}")
        return 0

def get_user_following(user_id):
    following_url = f'{GITLAB_URL}/users/{user_id}/following'
    response = requests.get(following_url, headers=headers)
    if response.status_code == 200:
        return len(response.json())
    else:
        print(f"Ошибка: {response.status_code}")
        return 0