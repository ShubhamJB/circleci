from main import Add, Subtract

def test_add():
    assert Add(2,3) == 5
    assert Add(5,6) == 11

def test_subtract():
    assert Subtract(5,2) == 3

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("All tests passed")
    
    #step1 : git add .
    #step2 : git commit --allow-empty -m "trigger ci"
    #step3 : git push 