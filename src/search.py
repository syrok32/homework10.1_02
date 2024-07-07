import re
from collections import Counter
from typing import Any, Dict, List


def search_str(dict_list: List[Dict[Any, Any]], found_str: str) -> List[Dict[str, Any]]:
    """ищет слово в значениях """
    new_list = []
    pattern = re.compile(rf"{found_str}")
    for i in dict_list:
        for example in i.values():
            if not isinstance(example, str):
                example = str(example)
            if pattern.search(example):
                new_list.append(i)
    return new_list


def count_categories(oper: Any, dict_categories: Any) -> dict:
    """ищет категории"""
    new_list = []
    for dict_sing in oper:
        for key_oper, values_oper in dict_sing.items():
            for key_dict, values_dict in dict_categories.items():
                pattern = re.compile(rf"{values_dict}")
                if pattern.search(values_oper):
                    new_list.append(key_dict)

    counted = Counter(new_list)
    return dict(counted)


# oper = [{'1': "покупка молока"},
#          {'2': 'донат игра'},
#          {'3': 'перевод маме'},
#          {'4': 'перевод папе'}]
#
#
# categories = {'развлечение' : 'игра',
#               'переводы': 'перевод',
#               'товары': 'покупка'}
#
# print(count_categories(oper, categories))
#
# print(search_str(oper,'перевод'))
