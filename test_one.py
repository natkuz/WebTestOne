from login import get_post, create_post
import pytest

def test_step_one(login):
    res = get_post(login)
    res_lst = res.get('data')
    res_id_list = [item['id'] for item in res_lst]
    assert 83943 in res_id_list, "test_step_one не пройден"


def test_step_two(login):
    res = create_post(login)
    assert 'пост про котика-лапу' in res.get('description'), "test_step_two не пройден"


if __name__ == '__main__':
    pytest.main(['-vv'])
