
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id":self._generateId(),
                "name":"John",
                "last_name":last_name,
                "years_old":33,
                "lucky_numbers":[7,13,22]
            },
            {
                "id":self._generateId(),
                "name":"Jane",
                "last_name":last_name,
                "years_old":35,
                "lucky_numbers":[10,14,3]
            },
            {
                "id":self._generateId(),
                "name":"Jimmy",
                "last_name":last_name,
                "years_old":5,
                "lucky_numbers":[1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        response_body={
            "msg":"ok - member added"
        }
        return response_body

    def delete_member(self, id):
        counter = 0
        for member in self._members:
            if member["id"] == id:
                del self._members[counter]
                response_body={
                    "msg":"ok - member deleted",
                }
                return response_body
            counter+=1
        return "Miembro no encontrado"

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                response_body={
                    "msg":"ok",
                    "member":{
                        "id":member["id"],
                        "name":member["name"],
                        "last_name":member["last_name"],
                        "years_old":member["years_old"],
                        "lucky_numbers":member["lucky_numbers"]
                    }
                }
                return response_body
        return "Miembro no encontrado"

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
