from mongoengine import *

class resources(Document):
    resource_id=SequenceField()
    resource_name=StringField(max_length=255)
    resource_contact=IntField()
    resource_skills=ListField()
    resource_experience=IntField()
    
    def born(self,name="",contact=0,skills=[],exp=0):
        self.resource_name=name
        self.resource_contact=contact
        self.resource_experience=exp
        self.resource_skills=skills
    
    def __str__(self):
        return self.resource_name+" "+str(self.resource_contact)+" "+str(self.resource_skills)+" "+str(self.resource_experience)+" "+str(self.resource_id)+"\n"