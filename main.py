# import json to work with json files or data
import json

def getDictionaryContent(content):
    """
        This function takes the value of a dictionary
        and returns its properties(type, tag, description, required).
    """
    sub_dictionary = {}
    if type(content) == int:
        sub_dictionary["type"] = "integer"
        sub_dictionary["tag"] = ""
        sub_dictionary["description"] = ""
        sub_dictionary["required"] = False
    elif type(content) == str:
        sub_dictionary["type"] = "string"
        sub_dictionary["tag"] = ""
        sub_dictionary["description"] = ""
        sub_dictionary["required"] = False
    elif type(content) == list:
        try:
            if type(content[0]) == str:
                sub_dictionary["type"] = "enum"
                sub_dictionary["tag"] = ""
                sub_dictionary["description"] = ""
                sub_dictionary["required"] = False
        except:
                sub_dictionary["type"] = "array"
                sub_dictionary["tag"] = ""
                sub_dictionary["description"] = ""
                sub_dictionary["required"] = False
    elif type(content) == dict:
        sub_dictionary["type"] = "array"
        sub_dictionary["tag"] = ""
        sub_dictionary["description"] = ""
        sub_dictionary["required"] = False
    elif type(content) == bool:
        sub_dictionary["type"] = "bool"
        sub_dictionary["tag"] = ""
        sub_dictionary["description"] = ""
        sub_dictionary["required"] = False
    else:
        sub_dictionary["type"] = "string"
        sub_dictionary["tag"] = ""
        sub_dictionary["description"] = ""
        sub_dictionary["required"] = False
            
    return sub_dictionary



# read the json file and return the schema of the dictionary
with open('data/data_1.json', 'r') as reader:
    content = json.load(reader)
    print(content)
    print(type(content))
    message = content['message']
    print('message')
    print(message)
    keys = ['key_one', 'key_two', 'key_three', 
            'key_four', 'key_five', 'key_six', 'key_seven', 'key_eight',
            'key_nine', 'key_ten', 'key_eleven']
    main_dictionary = {}
    count = 0
    for eachItem in message.values():
        print(eachItem)
        main_dictionary[keys[count]] = getDictionaryContent(eachItem)
        count += 1
        
with open('schema/output.json', 'w') as reader:
    json.dump(main_dictionary, reader, indent=4)
    
    
