class Employee:
   def __init__(self,eid,name,age,deptid):
       self.eid=eid
       self.name=name
       self.age=age
       self.deptid=deptid
       
   def printEmp(self):
       print("Employee id:",self.eid,"name:",self.name,"age:",self.age,"dept id:",self.deptid)
      
def main(self):
    emp = Employee(242,"ram",43,4324)
    emp.printEmp()  
   
