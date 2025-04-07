from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def comments(request):
    if request.method == 'GET':
        try:
            comments = Comment.objects.order_by('-date')
            data = {
                "comments": [{
                    "id": comment.id,
                    "author": comment.author,
                    "text": comment.text,
                    "date": comment.date,
                    "likes": comment.likes,
                    "image": comment.image,
                } for comment in comments]
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            data = request.data
            comment = Comment.objects.create(
                id=data.get("id"),
                author=data.get("author"),
                text=data.get("text"),
                date=data.get("date"),
                likes=data.get("likes"),
                image=data.get("image")
            )
            return Response({"message": "Comment created", "id": comment.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            data = request.data
            comment_id = data.get("id")
            if not comment_id:
                return Response({"error": "No comment ID provided"}, status=status.HTTP_400_BAD_REQUEST)

            comment = Comment.objects.get(id=comment_id)
            # Update fields
            comment.author = data.get("author", comment.author)
            comment.text = data.get("text", comment.text)
            comment.date = data.get("date", comment.date)
            comment.likes = data.get("likes", comment.likes)
            comment.image = data.get("image", comment.image)
            comment.save()

            return Response({"message": f"Comment {comment_id} updated"}, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        try:
            comment_id = request.GET.get("id")
            if not comment_id:
                return Response({"error": "No comment ID provided"}, status=status.HTTP_400_BAD_REQUEST)
            
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return Response({"message": f"Comment {comment_id} deleted"}, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
