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


zxc=collect_args()
zxc(130)
zxc(20)
zxc(130)
zxc(20)
zxc(130)
zxc(20)
print(zxc(10))
print(zxc(10))


