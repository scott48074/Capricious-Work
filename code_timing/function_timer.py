import time

def timer(function):
    def wrapper(*args):
        start = time.time()
        function(*args)
        stop = time.time()
        return stop - start
    return wrapper

@timer
def test():
    for x in range(1000000):
        i = 0

def main():
	print(test())

if __name__ == '__main__':
	main()
