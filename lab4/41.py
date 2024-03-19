def collect_args():
    args = []
    

    def wrapper(x):
        if x==10:
            a = args.copy()
            args.clear()
            return a
        args.append(x)
        return args 
    return wrapper


collect=collect_args()
collect(130)
collect(20)
collect(130)
collect(20)
collect(130)
collect(20)
print(collect(10))
print(collect(10))


