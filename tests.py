import requests

def test_create():
    r = requests.post('https://hng-stage-2-ndiuel.vercel.app/api', json={'name': 'Samuel', 'age': 25, 'email': 'ndiuel@gmail.com'})

    data = r.json()
    assert data['name'] == 'Samuel'
    assert data['age'] == 25
    assert data['email'] == 'ndiuel@gmail.com'
    assert 'id' in data
    print("--------------Create Record Passed--------------")


def test_fetch_all():
    r = requests.get('https://hng-stage-2-ndiuel.vercel.app/api')

    data = r.json()[0]
    assert 'name' in data
    assert 'age' in data
    assert 'email' in data
    assert 'id' in data
    print("--------------Fetch Records Passed--------------")


def test_fetch():
    r = requests.get('https://hng-stage-2-ndiuel.vercel.app/api/Samuel')
    data = r.json()
    assert data['name'] == 'Samuel'

    r = requests.get(f'https://hng-stage-2-ndiuel.vercel.app/api/{data["id"]}')
    data = r.json()
    assert data['name'] == 'Samuel'
    print("--------------Fetch Single Record Passed--------------")


def test_update():
    body = {
        'age': 15,
        'email': 'ndi@gmail.com'
    }


    r = requests.patch('https://hng-stage-2-ndiuel.vercel.app/api/Samuel', json=body)
    data = r.json()
    assert data['age'] == 15
    assert data['email'] == 'ndi@gmail.com'
    print("--------------Update Record Passed--------------")


def test_delete():

    r = requests.delete('https://hng-stage-2-ndiuel.vercel.app/api/Samuel')
    data = r.json()
    assert data['message'].lower() == 'samuel has been deleted'
    print("--------------Delete Record Passed--------------")


if __name__ == '__main__':
    test_create()
    test_fetch_all()
    test_fetch()
    test_update()
    test_delete()