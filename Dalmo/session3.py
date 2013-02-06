import os

class repo_dir(object):

    def __init__(self, dir):
        self.current = os.getcwd()
        self.new = dir
   	
    def __enter__(self):
        try:
	    os.chdir(self.new)
	
        except OSError:
            print 'OSError: Path doesn\'t exists'
   	
    def __exit__(self, type, value, traceback):
        os.chdir(self.current)	

class CourseRepo(object):

    def __init__(self, name):
        self.surname = name

    @property
    def surname(self):
        return self._surname
        
    @surname.setter
    def surname(self,name):
        self._surname=name
        self.required=['.git','setup.py','README.md','scripts/getting_data.py','scripts/check_repo.py',self.surname+'/__init__.py',self.surname+'/session3.py']

    def check(self):
        F=True
        List = self.required
        for item in List:
            if os.path.exists(item)==False:
                F=False
        if F==False:
            return False
        else:
            return True
