

import time

def log_execution(func):
    def wraps(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Running {func.__name__}. Executed in {end_time - start_time:.4f} seconds")
        return result

    return wraps

@log_execution
def multiflier():
    print(5 * 4)

multiflier()



