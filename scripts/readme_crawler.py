import requests


def get_readme(username, repository):
    url = f"https://raw.githubusercontent.com/{username}/{repository}/master/README.md"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def main():
    username = input("Enter GitHub username: ")
    repository = input("Enter repository name: ")
    readme_content = get_readme(username, repository)
    if readme_content:
        print("README successfully fetched.")
        with open("./temp_readme.md", "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("README saved successfully.")
    else:
        print("Failed to fetch README.")


if __name__ == "__main__":
    main()
