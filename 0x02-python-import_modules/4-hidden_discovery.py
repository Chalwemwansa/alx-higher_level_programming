#!/usr/bin/pythin3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for each in names:
        if'__' not in each:
            print("{}".format(each))
