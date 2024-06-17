import httpx
from prefect import flow, task

@task
def fetch_repo_stars(repo_owner: str, repo_name: str):
    """Fetch the number of stars for a GitHub repository."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo_info = response.json()
    return repo_info['stargazers_count']

@flow(log_prints=True)
def display_repo_stars(repo_owner: str = "UniversalExtensionsDev", repo_name: str = "ue-prefect"):
    """Fetch and display the number of stars for a GitHub repository."""
    stars = fetch_repo_stars(repo_owner, repo_name)
    print(f"The repository {repo_owner}/{repo_name} has {stars} stars.")

if __name__ == "__main__":
    display_repo_stars()
