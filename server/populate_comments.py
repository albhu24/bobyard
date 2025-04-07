import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()

from db.models import Comment

json_file_path = './comments.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)
    comments = data['comments']

    for comment_data in comments:
        Comment.objects.create(
            id=comment_data['id'],
            author=comment_data['author'],
            text=comment_data['text'],
            date=comment_data['date'],
            likes=comment_data['likes'],
            image=comment_data['image']
        )

print("uploaded")