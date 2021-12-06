# added background_enable attribute

# Edit: Jihyun Nam
# Version: 1.0.0


import json

try:
    subnet = hou.selectedNodes()[0]
except IndexError:
    hou.ui.displayMessage("Please select subnet(LightRig) first")
    exit()
    

    
def filePath():
    """ ask for file path"""
    filepath = hou.expandString(hou.ui.selectFile())
    return filepath
    
def loadJson():
    """ let user select the attribute filepath to read  """
    json_file = filePath()      
    with open(json_file) as data_file:
        data = json.load(data_file)
        #data = [s.encode('utf-8') for s in data_file]        
    return data

def getData(filename):
    return eval(open(filename).read(), {"false": False, "true":True})

temp_data = getData(filePath())


for i in range(len(temp_data)):
    #print(dict[i])
    
    data = temp_data[i]
     
    
    # Create RS_Domelight
    light = subnet.createNode('rslightdome::2.0', 'Dome')

    light.setInput(0, subnet.indirectInputs()[0])

    subnet.layoutChildren()
    
    #light.parmTuple('t').set(tuple(data["translate"][0]))
    #light.parmTuple('r').set(tuple(data["rotate"][0]))
    
    #light.parm('RSL_intensityMultiplier').set(data["intensity"])    
    #light.parm('Light1_exposure').set(data["exposure"])
    
    light.parm('env_map').set(data["tex0"])

    light.parm('gamma0').set(data["gamma0"])
    
    light.parm('RSL_saturation').set(data["saturation0"])   

    light.parmTuple('light_color').set(tuple(data["color"][0]))
    
    light.parm('RSL_diffuseScale').set(data["diffuseRayContributionScale"])
    light.parm('RSL_specularScale').set(data["glossyRayContributionScale"])
    light.parm('RSL_sssScale').set(data["singleScatteringRayContributionScale"])
    light.parm('RSL_multisssScale').set(data["multipleScatteringRayContributionScale"])
    light.parm('RSL_indirectScale').set(data["indirectRayContributionScale"])
    
    light.parm('background_enable').set(data["background_enable"])
    
    light.setGenericFlag(hou.nodeFlag.DisplayComment, True)
    light.setComment(data["name"])
    
    
    