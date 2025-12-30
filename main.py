import client


def main():
    koetomo = client.Koetomo()
    koetomo.login("test@gmail.com", "123456")

    koetomo.post_feed("Hello World! from Python")

    response = koetomo.get_feed(10 * 5)

    feed_posts = response.get("feed_posts", [])
    user_info = response.get("user_info", [])

    user_map = {u["user_id"]: u for u in user_info}

    for post in feed_posts:
        user = user_map.get(post["user_id"], {})

        if post.get("description") is None:
            continue

        if user.get("sex") is 1:
            continue

        print(
            user.get("sex", "[不明]"),
            user.get("age", "[不明]"),
            user.get("user_id", "[不明]"),
            user.get("name", "[不明]"),
            post.get("id", "[不明]"),
            post.get("description", "[不明]"),
        )

        # image_file_path
        # voice_file_path


if __name__ == "__main__":
    main()
