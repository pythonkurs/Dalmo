from Dalmo.session3 import CourseRepo,repo_dir 
import sys
import os

CHECK='FAIL'

dir=sys.argv[1]
base=os.path.basename(dir)

context_manager=repo_dir(dir)

with context_manager as cm:
 
    repo=CourseRepo(base)
    if repo.check()==True:
        CHECK='PASS'
   
    print CHECK
