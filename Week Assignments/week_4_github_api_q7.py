import requests

# GitHub API base URL
base_url = "https://api.github.com"

# Search for users with location 'Mumbai'
search_url = f"{base_url}/search/users?q=location:Mumbai"
response = requests.get(search_url)
users = response.json().get('items', [])

# Initialize variables to track the newest user
newest_user = None
newest_creation_date = None

# Iterate through the users to find those with >120 followers
for user in users:
    username = user['login']
    user_url = f"{base_url}/users/{username}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    #print(user_data)
    
    if user_data.get('followers', 0) > 120:
        creation_date = user_data.get('created_at')
        if newest_creation_date is None or creation_date > newest_creation_date:
            newest_creation_date = creation_date
            newest_user = username

if newest_user:
    print(f"The newest user in Mumbai with over 120 followers is {newest_user}, created on {newest_creation_date}.")
else:
    print("No users found with over 120 followers in Mumbai.")
