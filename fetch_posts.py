import requests

def fetch_posts():
    api_url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            posts = response.json()

            # Display the posts
            for post in posts:
                print(f"Post #{post['id']}: {post['title']}")
        else:
            print(f"Error: Unable to fetch posts. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_posts()

