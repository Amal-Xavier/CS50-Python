from hello import hello

def test_hello():
    for name in ["hermione","harry","ron"]:
        assert hello(name) == f"hello,{name}"

    

def test_arguments():
    assert hello("world") == "hello,world"