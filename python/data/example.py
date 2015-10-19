#!/usr/bin
class Example(dict):
    def __getitem__(self):
        try:
            return dict.__getitem__(self, item)
        except:
            value = self[item] = type(self)()

if __name__ == "__main__":
    a = Example()
    a[1][2][3] = 4
    a[1][3][3] = 5
    a[1][2]['test'] = 6
    print a 
