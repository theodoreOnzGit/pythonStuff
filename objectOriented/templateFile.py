class yourClass:

    def __init__(self):

        print('this is the '+ self.__class__.__name__  + ' constructor')



class test:

    def __init__(self):

        print('welcome to the test class')

        import importlib
        self.importlib = importlib


    def returnYourObject(self):

        importlib = self.importlib

        yourClass = getattr(importlib.import_module(__name__),'yourClass')
        yourObject = yourClass()

        return yourObject

    def test2(self):

        print('this is test 2')



class workspace:

    def __init__(self):

        print('initialising workspace')

        self.initialiseDefaults()


    def getTestObj(self):

        self.reloadClasses()
        self.testObj = self.test()

        return self.testObj

    def getClassObj(self):

        self.reloadClasses()
        self.templateClassObj = self.templateClass()

        return self.templateClassObj



    def initialiseDefaults(self):

        # the first part grabs the name of the module 
        # __name__ is a string with the name of this python file
        # but i cannot use import __name__
        # because python thinks i'm importing a string
        # i need to convert it into a variable
        # then i can import it

        # for this we use import library

        import importlib
        self.importlib = importlib

        myModule = importlib.import_module(__name__)
        # https://www.devdungeon.com/content/import-python-module-string-name

        # now we need to do the same thing for classes
        # https://www.blog.pythonlibrary.org/2012/07/31/advanced-python-how-to-dynamically-load-modules-or-classes/

        test = getattr(importlib.import_module(__name__),'test')

        self.test = test
        self.testClassName = self.returnClassName(test)

        from importlib import reload
        self.reload = reload

        print("workspace defaults initiated")

    def reloadClasses(self):

        reload = self.reload
        importlib = self.importlib

        myModule = importlib.import_module(__name__)
        reload(myModule)
        # https://www.blog.pythonlibrary.org/2012/07/31/advanced-python-how-to-dynamically-load-modules-or-classes/

        # the code be

        test = getattr(importlib.import_module(__name__),'test')
        self.test = test


    def returnClassName(self,yourClass):

        object = yourClass()

        return object.__class__.__name__





def printHelp():

    print('hello, welcome to the templateClass module')

    print(' ')

    print('to load test modules use:')

    print(' ')

    print('import '+__name__)
    print('self = '+__name__+'.workspace()')

    print(' ')
    print('testObj = self.getTestObj()')
    print('testObj.returnYourObject()')



printHelp()


