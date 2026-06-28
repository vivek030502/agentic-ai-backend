from app.integrations.github.client import GitHubClient

client = GitHubClient()

print("=" * 60)
print("GitHub Client")
print("=" * 60)

print(client.base_url)
print(client.headers)