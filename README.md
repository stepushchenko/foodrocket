# Food Rocket company

### Inside

1. Selenium
2. Page Object Model 
3. PyTest - framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
4. Selenoid - launch different browsers in parallel

### Other libraries 
1. ipdb - python debugging


### Pytest configuration

```bash
pytest --setup-show  # show fixtures work result
pytest -s  # allow to see 'print()' statements in the console
pytest -v  # to get more information in output
pytest --driver=chrome  # to select driver, which will run tests
pytest --env=prod  # to select env, which will be used in tests
```

### Debugging

```python
import ipdb
from pages.base_page import BasePage

class TestClassTitle:
    
    def test_function_title(self, driver, env):
        browser = BasePage(driver, env)
        ipdb.set_trace()  # here debugging will be started
        browser.open('')
```

### Parametrization

```python
import pytest

class TestClassTitle:
    
    @pytest.mark.parametrize("parameter1, parameter2", [('parameter1_value1', 'parameter2_value1'), ('parameter1_value2', 'parameter2_value2')])
    def test_function_title(self, parameter1, parameter2):
        return parameter1 + parameter2
```