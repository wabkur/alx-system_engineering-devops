
#!/usr/bin/python3
"""script that queries subs on a given reddit subreddit"""


def number_of_subscribers(subreddit):
    """Return the number of subs on a given subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
