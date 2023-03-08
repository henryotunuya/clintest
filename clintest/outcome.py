from typing import Tuple

class Outcome:
    def __init__(self, current_value: bool, is_certain: bool) -> None:
        self.__current_value = current_value
        self.__is_certain = is_certain

    def current_value(self) -> bool:
        return self.__current_value

    def is_certain(self) -> bool:
        return self.__is_certain

    def as_tuple(self) -> Tuple[bool, bool]:
        return (self.__current_value, self.__is_certain)

    def is_certainly_true(self) -> bool:
        return self.__is_certain and self.__current_value

    def is_certainly_false(self) -> bool:
        return self.__is_certain and not self.__current_value