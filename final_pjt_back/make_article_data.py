import os
import random
from faker import Faker
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_pjt.settings')
application = get_wsgi_application()

from accounts.models import User
from articles.models import Article, Comment

fake = Faker()

def create_articles_and_comments(n):
    users = User.objects.all()

    for _ in range(n):
        # Create an article
        user = random.choice(users)
        title = fake.sentence(nb_words=6)
        content = fake.text(max_nb_chars=2000)
        article = Article.objects.create(user=user, title=title, content=content)

        # Create comments for the article
        for _ in range(random.randint(1, 10)):  # Each article can have between 1 and 10 comments
            user = random.choice(users)
            content = fake.text(max_nb_chars=200)
            Comment.objects.create(article=article, user=user, content=content)

create_articles_and_comments(80)