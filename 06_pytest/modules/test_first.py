import pytest 

class TestClass:
    
    def test_method1(self):
        print("test method 1")
        assert 1==1
        
    @pytest.mark.sanity
    def test_method2(self):
        print("test method 2")
        assert 1==1
        
    @pytest.mark.regression
    def test_method3(self):
        print("test method 3")
        assert 1==1
        