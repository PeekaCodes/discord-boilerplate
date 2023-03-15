import json
import os


__config_name__ = "config.json"


def getJson(src:str)->dict:
    __cwd__ = os.path.dirname(__file__)
    
    if(not(os.path.exists(f"{__cwd__}/{src}"))):
        __cwd__ = __cwd__.removesuffix(os.path.basename(__cwd__))[:-1]
        if(not(os.path.exists(f"{__cwd__}/{src}"))):
            __cwd__ = __cwd__.removesuffix(os.path.basename(__cwd__))[:-1]
            if(not(os.path.exists(f"{__cwd__}/{src}"))):
                __cwd__ = __cwd__.removesuffix(os.path.basename(__cwd__))[:-1]

                
    
    try:
            filePath = f"{__cwd__}/{src}"
            file = open(filePath)
            return json.load(file)
    except:
        return None
            

    
def getGuildId()->int:
    config = getJson(__config_name__)
    return int(config.get("guild_id"))


def getAdminRoles()->list[int]:
    config = getJson(__config_name__)
    return config.get("admin_roles")


