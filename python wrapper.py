import time
def tictoc(func):
    def wrapper(*args,**kwargs):
        t1=time.time()
        value = func(*args,**kwargs)
        t2 = time.time()-t1
        print(f'Took {t2} seconds')
        return value
    return wrapper

@tictoc
def do_this(x):
    # Simulating running code...
    time.sleep(x + 1.3)
    return x*2.0

@tictoc
def do_that(x):
    # Simulating running code...
    time.sleep(x + .4)

x = do_this(9.9)
do_that(0)
print ('Done')
print(x)