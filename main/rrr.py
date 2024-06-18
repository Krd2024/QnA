import random
from django.http import HttpResponse

from .models import Answer, Question, Rection, Subscription, Teg
from .models import User

import random
from datetime import datetime, timedelta


def test2(req):

    # ========================== Реакции ===========================================
    try:
        for i in range(1000):
            # user = User.objects.get(id=random.randrange(300, 1500))
            Answer.objects.filter(id=random.randrange(1500, 11573)).update(correct=True)
            # Rection.objects.create(user=user, answer=answers).save()
    except Exception as e:
        print(e)
        pass
    return HttpResponse("Ok")

    # создаем тонну комнат

    # programming_questions = [
    #     {
    #         "title": "What are the differences between Python 2 and Python 3?",
    #         "text": "Explain the major differences between Python 2 and Python 3 in terms of syntax, features, and compatibility.",
    #     },
    #     {
    #         "title": "How does a blockchain work?",
    #         "text": "Describe the fundamental concepts and principles behind blockchain technology, including its structure, consensus mechanisms, and use cases.",
    #     },
    #     {
    #         "title": "What are RESTful APIs?",
    #         "text": "Define what RESTful APIs are and explain their key principles, such as statelessness, uniform interface, and client-server architecture.",
    #     },
    #     {
    #         "title": "What is the difference between machine learning and deep learning?",
    #         "text": "Differentiate between machine learning and deep learning techniques, and discuss their applications, algorithms, and training processes.",
    #     },
    #     {
    #         "title": "Explain the concept of microservices architecture.",
    #         "text": "Discuss the principles and benefits of microservices architecture, including scalability, modularity, and independent deployment.",
    #     },
    #     {
    #         "title": "What is Docker and how does it work?",
    #         "text": "Provide an overview of Docker containerization technology and explain its components, such as Docker Engine, images, and containers.",
    #     },
    #     {
    #         "title": "What are design patterns in software engineering?",
    #         "text": "Describe the concept of design patterns and provide examples of commonly used design patterns in software development.",
    #     },
    #     {
    #         "title": "How do you handle errors and exceptions in Python?",
    #         "text": "Explain error handling techniques in Python, including try-except blocks, raising exceptions, and handling specific types of errors.",
    #     },
    #     {
    #         "title": "What is the difference between a list and a tuple in Python?",
    #         "text": "Differentiate between lists and tuples in Python based on their mutability, syntax, and typical use cases.",
    #     },
    #     {
    #         "title": "What are the advantages of using version control systems?",
    #         "text": "Discuss the benefits of version control systems, such as Git, in software development projects, including collaboration, history tracking, and code management.",
    #     },
    #     {
    #         "title": "What is the difference between SQL and NoSQL databases?",
    #         "text": "Compare and contrast SQL and NoSQL databases in terms of data model, scalability, consistency, and use cases.",
    #     },
    #     {
    #         "title": "Explain the concept of recursion in programming.",
    #         "text": "Define recursion and discuss its implementation in programming languages, including base case, recursive case, and stack usage.",
    #     },
    #     {
    #         "title": "How does a binary search algorithm work?",
    #         "text": "Describe the binary search algorithm and its implementation, including the iterative and recursive approaches, time complexity, and use cases.",
    #     },
    #     {
    #         "title": "What are the SOLID principles in object-oriented design?",
    #         "text": "Discuss the five SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) and their importance in object-oriented design.",
    #     },
    #     {
    #         "title": "What is the difference between synchronous and asynchronous programming?",
    #         "text": "Compare synchronous and asynchronous programming paradigms, including execution flow, blocking, and non-blocking operations.",
    #     },
    #     {
    #         "title": "What are the advantages of using a framework for web development?",
    #         "text": "Discuss the benefits of using web development frameworks, such as code reuse, productivity, and community support.",
    #     },
    #     {
    #         "title": "What are the benefits of unit testing?",
    #         "text": "Discuss the advantages of unit testing, including early bug detection, improved code quality, and regression prevention.",
    #     },
    #     {
    #         "title": "How does garbage collection work in programming languages?",
    #         "text": "Describe the concept of garbage collection and its implementation in programming languages, including reference counting, mark-and-sweep, and generational garbage collection.",
    #     },
    #     {
    #         "title": "How do you handle concurrency in programming?",
    #         "text": "Discuss concurrency concepts and techniques, such as threading, multiprocessing, asynchronous programming, and thread synchronization.",
    #     },
    #     {
    #         "title": "What is the importance of code documentation?",
    #         "text": "Explain the significance of code documentation in software development, including readability, maintainability, and collaboration.",
    #     },
    #     {
    #         "title": "What are design trade-offs in software engineering?",
    #         "text": "Discuss the concept of design trade-offs and how they influence software design decisions, including performance vs. scalability, flexibility vs. simplicity, and consistency vs. availability.",
    #     },
    #     {
    #         "title": "How do you stay updated with the latest programming trends and technologies?",
    #         "text": "Share strategies for staying informed about new programming trends, technologies, and best practices, including reading blogs, attending conferences, and participating in online communities.",
    #     },
    #     {
    #         "title": "How do you handle sessions and cookies in web development?",
    #         "text": "Explain the concepts of sessions and cookies in web development, including their use cases, implementation, and security considerations.",
    #     },
    #     {
    #         "title": "What is the difference between a router and a switch?",
    #         "text": "Differentiate between routers and switches in computer networking, including their functions, operating layers, and typical deployments.",
    #     },
    #     {
    #         "title": "How do you deploy a web application to a production server?",
    #         "text": "Discuss the steps and best practices for deploying a web application to a production server, including environment setup, version control integration, and monitoring.",
    #     },
    #     {
    #         "title": "What are the principles of responsive web design?",
    #         "text": "Explain the principles of responsive web design, including fluid grids, flexible images, and media queries, and discuss their importance in creating user-friendly interfaces across devices.",
    #     },
    #     {
    #         "title": "What are the benefits of using a virtual private network (VPN)?",
    #         "text": "Discuss the advantages of using a virtual private network (VPN) for secure remote access, data encryption, and privacy protection.",
    #     },
    #     {
    #         "title": "How does an operating system manage processes and memory?",
    #         "text": "Describe the mechanisms and algorithms used by operating systems to manage processes, memory allocation, and scheduling, and discuss their impact on system performance and reliability.",
    #     },
    #     {
    #         "title": "What are the different types of software testing?",
    #         "text": "Discuss various types of software testing, such as unit testing, integration testing, system testing, and acceptance testing, and explain their objectives and methods.",
    #     },
    #     {
    #         "title": "How do you handle user authentication and authorization in web applications?",
    #         "text": "Explain the concepts of user authentication and authorization in web applications, including techniques such as password hashing, session management, and role-based access control (RBAC).",
    #     },
    #     {
    #         "title": "What are the advantages of using a content delivery network (CDN)?",
    #         "text": "Discuss the benefits of using a content delivery network (CDN) for improving website performance, scalability, and global reach by caching content closer to users.",
    #     },
    #     {
    #         "title": "How do you handle file uploads in web applications?",
    #         "text": "Explain the process of handling file uploads in web applications, including server-side and client-side validation, storage options, and security considerations.",
    #     },
    #     {
    #         "title": "What is the difference between functional and object-oriented programming?",
    #         "text": "Differentiate between functional and object-oriented programming paradigms, including their approaches to state, behavior, and composition.",
    #     },
    #     {
    #         "title": "How do you handle errors and exceptions in JavaScript?",
    #         "text": "Explain error handling techniques in JavaScript, including try-catch blocks, throwing exceptions, and handling asynchronous errors.",
    #     },
    #     {
    #         "title": "What are the advantages of using a NoSQL database?",
    #         "text": "Discuss the benefits of using a NoSQL database, such as flexibility, scalability, and performance, and explain its suitability for various use cases, such as real-time analytics and content management.",
    #     },
    #     {
    #         "title": "What is the difference between imperative and declarative programming?",
    #         "text": "Compare and contrast imperative and declarative programming paradigms, including their approaches to defining logic, side effects, and abstraction.",
    #     },
    #     {
    #         "title": "How do you implement pagination in web applications?",
    #         "text": "Explain the concept of pagination in web applications, including techniques for retrieving and displaying data in manageable chunks, and discuss its benefits for performance and user experience.",
    #     },
    #     {
    #         "title": "What are the principles of user-centered design (UCD)?",
    #         "text": "Explain the principles of user-centered design (UCD), including user research, usability testing, and iterative design, and discuss their importance in creating intuitive and user-friendly interfaces.",
    #     },
    #     {
    #         "title": "How do you scale a web application to handle increased traffic?",
    #         "text": "Discuss strategies for scaling a web application to handle increased traffic, including horizontal and vertical scaling, load balancing, and caching.",
    #     },
    #     {
    #         "title": "What is the difference between a stack and a queue?",
    #         "text": "Differentiate between stacks and queues in data structures, including their operations, usage patterns, and real-world analogies.",
    #     },
    #     {
    #         "title": "What is the role of a backend developer?",
    #         "text": "Describe the responsibilities and skills of a backend developer, including server-side scripting, database management, and API development.",
    #     },
    #     {
    #         "title": "How do you handle cross-site scripting (XSS) attacks?",
    #         "text": "Explain techniques for preventing and mitigating cross-site scripting (XSS) attacks in web applications, including input validation, output encoding, and content security policies (CSP).",
    #     },
    #     {
    #         "title": "What are the principles of object-oriented programming (OOP)?",
    #         "text": "Explain the principles of object-oriented programming (OOP), including encapsulation, inheritance, polymorphism, and abstraction, and discuss their importance in software design and development.",
    #     },
    #     {
    #         "title": "How do you implement authentication using JSON Web Tokens (JWT)?",
    #         "text": "Describe the process of implementing authentication using JSON Web Tokens (JWT), including token generation, verification, and usage in web applications.",
    #     },
    #     {
    #         "title": "What is the role of a quality assurance (QA) engineer?",
    #         "text": "Describe the responsibilities and tasks of a quality assurance (QA) engineer, including test planning, execution, and reporting, and discuss their importance in ensuring software quality.",
    #     },
    #     {
    #         "title": "What is the difference between HTTP GET and POST methods?",
    #         "text": "Differentiate between HTTP GET and POST methods in web development, including their purposes, usage scenarios, and data transmission mechanisms.",
    #     },
    #     {
    #         "title": "How do you implement rate limiting in web APIs?",
    #         "text": "Discuss strategies for implementing rate limiting in web APIs, including token bucket algorithm, sliding window algorithm, and usage quotas.",
    #     },
    #     {
    #         "title": "How do you handle database transactions in web applications?",
    #         "text": "Discuss techniques for managing database transactions in web applications, including transaction isolation levels, ACID properties, and error handling.",
    #     },
    #     {
    #         "title": "What is the role of a product manager in software development?",
    #         "text": "Describe the responsibilities and tasks of a product manager in software development, including product planning, roadmap development, and stakeholder communication.",
    #     },
    #     {
    #         "title": "What is the difference between a mutex and a semaphore?",
    #         "text": "Differentiate between mutexes and semaphores in concurrent programming, including their usage, synchronization mechanisms, and applications.",
    #     },
    #     {
    #         "title": "What is the difference between encryption and hashing?",
    #         "text": "Explain the distinctions between encryption and hashing techniques, including their purposes, algorithms, and security properties.",
    #     },
    #     {
    #         "title": "What is the role of a frontend developer?",
    #         "text": "Describe the responsibilities and skills of a frontend developer, including UI design, client-side scripting, and browser compatibility.",
    #     },
    #     {
    #         "title": "How do you implement data validation in web forms?",
    #         "text": "Discuss techniques for implementing data validation in web forms, including client-side and server-side validation, input sanitization, and error handling.",
    #     },
    #     {
    #         "title": "What is the CAP theorem?",
    #         "text": "Define the CAP theorem (Consistency, Availability, Partition Tolerance) and discuss its implications for distributed systems and database design.",
    #     },
    #     {
    #         "title": "Explain the concept of cloud computing.",
    #         "text": "Define cloud computing and discuss its key characteristics, deployment models (public, private, hybrid), and service models (IaaS, PaaS, SaaS).",
    #     },
    #     {
    #         "title": "What is the difference between procedural and object-oriented programming?",
    #         "text": "Compare and contrast procedural and object-oriented programming paradigms, including their approaches to data abstraction, encapsulation, and inheritance.",
    #     },
    #     {
    #         "title": "How do you handle asynchronous operations in JavaScript?",
    #         "text": "Explain asynchronous programming techniques in JavaScript, including callbacks, promises, and async/await syntax.",
    #     },
    #     {
    #         "title": "What are the advantages of using a document-oriented database?",
    #         "text": "Discuss the benefits of using a document-oriented database, such as schema flexibility, scalability, and ease of data modeling.",
    #     },
    #     {
    #         "title": "What is functional programming?",
    #         "text": "Define functional programming paradigm and discuss its key concepts, such as pure functions, higher-order functions, and immutability.",
    #     },
    #     {
    #         "title": "How do you implement authentication and authorization in a RESTful API?",
    #         "text": "Describe approaches for implementing authentication and authorization mechanisms in a RESTful API, such as token-based authentication and role-based access control (RBAC).",
    #     },
    #     {
    #         "title": "What is the difference between GraphQL and REST APIs?",
    #         "text": "Compare and contrast GraphQL and REST APIs in terms of data querying, schema flexibility, and client-server interactions.",
    #     },
    #     {
    #         "title": "How do you design a database schema for a relational database?",
    #         "text": "Discuss principles and best practices for designing a database schema, including normalization, denormalization, and indexing.",
    #     },
    #     {
    #         "title": "What is functional testing?",
    #         "text": "Explain functional testing methodology and its role in software quality assurance, including test scenarios, data preparation, and automation.",
    #     },
    #     {
    #         "title": "How do you optimize SQL queries for performance?",
    #         "text": "Discuss strategies for optimizing SQL queries, including index optimization, query caching, and query execution plan analysis.",
    #     },
    #     {
    #         "title": "What is the role of a DevOps engineer?",
    #         "text": "Describe the responsibilities and tasks of a DevOps engineer, including continuous integration, continuous delivery, and infrastructure automation.",
    #     },
    #     {
    #         "title": "What are the principles of RESTful API design?",
    #         "text": "Explain principles of RESTful API design, such as resource identification, statelessness, and uniform interface, and discuss their importance in creating scalable and maintainable APIs.",
    #     },
    #     {
    #         "title": "How do you handle data validation and sanitization in web applications?",
    #         "text": "Discuss techniques for validating and sanitizing user input in web applications, including client-side validation, server-side validation, and input filtering.",
    #     },
    #     {
    #         "title": "What is the difference between unit testing and integration testing?",
    #         "text": "Differentiate between unit testing and integration testing in software testing, including their scope, purpose, and testing environments.",
    #     },
    #     {
    #         "title": "How do you implement continuous integration and continuous deployment (CI/CD)?",
    #         "text": "Describe the process of implementing continuous integration and continuous deployment (CI/CD) pipelines, including automated testing, build automation, and deployment automation.",
    #     },
    #     {
    #         "title": "What is the role of a data scientist?",
    #         "text": "Describe the responsibilities and skills of a data scientist, including data analysis, machine learning, and statistical modeling.",
    #     },
    #     {
    #         "title": "How do you handle file uploads in web applications securely?",
    #         "text": "Discuss security considerations for handling file uploads in web applications, including file type validation, file size restrictions, and storage security.",
    #     },
    #     {
    #         "title": "What is the difference between functional and non-functional requirements?",
    #         "text": "Differentiate between functional and non-functional requirements in software development, including their definitions, examples, and prioritization.",
    #     },
    #     {
    #         "title": "What are the principles of agile software development?",
    #         "text": "Explain principles of agile software development, such as iterative development, customer collaboration, and responding to change, and discuss their importance in delivering high-quality software.",
    #     },
    #     {
    #         "title": "How do you handle errors and exceptions in Java?",
    #         "text": "Explain error handling techniques in Java, including try-catch blocks, throwing exceptions, and checked vs. unchecked exceptions.",
    #     },
    #     {
    #         "title": "What is the difference between a primary key and a foreign key in a database?",
    #         "text": "Differentiate between primary keys and foreign keys in a database, including their roles, constraints, and relationships.",
    #     },
    #     {
    #         "title": "How do you design a RESTful API?",
    #         "text": "Discuss steps and best practices for designing a RESTful API, including resource identification, endpoint naming conventions, and response formats.",
    #     },
    #     {
    #         "title": "What is the role of a data engineer?",
    #         "text": "Describe the responsibilities and skills of a data engineer, including data modeling, ETL (extract, transform, load) processes, and data pipeline management.",
    #     },
    #     {
    #         "title": "How do you handle authentication and authorization in a microservices architecture?",
    #         "text": "Discuss approaches for implementing authentication and authorization mechanisms in a microservices architecture, such as OAuth 2.0, JWT tokens, and API gateways.",
    #     },
    #     {
    #         "title": "What is the difference between server-side rendering and client-side rendering?",
    #         "text": "Differentiate between server-side rendering and client-side rendering in web development, including their architectures, performance considerations, and SEO implications.",
    #     },
    #     {
    #         "title": "How do you handle input/output operations in Python?",
    #         "text": "Explain techniques for handling input/output operations in Python, including file handling, standard input/output streams, and serialization.",
    #     },
    #     {
    #         "title": "What are the benefits of using a container orchestration platform like Kubernetes?",
    #         "text": "Discuss the advantages of using a container orchestration platform like Kubernetes for managing containerized applications, including scalability, fault tolerance, and resource optimization.",
    #     },
    #     {
    #         "title": "What is the role of a systems administrator?",
    #         "text": "Describe the responsibilities and tasks of a systems administrator, including server provisioning, configuration management, and system monitoring.",
    #     },
    #     {
    #         "title": "How do you handle version control in software development?",
    #         "text": "Discuss strategies and best practices for version control in software development, including branching models, merge strategies, and release management.",
    #     },
    #     {
    #         "title": "What is the difference between a process and a thread?",
    #         "text": "Explain the distinctions between processes and threads in operating systems, including memory usage, context switching, and concurrency.",
    #     },
    #     {
    #         "title": "How do you handle exceptions in Python?",
    #         "text": "Discuss exception handling techniques in Python, including try-except blocks, exception hierarchy, and best practices for error handling.",
    #     },
    #     {
    #         "title": "What are the advantages of using a relational database?",
    #         "text": "Discuss the benefits of using a relational database, such as data integrity, ACID properties, and support for complex queries.",
    #     },
    #     {
    #         "title": "How do you implement caching in web applications?",
    #         "text": "Explain caching strategies in web applications, including client-side caching, server-side caching, and CDN caching.",
    #     },
    #     {
    #         "title": "What is the difference between compile-time and runtime?",
    #         "text": "Differentiate between compile-time and runtime in software development, including when errors are detected and how code is executed.",
    #     },
    #     {
    #         "title": "How do you handle memory management in C++?",
    #         "text": "Discuss memory management techniques in C++, including dynamic memory allocation, pointers, and smart pointers.",
    #     },
    #     {
    #         "title": "What is the role of a software tester?",
    #         "text": "Describe the responsibilities and tasks of a software tester, including test planning, test case design, and defect reporting.",
    #     },
    #     {
    #         "title": "How do you implement pagination in SQL queries?",
    #         "text": "Explain techniques for implementing pagination in SQL queries, including LIMIT-OFFSET, ROW_NUMBER(), and cursor-based pagination.",
    #     },
    #     {
    #         "title": "What is the difference between a library and a framework?",
    #         "text": "Differentiate between libraries and frameworks in software development, including their roles, architecture, and flexibility.",
    #     },
    #     {
    #         "title": "How do you handle concurrency in Java?",
    #         "text": "Discuss concurrency control mechanisms in Java, including synchronization, locks, and concurrent data structures.",
    #     },
    #     {
    #         "title": "What are the principles of object-oriented design (OOD)?",
    #         "text": "Explain principles of object-oriented design (OOD), such as encapsulation, inheritance, and polymorphism, and discuss their importance in creating reusable and maintainable software.",
    #     },
    #     {
    #         "title": "How do you implement authentication in web applications?",
    #         "text": "Discuss techniques for implementing authentication in web applications, including session-based authentication, token-based authentication, and OAuth.",
    #     },
    #     {
    #         "title": "What is the difference between TCP and UDP?",
    #         "text": "Differentiate between TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) in computer networking, including reliability, connection-oriented vs. connectionless, and use cases.",
    #     },
    #     {
    #         "title": "How do you optimize database queries for performance?",
    #         "text": "Discuss strategies for optimizing database queries, including index optimization, query optimization, and denormalization.",
    #     },
    #     {
    #         "title": "What is the role of a software architect?",
    #         "text": "Describe the responsibilities and skills of a software architect, including system design, technical leadership, and decision-making.",
    #     },
    #     {
    #         "title": "How do you handle file input/output in Java?",
    #         "text": "Explain file input/output operations in Java, including file handling, stream-based I/O, and NIO (New I/O) API.",
    #     },
    #     {
    #         "title": "What are the principles of good software design?",
    #         "text": "Explain the principles of good software design, such as modularity, cohesion, and separation of concerns, and discuss their importance in creating maintainable and scalable software systems.",
    #     },
    #     {
    #         "title": "How do you prevent SQL injection attacks?",
    #         "text": "Discuss techniques for preventing SQL injection attacks, such as parameterized queries, input validation, and ORM (Object-Relational Mapping) frameworks.",
    #     },
    #     {
    #         "title": "What is the role of a database administrator (DBA)?",
    #         "text": "Describe the responsibilities and tasks of a database administrator (DBA), including database management, performance tuning, and security enforcement.",
    #     },
    #     {
    #         "title": "How do you handle session management in web applications?",
    #         "text": "Explain techniques for managing user sessions in web applications, including session cookies, server-side session storage, and session hijacking prevention.",
    #     },
    #     {
    #         "title": "What is the difference between HTTP and HTTPS?",
    #         "text": "Explain the distinctions between HTTP and HTTPS protocols, including security features, encryption, and use cases.",
    #     },
    #     {
    #         "title": "How do you optimize website performance?",
    #         "text": "Discuss strategies for optimizing website performance, including minimizing HTTP requests, optimizing images, caching, and using CDNs.",
    #     },
    #     {
    #         "title": "What is the difference between static and dynamic typing?",
    #         "text": "Differentiate between static and dynamic typing in programming languages, including advantages, disadvantages, and examples of languages that use each approach.",
    #     },
    #     {
    #         "title": "What is RESTful architecture?",
    #         "text": "Define RESTful architecture and discuss its key principles, such as statelessness, uniform interface, and resource-based interaction.",
    #     },
    #     {
    #         "title": "How do you handle concurrent programming in Python?",
    #         "text": "Discuss concurrency control mechanisms in Python, including threading, multiprocessing, and asynchronous programming with asyncio.",
    #     },
    #     {
    #         "title": "What is the role of a software engineer?",
    #         "text": "Describe the responsibilities and tasks of a software engineer, including software design, coding, testing, and maintenance.",
    #     },
    #     {
    #         "title": "How do you design a relational database schema?",
    #         "text": "Discuss principles and best practices for designing a relational database schema, including normalization, denormalization, and entity-relationship modeling.",
    #     },
    #     {
    #         "title": "What is the difference between a primary key and a foreign key?",
    #         "text": "Differentiate between primary keys and foreign keys in a database, including their roles, constraints, and relationships.",
    #     },
    # ]

    # topics = [
    #     "Python",
    #     "C++",
    #     "Java",
    #     "JavaScript",
    #     "Ruby",
    #     "Python",
    #     "JavaScript",
    #     "Java",
    #     "C++",
    #     "C#",
    #     "Ruby",
    #     "Go",
    #     "Swift",
    #     "Kotlin",
    #     "PHP",
    #     "TypeScript",
    #     "R",
    #     "Objective-C",
    #     "Scala",
    #     "Rust",
    # ]

    # ============================= Создать подписку на тег =======================================
    # def test2(request):
    #     subsc = Subscription.objects.all()
    #     tags = Teg.objects.all()
    #     users = User.objects.all()

    #     for user in users:
    #         try:
    #             subsc = Subscription.objects.create(tag=random.choice(tags), user=user)
    #             # print(subsc)
    #             subsc.save()
    #         except Exception as e:
    #             # print(e)
    #             continue
    #     return HttpResponse("OK")

    #     # ======================= Создать вопросы ==========================================
    # from django.db.models import Count

    # topics = Teg.objects.all()
    # # users = User.objects.all()
    # users = User.objects.annotate(question_count=Count("question_set")).filter(
    #     question_count=0
    # )

    # # users = User.objects.exclude(username="Den")
    # # for u in users:
    # #     print(u.username)
    # for q in programming_questions:

    #     try:
    #         today = datetime.now()
    #         random_days = random.randint(
    #             0, 700
    #         )  # Randomly select days within one month
    #         random_timedelta = timedelta(hours=random_days)
    #         date = today - random_timedelta

    #         random_days = random.randint(
    #             0, random_days
    #         )  # Randomly select days within one month
    #         random_timedelta = timedelta(hours=random_days)
    #         upd = date + random_timedelta

    #         # date случайная дата от сегодня до месяца назад
    #         # upd случайная дата от сегодня до date

    #         quest = Question.objects.create(
    #             autor=random.choice(users),
    #             title=q["title"],
    #             text=q["text"],
    #             tegs=random.choice(topics),
    #         )

    #         # print(random.choice(topics))
    #         quest.save()
    #         # из за auto_now_add и auto_now которые не сами устанавливают дату при сохранинии,  приходится устанавливать дату отдельно через update
    #         Question.objects.filter(id=quest.id).update(created_at=date, updated_at=upd)
    #     except Exception as e:
    #         # print(e)
    #         pass
    # return HttpResponse("test2")

    #     # ===================== Создать ответы ===================================================

    # answers = [
    #     "Python — это интерпретируемый язык программирования высокого уровня, используемый для разработки веб-приложений и анализа данных.",
    #     "JavaScript — это язык программирования, используемый для создания интерактивных элементов на веб-страницах, таких как кнопки и формы.",
    #     "Java — это объектно-ориентированный язык программирования, широко используемый для разработки корпоративных приложений и Android-приложений.",
    #     "C++ — это расширение языка программирования C, которое поддерживает объектно-ориентированное программирование и используется для разработки системного ПО и игр.",
    #     "C# — это язык программирования, разработанный Microsoft, используемый для создания приложений на платформе .NET.",
    #     "Ruby — это язык программирования с динамической типизацией, известный своей простотой и элегантностью, часто используется для веб-разработки с Ruby on Rails.",
    #     "Go, также известный как Golang, — это компилируемый язык программирования, созданный Google, известный своей простотой и эффективностью.",
    #     "Swift — это язык программирования, разработанный Apple для создания приложений для iOS и macOS.",
    #     "Kotlin — это язык программирования, разработанный JetBrains, полностью совместимый с Java и используемый для разработки Android-приложений.",
    #     "PHP — это серверный язык программирования, используемый для создания динамических веб-страниц и веб-приложений.",
    #     "TypeScript — это язык программирования, являющийся надстройкой над JavaScript, добавляющий статическую типизацию и другие возможности.",
    #     "R — это язык программирования и среды для статистических вычислений и визуализации данных, широко используемый в научных исследованиях.",
    #     "Objective-C — это объектно-ориентированный язык программирования, используемый для разработки приложений под macOS и iOS до появления Swift.",
    #     "Scala — это язык программирования, который сочетает в себе функции объектно-ориентированного и функционального программирования, используется для разработки высоконагруженных приложений.",
    #     "Rust — это системный язык программирования, разработанный Mozilla, который обеспечивает безопасность памяти и высокую производительность.",
    #     "SQL — это язык запросов, используемый для управления и манипулирования данными в реляционных базах данных.",
    #     "Perl — это язык программирования, известный своей мощью в обработке текста и веб-разработке, особенно в области системного администрирования.",
    #     "Lua — это легковесный, встраиваемый скриптовый язык программирования, часто используемый для разработки игр.",
    #     "Haskell — это функциональный язык программирования с сильной статической типизацией, известный своей мощной системой типов.",
    #     "MATLAB — это язык программирования и среда для численных вычислений и визуализации данных, широко используемый в инженерии и науке.",
    #     "Dart — это язык программирования, разработанный Google, используемый для создания кроссплатформенных мобильных и веб-приложений с Flutter.",
    #     "Elixir — это функциональный язык программирования, построенный на базе Erlang, используемый для разработки масштабируемых и поддерживаемых приложений.",
    #     "F# — это функциональный язык программирования, который работает на платформе .NET и используется для разработки приложений с высокой производительностью.",
    #     "Julia — это высокоуровневый язык программирования, разработанный для высокопроизводительных численных и научных вычислений.",
    #     "Shell — это язык сценариев командной оболочки, используемый для автоматизации задач в Unix-подобных операционных системах.",
    #     "Ada — это структурированный язык программирования, разработанный для обеспечения надежности и безопасности в критически важных системах.",
    #     "Prolog — это логический язык программирования, используемый в искусственном интеллекте и обработке естественного языка.",
    #     "Lisp — это семейство функциональных языков программирования, известное своей мощной макросистемой и использованием списков.",
    #     "Scheme — это диалект Lisp, известный своей минималистичностью и поддержкой функционального программирования.",
    #     "Clojure — это современный диалект Lisp, работающий на JVM, используемый для разработки многопоточных приложений.",
    #     "Erlang — это функциональный язык программирования, разработанный для разработки масштабируемых и отказоустойчивых систем.",
    #     "COBOL — это старый, но все еще используемый язык программирования, предназначенный для бизнес-приложений и финансовых систем.",
    #     "Fortran — это язык программирования, используемый в научных вычислениях и инженерных приложениях, особенно в области численного моделирования.",
    #     "RPG — это язык программирования, используемый в коммерческих приложениях на мэйнфреймах IBM.",
    #     "Smalltalk — это объектно-ориентированный язык программирования, известный своей простотой и чистотой синтаксиса.",
    #     "Bash — это язык командной оболочки, используемый для написания скриптов и автоматизации задач в Unix-подобных системах.",
    #     "PowerShell — это язык сценариев и инструмент командной строки от Microsoft, используемый для управления и автоматизации задач в Windows.",
    #     "VHDL — это язык описания аппаратуры, используемый для моделирования и разработки цифровых систем.",
    #     "Verilog — это язык описания аппаратуры, широко используемый в разработке и верификации цифровых интегральных схем.",
    #     "AWK — это язык программирования для обработки текстовых данных, часто используемый в системном администрировании и анализе данных.",
    #     "Tcl — это интерпретируемый язык программирования, известный своей простотой и встраиваемостью в другие приложения.",
    #     "Scratch — это визуальный язык программирования, разработанный для обучения детей основам программирования.",
    #     "Forth — это стековый язык программирования, используемый в встраиваемых системах и реального времени.",
    #     "Logo — это язык программирования, разработанный для обучения детей, известный своим использованием черепаховой графики.",
    #     "Nim — это статически типизированный компилируемый язык программирования, известный своей эффективностью и экспрессивностью.",
    #     "Crystal — это компилируемый язык программирования, синтаксически похожий на Ruby, но обеспечивающий высокую производительность.",
    #     "OCaml — это функциональный язык программирования, известный своей мощной системой типов и эффективностью.",
    #     "D — это системный язык программирования, сочетающий производительность C и C++ с безопасностью и удобством более высокоуровневых языков.",
    #     "Solidity — это язык программирования, используемый для разработки смарт-контрактов на платформе блокчейна Ethereum.",
    # ]

    # questions = Question.objects.all()
    # for i in range(1):
    #     for i in questions:
    #         autor = User.objects.get(id=random.randint(100, 1629))
    #         autor_1 = User.objects.get(id=random.randint(100, 1629))

    #         try:
    #             q_list = Question.objects.filter(autor=autor_1)
    #             ans = Answer.objects.create(
    #                 autor=autor,
    #                 question=random.choice(q_list),
    #                 text=random.choice(answers),
    #                 correct=False,
    #             )

    #             today = datetime.now()
    #             random_days = random.randint(0, 700)
    #             random_timedelta = timedelta(hours=random_days)
    #             date = today - random_timedelta

    #             random_days = random.randint(0, random_days)
    #             random_timedelta = timedelta(hours=random_days)
    #             upd = date + random_timedelta

    #             Answer.objects.filter(id=ans.id).update(created_at=date, updated_at=upd)
    #         except Exception as e:
    #             print(e)
    #             continue
    # return HttpResponse("test1")


