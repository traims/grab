from ..error import GrabError


class ItemError(GrabError):
    pass


class ChoiceFieldError(ItemError):
    pass
