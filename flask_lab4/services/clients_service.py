import mysql.connector
from dao.clients_dao import ClientsDAO

class ClientsService:
    def __init__(self):
        self.dao = ClientsDAO()

    def get_all_clients(self):
        return [client.to_dict() for client in self.dao.get_all()]


    def get_client(self, id):
        client = self.dao.get_by_id(id)
        return client.to_dict() if client else None

    def create_client(self, data):
        return self.dao.create(data)

    def update_client(self, id, data):
        return self.dao.update(id, data)

    def delete_client(self, id):
        try:
            return self.dao.delete(id)
        except mysql.connector.Error as e:
            # Foreign key constraint: клієнт має repairs
            if e.errno == 1451:
                raise Exception("Неможливо видалити клієнта — існують пов’язані ремонти.")
            raise