#     # =========================================================================================


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
#         "playful_bunny",
#         "breezy_wind",
#         "soothing_waves",
#         "delightful_bird",
#         "grateful_tree",
#         "optimistic_star",
#         "radiant_moon",
#         "lovely_cloud",
#         "serene_river",
#         "gentle_whisper",
#         "kindhearted_fawn",
#         "tranquil_meadow",
#         "harmonious_song",
#         "serendipity_smile",
#         "cozy_blanket",
#         "giggling_squirrel",
#         "merry_garden",
#         "friendly_glow",
#         "compassionate_heart",
#         "whimsical_rain",
#         "sparkling_eyes",
#         "magical_spark",
#         "blissful_sunset",
#         "tender_leaf",
#         "chirpy_robin",
#         "dancing_buttercup",
#         "dreamy_wish",
#         "graceful_breeze",
#         "serenity_garden",
#         "happiness_hummingbird",
#         "mellow_melody",
#         "harmony_hug",
#         "lively_ladybug",
#         "radiant_breeze",
#         "smiling_sunflower",
#     ]
#     it_professions = [
#         "Software Developer",  # Разработчик программного обеспечения
#         "Web Developer",  # Веб-разработчик
#         "Mobile App Developer",  # Разработчик мобильных приложений
#         "Data Scientist",  # Специалист по данным
#         "Data Analyst",  # Аналитик данных
#         "DevOps Engineer",  # Инженер DevOps
#         "System Administrator",  # Системный администратор
#         "Network Engineer",  # Сетевой инженер
#         "Cybersecurity Specialist",  # Специалист по кибербезопасности
#         "Database Administrator",  # Администратор баз данных
#         "Cloud Engineer",  # Облачный инженер
#         "Machine Learning Engineer",  # Инженер машинного обучения
#         "AI Engineer",  # Инженер по искусственному интеллекту
#         "Frontend Developer",  # Фронтенд-разработчик
#         "Backend Developer",  # Бэкенд-разработчик
#         "Full Stack Developer",  # Разработчик полного стека
#         "IT Support Specialist",  # Специалист по IT-поддержке
#         "IT Project Manager",  # Менеджер IT-проектов
#         "QA Engineer",  # Инженер по качеству (тестировщик)
#         "UX/UI Designer",  # UX/UI дизайнер
#         "Scrum Master",  # Скрам-мастер
#         "Product Manager",  # Менеджер продукта
#         "IT Consultant",  # IT-консультант
#         "Security Analyst",  # Аналитик безопасности
#         "Technical Writer",  # Технический писатель
#         "Business Analyst",  # Бизнес-аналитик
#         "Blockchain Developer",  # Разработчик блокчейн
#         "Embedded Systems Engineer",  # Инженер встраиваемых систем
#         "Game Developer",  # Разработчик игр
#         "IT Architect",  # IT-архитектор
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#         "",
#     ]
#     for i in range(20):
#         for username in usernames:
#             try:
#                 # rand = random.randint(1000)
#                 user = User.objects.create(
#                     username=f"{username}{random.randint(0,1000)}"
#                 )
#                 user.set_unusable_password()  # разрешаем устанавливать плохой пасспорт
#                 user.set_password("1")  # всем юзерам ставим единицу в пароль
#                 user.profession = random.choice(it_professions)
#                 user.save()
#                 # print(user)
#             except Exception as e:
#                 # print(e)
#                 continue

#     return HttpResponse("test2")


# test2()
