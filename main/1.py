from django.http import HttpResponse

from main.models import Question
from django.contrib.auth.models import User


def test2(req):
    # создаем тонну комнат
    import random
    from datetime import datetime, timedelta

    programming_questions = [
        {
            "q": "What are the differences between Python 2 and Python 3?",
            "text": "Explain the major differences between Python 2 and Python 3 in terms of syntax, features, and compatibility.",
        },
        {
            "q": "How does a blockchain work?",
            "text": "Describe the fundamental concepts and principles behind blockchain technology, including its structure, consensus mechanisms, and use cases.",
        },
        {
            "q": "What are RESTful APIs?",
            "text": "Define what RESTful APIs are and explain their key principles, such as statelessness, uniform interface, and client-server architecture.",
        },
        {
            "q": "What is the difference between machine learning and deep learning?",
            "text": "Differentiate between machine learning and deep learning techniques, and discuss their applications, algorithms, and training processes.",
        },
        {
            "q": "Explain the concept of microservices architecture.",
            "text": "Discuss the principles and benefits of microservices architecture, including scalability, modularity, and independent deployment.",
        },
        {
            "q": "What is Docker and how does it work?",
            "text": "Provide an overview of Docker containerization technology and explain its components, such as Docker Engine, images, and containers.",
        },
        {
            "q": "What are design patterns in software engineering?",
            "text": "Describe the concept of design patterns and provide examples of commonly used design patterns in software development.",
        },
        {
            "q": "How do you handle errors and exceptions in Python?",
            "text": "Explain error handling techniques in Python, including try-except blocks, raising exceptions, and handling specific types of errors.",
        },
        {
            "q": "What is the difference between a list and a tuple in Python?",
            "text": "Differentiate between lists and tuples in Python based on their mutability, syntax, and typical use cases.",
        },
        {
            "q": "What are the advantages of using version control systems?",
            "text": "Discuss the benefits of version control systems, such as Git, in software development projects, including collaboration, history tracking, and code management.",
        },
        {
            "q": "What is the difference between SQL and NoSQL databases?",
            "text": "Compare and contrast SQL and NoSQL databases in terms of data model, scalability, consistency, and use cases.",
        },
        {
            "q": "Explain the concept of recursion in programming.",
            "text": "Define recursion and discuss its implementation in programming languages, including base case, recursive case, and stack usage.",
        },
        {
            "q": "How does a binary search algorithm work?",
            "text": "Describe the binary search algorithm and its implementation, including the iterative and recursive approaches, time complexity, and use cases.",
        },
        {
            "q": "What are the SOLID principles in object-oriented design?",
            "text": "Discuss the five SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) and their importance in object-oriented design.",
        },
    ]
    topics = ["Python", "C++", "Java", "JavaScript", "Ruby"]
    # topics = Topic.objects.all()
    # users = User.objects.all()
    users = User.objects.exclude(username="Den")
    for u in users:
        print(u.username)
    for q in programming_questions:

        try:
            today = datetime.now()
            random_days = random.randint(
                0, 700
            )  # Randomly select days within one month
            random_timedelta = timedelta(hours=random_days)
            date = today - random_timedelta

            random_days = random.randint(
                0, random_days
            )  # Randomly select days within one month
            random_timedelta = timedelta(hours=random_days)
            upd = date + random_timedelta

            # date случайная дата от сегодня до месяца назад
            # upd случайная дата от сегодня до date

            quest = Question.objects.create(
                autor=random.choice(users),
                title=q["q"],
                text=q["text"],
                teg=random.choice(topics),
            )
            print(random.choice(topics))
            quest.save()
            # из за auto_now_add и auto_now которые не сами устанавливают дату при сохранинии,  приходится устанавливать дату отдельно через update
            Question.objects.filter(id=quest.id).update(created_at=date, updated_at=upd)
        except:
            pass

    return HttpResponse("test1")


# def test2(req):
#     # создаем тонну юзеров
#     usernames = [
#         "happy_daisy",
#         "friendly_fox",
#         "cheerful_bee",
#         "sunny_lemon",
#         "kind_dolphin",
#         "joyful_butterfly",
#         "gentle_rainbow",
#         "bright_sunshine",
#         "peaceful_ocean",
#         "smiling_flower",
#         "laughing_panda",
#         "calm_seashell",
#         "loving_kitten",
#         "hopeful_raindrop",
#         "warm_cuddle",
#     ]

#     for username in usernames:
#         try:
#             user = User.objects.create(username=username)
#             user.set_unusable_password()  # разрешаем устанавливать плохой пасспорт
#             user.set_password("1")  # всем юзерам ставим единицу в пароль
#             user.save()
#             print(user)
#         except:
#             pass

#     return HttpResponse("test2")


test2()
