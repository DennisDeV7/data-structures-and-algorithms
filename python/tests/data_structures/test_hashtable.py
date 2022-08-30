import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

def test_get_returns_none_for_missing_key():
    table = Hashtable()
    actual = table.get("spam")
    expected = None
    assert actual == expected

def test_bucket_size():
    table = Hashtable()
    actual = len(table.buckets)
    expected = 1024
    assert actual == expected

def test_hash_in_range():
    table = Hashtable(size=2)
    keys = ["spam", "eggs", "bacon", "toast"]
    for key in keys:
        index = table.hash(key)
        assert 0 <= index <= table.size

def test_set():
    table = Hashtable()
    table.set("eggs", "bacon")
    assert True

def test_contains():
    table = Hashtable()
    table.set("eggs", "bacon")
    actual = table.contains("eggs")
    expected = True
    assert actual == expected

def test_not_contains():
    table = Hashtable()
    table.set("eggs", "bacon")
    actual = table.contains("spam")
    expected = False
    assert actual == expected

def test_gathered_keys():
    table = Hashtable()
    table.set("eggs", "bacon")
    table.set("ping", "pong")
    keys = table.keys()
    actual = sorted(keys)
    expected = ["eggs", "ping"]
    assert actual == expected

def test_get():
    table = Hashtable()
    table.set("eggs", "bacon")
    get_value = table.get("eggs")
    actual = get_value
    expected = "bacon"
    assert actual == expected

def test_get_deeper_item():
    table = Hashtable()
    table.set("eggs", "bacon")
    table.set("gegs", "pong")
    table.set("mint", "oreos")
    get_value = table.get("gegs")
    actual = get_value
    expected = "pong"
    assert actual == expected
