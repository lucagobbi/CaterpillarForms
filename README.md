# CaterpillarForms

<img src="./assets/caterpillar_forms.png" width=400>

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=383938&style=for-the-badge&logo=cheshire_cat_ai)](https://)

CaterpillarForms is a dynamic form plugin for the Cheshire Cat AI, allowing for flexible and adaptive form creation and handling.

Leverage the user context, conversation history, or any other runtime information to determine the appropriate form model.

## Features

- Dynamic model generation based on runtime conditions
- Easy-to-use decorator for form creation
- Inherits all capabilities from the base CatForm class
- Allows for user-specific or context-specific form schemas

## Usage

1. Import the necessary components:

```python
from cat.plugins.CaterpillarForms.caterpillarforms import CaterpillarForm, caterpillar_form
from pydantic import BaseModel
```

2. Create your dynamic form by subclassing `CaterpillarForm` and using the `@caterpillar_form` decorator:

```python
@caterpillar_form
class DynamicPizzaForm(CaterpillarForm):
    description = "Dynamic Pizza Order Form"
        start_examples = [
        "order a pizza!",
        "I want pizza"
    ]
    stop_examples = [
        "stop pizza order",
        "not hungry anymore",
    ]
    ask_confirm = True

    def model_getter(self) -> BaseModel:
        # Define your dynamic model logic here
        if self._cat.user_id == "vip_customer":
            return VIPPizzaModel
        else:
            return StandardPizzaModel

    def submit(self, form_data):
        return {"output": f"Pizza order confirmed: {form_data}"}
```

3. Implement your dynamic model logic in the `model_getter` method. This method should return a Pydantic BaseModel.

4. Use your form in your Cat application as you would with regular forms.