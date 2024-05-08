import json

data_post = """
{
    "userId": 1,
    "id": 1,
    "isPublished": false,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipitsuscipit recusandae consequuntur expedita et cumreprehenderit molestiae ut ut quas totamnostrum rerum est autem sunt rem eveniet architecto",
    "emojis": ["happy", "sad", "angry"],
    "isReported": null
}
"""

print(data_post, type(data_post))

post_dict = json.loads(data_post)
print(post_dict, type(post_dict))
print(post_dict["userId"], type(post_dict["userId"]))
print(post_dict["isPublished"], type(post_dict["isPublished"]))
print(post_dict["emojis"], type(post_dict["emojis"]))
print(post_dict["isReported"], type(post_dict["isReported"]))