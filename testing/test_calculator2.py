import pytest
from pythoncode.calculator import Calculator
import yaml


def get_data():
    result = yaml.safe_load(open("./test_data.yml"))
    return result


class TestAdd:

    def setup_class(self):
        self.cal=Calculator()

    @pytest.mark.usefixtures("begin")
    @pytest.mark.parametrize("a,b,expect",get_data()["add_data"]["int"])
    def test_add_int(self,a,b,expect):
        result=self.cal.add(a,b)
        print(a,b)
        assert(result) ==expect

    @pytest.mark.parametrize("a,b,expect", get_data()["add_data"]["float"])
    def test_add_float(self,a,b,expect):
        result = self.cal.add(a, b)
        assert (round(result,2)) == expect

class TestSub:

    def setup_class(self):
        self.cal=Calculator()

    @pytest.mark.parametrize("a,b,expect",get_data()["sub_data"]["int"])
    def test_sub_int(self,a,b,expect):
        result=self.cal.sub(a,b)
        assert(result) ==expect

    @pytest.mark.parametrize("a,b,expect", get_data()["sub_data"]["float"])
    def test_sub_float(self,a,b,expect):
        result = self.cal.sub(a, b)
        assert (round(result,2)) == expect

class TestMul:

    def setup_class(self):
        self.cal=Calculator()

    @pytest.mark.parametrize("a,b,expect",get_data()["mul_data"]["int"])
    def test_mul_int(self,a,b,expect):
        result=self.cal.mul(a,b)
        assert(result) ==expect

    @pytest.mark.parametrize("a,b,expect", get_data()["mul_data"]["float"])
    def test_mul_float(self,a,b,expect):
        result = self.cal.mul(a, b)
        assert (round(result,2)) == expect

class TestDiv:

    def setup_class(self):
        self.cal=Calculator()

    @pytest.mark.parametrize("a,b,expect", get_data()["div_data"]["formal"])
    def test_div_formal(self,a,b,expect):
        result = self.cal.div(a, b)
        assert (result) == expect


    @pytest.mark.parametrize("a,b", get_data()["div_data"]["zero"])
    def test_div_zero(self,a,b):
        try:
            result = self.cal.div(a, b)
        except ZeroDivisionError:
            print("除数为0")