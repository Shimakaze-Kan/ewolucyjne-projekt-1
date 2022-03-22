from parameters_dto import ParametersDto


class CalculationsManager:
    params: ParametersDto = None

    def __init__(self, params: ParametersDto) -> None:
        self.params = params
        pass

    def start(self) -> None:
        pass
