# Food Rocket Project

### Inside
1. Selenium
2. Page Object Model 
3. PyTest
4. Selenoid 
5. ipdb (debugging)

### Pytest configuration

```bash
pytest --setup-show  # show fixtures work result
pytest -s  # allow to see 'print()' statements in the console
pytest -v  # to get more information in output
pytest -m marker_title  # run only selected marker tests
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

### Marked tests

```python
import pytest

class TestClassTitle:
    
    # change 'mark_title' to your mark title
    # add 'mark_title' to the 'pytest.ini' file
    @pytest.mark.mark_title
    def test_function_title(self):
        pass
```

### YAML

```yaml
---
string: This is a string.  # this is comment
command: "sh interface | include Queueing strategy:"

long string: 
    Это очень длинная строка,
    которую сложно читать в однострочной записи,
    так как она вылезает за пределы окна.

list title:
    - string element
    - 2
    - True
    - False
    - next list title:
        - element 1
        - element 2

dictionary title:
  name: !!str Ivan Katkov  # str type
  job: Tech writer
  skill: !!int 0  # int type
...
```
