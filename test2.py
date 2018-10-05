#!flask/bin/python
import json

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}
tasks = {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    }

def main():
    print(tasks['title'])
    with open('data.txt', 'w') as f:
        json.dump(tasks, f)

if __name__ == '__main__':
    main()
