# Import rsPhysical Light into Houdini
# https://github.com/joppevos/Maya-to-Houdini 

# Edit: Jihyun Nam
# Version: 1.0.0


import json

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

sceneroot = hou.node('/obj')

subnet = sceneroot.createNode('subnet', 'LightRig')

for i in range(len(temp_data)):
    #print(dict[i])
    
    data = temp_data[i]
    
    # Create Root Null
    
    
    #globalnull = sceneroot.createNode('null', 'size_locator')
    #globalnull.setParms({'scale': 1})
    
    
    light = subnet.createNode('rslight', 'Key')
    light.setInput(0, subnet.indirectInputs()[0])
       
    
    subnet.layoutChildren()
        
    light.parmTuple('t').set(tuple(data["translate"][0]))
    light.parmTuple('r').set(tuple(data["rotate"][0]))
    
    light.parm('RSL_intensityMultiplier').set(data["intensity"])    
    light.parm('Light1_exposure').set(data["exposure"])
    
    light.parm('RSL_affectDiffuse').set(data["affectsDiffuse"])
    light.parm('RSL_bidirectional').set(data["areaBidirectional"])
    light.parm('RSL_visible').set(data["areaVisibleInRender"])
    light.parm('RSL_volumeScale').set(data["volumeRayContributionScale"])
    light.parm('RSL_areaShape').set(data["areaShape"])
    

    light.parm('Light1_colorMode').set(str(data["colorMode"]))
    light.parm('Light1_temperature').set(data["temperature"])


    light.parmTuple('areasize').set(tuple(data["scale"][0]))
    
    light.parmTuple('light_color').set(tuple(data["color"][0]))    

    light.parm('RSL_diffuseScale').set(data["diffuseRayContributionScale"])
    light.parm('RSL_specularScale').set(data["glossyRayContributionScale"])
    light.parm('RSL_sssScale').set(data["singleScatteringRayContributionScale"])
    light.parm('RSL_multisssScale').set(data["multipleScatteringRayContributionScale"])
    light.parm('RSL_indirectScale').set(data["indirectRayContributionScale"])
    
    
    light.parm('Light1_unitsType').set(str((data["unitsType"])))
    light.parm('RSL_spread').set(str(data["areaSpread"]))
    
    
    
    light.setGenericFlag(hou.nodeFlag.DisplayComment, True)
    light.setComment(data["name"])
    
    
    