import requests
import json

def evaluate_repo(repo_url):
    parts = repo_url.replace("https://github.com/", "").split("/")
    owner, repo = parts[0], parts[1]

    api = f"https://api.github.com/repos/{owner}/{repo}"
    data = requests.get(api).json()

    contents_api = f"https://api.github.com/repos/{owner}/{repo}/contents"
    contents = requests.get(contents_api).json()

    score = 0
    strengths = []
    weaknesses = []

    # License check
    if data.get("license"):
        score += 10
        strengths.append("Repository has a license")
    else:
        weaknesses.append("No license")

    # Description check
    if data.get("description"):
        score += 10
        strengths.append("Has project description")
    else:
        weaknesses.append("No description")

    # Community interest
    if data.get("stargazers_count", 0) > 50:
        score += 20
        strengths.append("Good community interest")
    else:
        weaknesses.append("Low star count")

    # Forks
    if data.get("forks_count", 0) > 10:
        score += 10
        strengths.append("Project is forked by others")

    # README check
    readme_api = f"https://api.github.com/repos/{owner}/{repo}/readme"
    readme_response = requests.get(readme_api)
    if readme_response.status_code == 200:
        score += 15
        strengths.append("README documentation present")
    else:
        weaknesses.append("Missing README")

    # Tests folder check
    has_tests = any("test" in item["name"].lower() for item in contents if isinstance(contents, list))
    if has_tests:
        score += 20
        strengths.append("Repository contains tests")
    else:
        weaknesses.append("No tests detected")

    # CI/CD workflow check
    ci_api = f"https://api.github.com/repos/{owner}/{repo}/contents/.github/workflows"
    ci_response = requests.get(ci_api)
    if ci_response.status_code == 200:
        score += 15
        strengths.append("CI/CD workflow detected")
    else:
        weaknesses.append("No CI/CD workflow found")

    return {
        "repo": repo_url,
        "score": score,
        "strengths": strengths,
        "weaknesses": weaknesses
    }


if __name__ == "__main__":
    import sys

    repos = sys.argv[1:]
    results = []

    for repo in repos:
        results.append(evaluate_repo(repo))

    # Find best repository
    best_repo = max(results, key=lambda x: x["score"])

    output = {
        "results": results,
        "best_repository": best_repo["repo"],
        "best_score": best_repo["score"]
    }

    print(json.dumps(output, indent=2))
