from locust import HttpUser,TaskSet,task,between


class AppUser(HttpUser):
    wait_time = between(2,5)
     
     #endpoint
    @task
    def home_page(self):
        self.client.get("/")
      
    
  

    


    


# to open interface locust
    #http://localhost:8089/