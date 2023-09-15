import requests

def test_create():
    r = requests.post('http://localhost:3000/api', json={'name': 'Samuel', 'age': 25, 'email': 'ndiuel@gmail.com'})

    data = r.json()
    assert data['name'] == 'Samue'
    assert data['age'] == 25
    assert data['email'] == 'ndiuel@gmail.com'
    assert 'id' in data


def test_fetch_all():
    r = requests.get('http://localhost:3000/api')

    data = r.json()[0]
    assert 'name' in data
    assert 'age' in data
    assert 'email' in data
    assert 'id' in data


def test_fetch():
    r = requests.get('http://localhost:3000/api/Samuel')
    data = r.json()
    assert data['name'] == 'Samuel'

    r = requests.get(f'http://localhost:3000/api/{data["id"]}')
    data = r.json()
    assert data['name'] == 'Samuel'


def test_update():
    body = {
        'age': 15,
        'email': 'ndi@gmail.com'
    }


    r = requests.patch('http://localhost:3000/api/Samuel', json=body)
    data = r.json()
    assert data['age'] == 15
    assert data['email'] == 'ndi@gmail.com'


def test_delete():

    r = requests.delete('http://localhost:3000/api/Samuel')
    data = r.json()
    assert data['message'].lower() == 'samuel has been deleted'


if __name__ == '__main__':
    test_create()
    test_fetch_all()
    test_fetch()
    test_update()
    test_delete()