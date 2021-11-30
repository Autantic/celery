import time
from utils import check_website
from websites import WEBSITE_LIST
from celery import Celery
from celery.result import ResultSet
 
app = Celery('testsite',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')
 
@app.task
def check_website_task(address):
    return check_website(address)
 
if __name__ == "__main__":
 
    #Utilisation de 'delay' pour exécuter les tâches de façon asynchrone
    rs = ResultSet([check_website_task.delay(address) for address in WEBSITE_LIST])
     
    #Patiente que la tâche finisse
    rs.get()