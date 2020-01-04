from typing import Any, Dict


class SubclassRegister:
    # Technically, this can be replaced by a call to __subclasses__(), but this enforces the presence and uniqueness
    # of the class variable (and these checks are run at import time).
    # It also allows for removing some classes from the registry

    _registry: Dict[type, Dict[Any, type]] = {}  # Registers the subclasses
    _key_registry: Dict[type, str] = {}  # Registers the class variable to use as a key for each SubclassRegister class

    @classmethod
    def __init_subclass__(cls, key: str=None, intermediate: bool=False, **kwargs) -> None:
        """
        :param key: The name of the class variable to use as a key in the registry
        :param intermediate: (default False) if True, do not save this class in the registry
        :param kwargs: Should be empty
        :raises ValueError: If the key's value is not unique
        :raises AttributeError: If one of the subclasses does not have the correct class variable
        """
        super().__init_subclass__(**kwargs)

        if intermediate:
            return

        if SubclassRegister in cls.__bases__:
            # If the class inherits from SubclassRegister directly, it's a base class; its subclasses should be saved
            SubclassRegister._registry[cls] = {}
            SubclassRegister._key_registry[cls] = key
        else:
            for c in SubclassRegister._registry:
                if issubclass(cls, c):
                    # It should have the required class variable, and that should be unique
                    key = getattr(cls, SubclassRegister._key_registry[c])

                    if key in SubclassRegister._registry[c]:
                        raise ValueError(f'Key should be unique, was: {key}')

                    SubclassRegister._registry[c][key] = cls

    @classmethod
    def get_subclass(cls, key) -> type:
        """
        :param key: A key
        :return: The subclass of cls that was registered with that key
        :raises KeyError: if the key is unknown
        """
        return SubclassRegister._registry[cls][key]
