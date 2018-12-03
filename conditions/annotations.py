from inspect import signature


def enforce_type_annotations(func):
    # Probably too unpythonic for regular use, but I can see this being used in testing
    sig = signature(func)
    print(sig.parameters)
    print(sig.return_annotation)
    # TODO use these to check if types were defined and if so, verify passed parameters match those types
    return func