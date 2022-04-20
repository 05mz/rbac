#!/usr/bin/python3




class Resources:
   

    def __init__(self):
        # Initialize resources
        self.resources = {}

    def addResource(self, resource, parents=[]):
      
        self.resources.setdefault(resource, set())
        self.resources[resource].update(parents)
