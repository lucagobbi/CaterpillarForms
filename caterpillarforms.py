from pydantic import BaseModel
from cat.experimental.form import CatForm

class CaterpillarForm(CatForm):
    def __init__(self, cat):
        super().__init__(cat)
        self.model_class = self.model_getter()

    def model_getter(self) -> BaseModel:
        raise NotImplementedError("Subclasses must implement model_getter()")


# caterpillar form decorator
def caterpillar_form(Form: CaterpillarForm) -> CaterpillarForm:
    Form._autopilot = True
    if Form.name is None:
        Form.name = Form.__name__

    if Form.triggers_map is None:
        Form.triggers_map = {
            "start_example": Form.start_examples,
            "description": [f"{Form.name}: {Form.description}"],
        }

    return Form
