import time


class RenderTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        total_time = end_time - start_time
        print()
        print(f"Total time: {total_time:.6f} seconds")
        print()

        return response
