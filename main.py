import instaloader
from instaloader import Post

def shortCode(url):
    # gets short code from post url
    return url.split("/")[-2]

# Get Instance
L = instaloader.Instaloader()

url = input("Enter URL: ")

code = shortCode(url)

post = Post.from_shortcode(L.context, code)
L.download_post(post, target="Images")