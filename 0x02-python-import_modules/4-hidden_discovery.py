#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    def vdir(obj):
        juanito = [x for x in dir(obj) if not x.startswith('__')]
        for i in range(len(juanito)):
            print("{}".format(juanito[i]))
    vdir(hidden_4)
