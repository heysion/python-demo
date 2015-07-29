import collections

if __name__ == "__main__":
    c = collections.Counter("abc")
    print c
    c.update("abcef")
    print c
    c.subtract("f")
    print c
