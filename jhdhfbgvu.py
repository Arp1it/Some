import inspect


class inspector:
    def __init__(self, obj):
        self.obj = obj
    def object_inspector(self):
        for item in inspect.classify_class_attrs(inspector):
            print(item)


the_object = inspector("CodeWithHarry")
# the_object.object_inspector()


def Inspect_somethingect(something, ch):
    import inspect
    if (ch==1):
        # check whether the arguement is a class or not
        if (inspect.isclass(something)):
            return f"'{something}' is a class."
        
        # check whether the arguement is a module or not
        elif (inspect.ismodule(something)):
            return f"'{something}' is a module."

        # check whether the arguement is a function or not
        elif (inspect.isfunction(something)):
            return f"'{something} is a function."
            
        # check whether the arguement is a method of a class or not
        elif (inspect.ismethod(something)):
            return f"'{something}' is a method."
    
    # if (ch==2):
    #     # returns the class hierarchy
    #     return f"Hierarchy of {something} object is \n{inspect.getmro(something)}"
    
    if (ch==3):
        # returns all the methods, attributes with values of the class.
        return inspect.getmembers(something)
    
    if (ch==4):
        # returns all the parameters passed to a given function
        return inspect.signature(something)
    
    if (ch==5):
        # returns the source code of given class, module, method, function
        return inspect.getsource(something)
    
    if (ch==6):
        # returns the module name of the method or function passed in it.
        return inspect.getmodule(something)
    
    if (ch==7):
        # returns the docstring of the method.
        return inspect.getdoc(something)

print(Inspect_somethingect(the_object, 3))