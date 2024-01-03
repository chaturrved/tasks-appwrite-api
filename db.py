from main import client,db_id ,db_collection_id
from appwrite.services.databases import Databases
import secrets

db = Databases(client)

#create database
# result = db.create(
#     database_id=secrets.token_hex(8),
#     name = 'tasks_db'
# )


#create a collection 
# result = db.create_collection(
#     database_id = db_id,
#     collection_id = secrets.token_hex(8),
#     name = 'tasks'
# )


#define attributes
# result = db.create_string_attribute(
#     database_id = db_id,
#     collection_id = db_collection_id,
#     key = 'name',
#     size = 225,
#     required= True
# )

# result = db.create_string_attribute(
#     database_id = db_id,
#     collection_id = db_collection_id,
#     key = 'description',
#     size = 225,
#     required= false
# )

# result = db.create_string_attribute(
#     database_id = db_id,
#     collection_id = db_collection_id,
#     key = 'due_date',
#     size = 10,
#     required= True
# )


# result = db.create_datetime_attribute(
#     database_id= db_id,
#     collection_id= db_collection_id,
#     key = 'date_added',
#     required= True
# )

# print(result)


# result = db.list_documents(
#     db_id,db_collection_id
# )

# print(result)


class CRUD:
    def __init__(self):
        self.db_id = db_id
        self.coll_id = db_collection_id


    def list_tasks(self):
        result = db.list_documents(
            database_id = self.db_id,
            collection_id= self.coll_id
        )

        print(type(result))
        return result
    

    def create_task(self,data:dict):
        result = db.create_document(
            database_id= self.db_id,
            collection_id= self.coll_id,
            document_id=secrets.token_hex(8),
            data=data
        )

        return result
    
    def retrieve_task(self, task_id:str):
        result = db.get_document(
            database_id= self.db_id,
            collection_id= self.coll_id,
            document_id=task_id
        )

        return result
    
    def update_task(self, task_id:str, data):
        result = db.update_document(
            database_id= self.db_id,
            collection_id= self.coll_id,
            document_id= task_id,
            data=data
        )

        return result
    
    def delete_task(self,task_id:str):
        result = db.delete_document(
            database_id= self.db_id,
            collection_id= self.coll_id,
            document_id= task_id,
        )

        return result