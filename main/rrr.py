import random
from django.http import HttpResponse

# from .models import Question
from .models import User


# def test2(req):
#     # создаем тонну комнат
#     import random
#     from datetime import datetime, timedelta

#     programming_questions = [
#         {
#             "q": "What are the differences between Python 2 and Python 3?",
#             "text": "Explain the major differences between Python 2 and Python 3 in terms of syntax, features, and compatibility.",
#         },
#         {
#             "q": "How does a blockchain work?",
#             "text": "Describe the fundamental concepts and principles behind blockchain technology, including its structure, consensus mechanisms, and use cases.",
#         },
#         {
#             "q": "What are RESTful APIs?",
#             "text": "Define what RESTful APIs are and explain their key principles, such as statelessness, uniform interface, and client-server architecture.",
#         },
#         {
#             "q": "What is the difference between machine learning and deep learning?",
#             "text": "Differentiate between machine learning and deep learning techniques, and discuss their applications, algorithms, and training processes.",
#         },
#         {
#             "q": "Explain the concept of microservices architecture.",
#             "text": "Discuss the principles and benefits of microservices architecture, including scalability, modularity, and independent deployment.",
#         },
#         {
#             "q": "What is Docker and how does it work?",
#             "text": "Provide an overview of Docker containerization technology and explain its components, such as Docker Engine, images, and containers.",
#         },
#         {
#             "q": "What are design patterns in software engineering?",
#             "text": "Describe the concept of design patterns and provide examples of commonly used design patterns in software development.",
#         },
#         {
#             "q": "How do you handle errors and exceptions in Python?",
#             "text": "Explain error handling techniques in Python, including try-except blocks, raising exceptions, and handling specific types of errors.",
#         },
#         {
#             "q": "What is the difference between a list and a tuple in Python?",
#             "text": "Differentiate between lists and tuples in Python based on their mutability, syntax, and typical use cases.",
#         },
#         {
#             "q": "What are the advantages of using version control systems?",
#             "text": "Discuss the benefits of version control systems, such as Git, in software development projects, including collaboration, history tracking, and code management.",
#         },
#         {
#             "q": "What is the difference between SQL and NoSQL databases?",
#             "text": "Compare and contrast SQL and NoSQL databases in terms of data model, scalability, consistency, and use cases.",
#         },
#         {
#             "q": "Explain the concept of recursion in programming.",
#             "text": "Define recursion and discuss its implementation in programming languages, including base case, recursive case, and stack usage.",
#         },
#         {
#             "q": "How does a binary search algorithm work?",
#             "text": "Describe the binary search algorithm and its implementation, including the iterative and recursive approaches, time complexity, and use cases.",
#         },
#         {
#             "q": "What are the SOLID principles in object-oriented design?",
#             "text": "Discuss the five SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) and their importance in object-oriented design.",
#         },
#     ]
#     topics = ["Python", "C++", "Java", "JavaScript", "Ruby"]
#     # topics = Topic.objects.all()
#     # users = User.objects.all()
#     users = User.objects.exclude(username="Den")
#     for u in users:
#         print(u.username)
#     for q in programming_questions:

#         try:
#             today = datetime.now()
#             random_days = random.randint(
#                 0, 700
#             )  # Randomly select days within one month
#             random_timedelta = timedelta(hours=random_days)
#             date = today - random_timedelta

#             random_days = random.randint(
#                 0, random_days
#             )  # Randomly select days within one month
#             random_timedelta = timedelta(hours=random_days)
#             upd = date + random_timedelta

#             # date случайная дата от сегодня до месяца назад
#             # upd случайная дата от сегодня до date

#             quest = Question.objects.create(
#                 autor=random.choice(users),
#                 title=q["q"],
#                 text=q["text"],
#                 teg=random.choice(topics),
#             )
#             print(random.choice(topics))
#             quest.save()
#             # из за auto_now_add и auto_now которые не сами устанавливают дату при сохранинии,  приходится устанавливать дату отдельно через update
#             Question.objects.filter(id=quest.id).update(created_at=date, updated_at=upd)
#         except:
#             pass

#     return HttpResponse("test1")


def test2(req):
    # создаем тонну юзеров
    usernames = [
        "happy_daisy",
        "friendly_fox",
        "cheerful_bee",
        "sunny_lemon",
        "kind_dolphin",
        "joyful_butterfly",
        "gentle_rainbow",
        "bright_sunshine",
        "peaceful_ocean",
        "smiling_flower",
        "laughing_panda",
        "calm_seashell",
        "loving_kitten",
        "hopeful_raindrop",
        "warm_cuddle",
        "playful_bunny",
        "breezy_wind",
        "soothing_waves",
        "delightful_bird",
        "grateful_tree",
        "optimistic_star",
        "radiant_moon",
        "lovely_cloud",
        "serene_river",
        "gentle_whisper",
        "kindhearted_fawn",
        "tranquil_meadow",
        "harmonious_song",
        "serendipity_smile",
        "cozy_blanket",
        "giggling_squirrel",
        "merry_garden",
        "friendly_glow",
        "compassionate_heart",
        "whimsical_rain",
        "sparkling_eyes",
        "magical_spark",
        "blissful_sunset",
        "tender_leaf",
        "chirpy_robin",
        "dancing_buttercup",
        "dreamy_wish",
        "graceful_breeze",
        "serenity_garden",
        "happiness_hummingbird",
        "mellow_melody",
        "harmony_hug",
        "lively_ladybug",
        "radiant_breeze",
        "smiling_sunflower",
    ]
    it_professions = [
        "Software Developer",  # Разработчик программного обеспечения
        "Web Developer",  # Веб-разработчик
        "Mobile App Developer",  # Разработчик мобильных приложений
        "Data Scientist",  # Специалист по данным
        "Data Analyst",  # Аналитик данных
        "DevOps Engineer",  # Инженер DevOps
        "System Administrator",  # Системный администратор
        "Network Engineer",  # Сетевой инженер
        "Cybersecurity Specialist",  # Специалист по кибербезопасности
        "Database Administrator",  # Администратор баз данных
        "Cloud Engineer",  # Облачный инженер
        "Machine Learning Engineer",  # Инженер машинного обучения
        "AI Engineer",  # Инженер по искусственному интеллекту
        "Frontend Developer",  # Фронтенд-разработчик
        "Backend Developer",  # Бэкенд-разработчик
        "Full Stack Developer",  # Разработчик полного стека
        "IT Support Specialist",  # Специалист по IT-поддержке
        "IT Project Manager",  # Менеджер IT-проектов
        "QA Engineer",  # Инженер по качеству (тестировщик)
        "UX/UI Designer",  # UX/UI дизайнер
        "Scrum Master",  # Скрам-мастер
        "Product Manager",  # Менеджер продукта
        "IT Consultant",  # IT-консультант
        "Security Analyst",  # Аналитик безопасности
        "Technical Writer",  # Технический писатель
        "Business Analyst",  # Бизнес-аналитик
        "Blockchain Developer",  # Разработчик блокчейн
        "Embedded Systems Engineer",  # Инженер встраиваемых систем
        "Game Developer",  # Разработчик игр
        "IT Architect",  # IT-архитектор
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]

    for username in usernames:
        try:
            user = User.objects.create(username=username)
            user.set_unusable_password()  # разрешаем устанавливать плохой пасспорт
            user.set_password("1")  # всем юзерам ставим единицу в пароль
            user.profession = random.choice(it_professions)
            user.save()
            print(user)
        except Exception as e:
            print(e)

    return HttpResponse("test2")


# test2()
