import re


def validate_values(params):
    """
    Validation of values
    :param params:
    :return dict:
    """
    id_person = check_id_person(params.get('id', None))
    get_sum = params.get('get_sum', None)
    add_sum = abs(int(get_sum)) if (get_sum is not None and get_sum.isdigit()) else None
    if None not in (id_person, add_sum):
        return dict(id_person=id_person, sum=add_sum)
    else:
        raise ValueError('Invalid parameters received')


def check_id_person(id_person):
    """
    Validate id person
    :param id_person:
    :return id_person:
    """
    id_view = re.compile(r'[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}')
    id_person = id_person if (id_person is not None and bool(id_view.match(id_person))) else None
    return id_person
