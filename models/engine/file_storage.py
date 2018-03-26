#!/usr/bin/python3
'''
    Define class FileStorage
'''
import json
import models


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
            Return dictionary of all objects or all the objects of a class
        '''
        if not cls:
            return FileStorage.__objects
        else:
            cname = cls.__name__
            print(cname)
            cls_obj = {}
            for k, v in self.__objects.items():
                #print(type(v))
                #print(v.to_dict())
               # print("KEY: " + str(k))
               # print("VALUE: " + str(v))
                if cname == v.__class__.__name__:
                    cls_obj[k] = v #cls(**v.to_dict())
            #print("CLS_OBJ: " + str(cls_obj))
            return cls_obj

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
           deletes obj specified

           Arg:
               obj: object to be deleted
        """
        if obj:
            cname = obj.__class__.__name__
            key = cname + "." + str(obj.id)
            del self.__objects[key]
            self.save()
