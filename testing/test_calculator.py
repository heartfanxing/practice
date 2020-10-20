import pytest
from pythoncode.calculator import Calculator

class TestCalculator:
    def setup_class(self):
        self.cal=Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect",[(1,2,3),(4,5,9)])
    def test_add_int(self,a,b,expect):
        result=self.cal.add(a,b)
        assert(result) ==expect

    @pytest.mark.parametrize("a,b,expect", [(0.1, 0.2, 0.3), (0.11, 0.22, 0.33)])
    def test_add_float(self,a,b,expect):
        result = self.cal.add(a, b)
        assert (round(result,2)) == expect

    @pytest.mark.parametrize("a,b,expect", [(1, 2, 0.5), (4, 2, 2)])
    def test_div_formal(self,a,b,expect):
        result = self.cal.div(a, b)
        assert (result) == expect

    @pytest.mark.parametrize("a,b", [(1, 0), (4, 0)])
    def test_div_zero(self,a,b):
        try:
            result = self.cal.div(a, b)
        except ZeroDivisionError:
            print("除数为0")


#