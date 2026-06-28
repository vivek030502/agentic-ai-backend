from pprint import pprint

from app.integrations.github.client import GitHubClient

client = GitHubClient()

user = client.get_authenticated_user()

print("=" * 80)
print("AUTHENTICATED GITHUB USER")
print("=" * 80)

pprint(user)