# from .models import Post, Category
#
# def navbar(request):
#     categories = Category.objects.all()
#
#     dic = dict()
#     for category in categories:
#         item = {
#             'category'  :   category.name,
#             'posts'     :   's'
#         }
#         dic[category.name] = Post.objects.filter(category=category).only("title")
#     return {'categories':dic}
