def increase(num):
    try:
        return int(num)+1
    except:
        raise ValueError("this is not good -- Nikhil")

a = increase("lksj24")
print(a)