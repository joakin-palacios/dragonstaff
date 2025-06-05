import setupnfunctions as snf

def modes(request):

    if "main_color" in request :
        snf.color=findrgbs(request)
        
    if "co_color" in request :
        snf.co_color=findrgbs(request)    
        
    elif "wait" in request:
        snf.wait = set_waiting_time(request)
        
    elif "/monochrome" in request:
        snf.status="Monochrome"
        
    elif "/blink" in request:
        snf.status="Blink"    
    
    elif "/cycle" in request:
        snf.status="Cycle"
    
    elif "/bycle" in request:
        snf.status="Bycle"
    
    elif "/bounce" in request:
        snf.status="Bounce"

    elif "/MPU" in request:
        snf.status="MPU Sensor"

    elif "/rainbow" in request:
        snf.status="Rainbow"
        
    elif "/firework" in request:
        snf.status="Firework"
        
    elif "/random_xD" in request:
        snf.status="Random"
        
    elif "/only_ends" in request:
        snf.status="OnlyEnds"
        
    elif "/only_ends_blink" in request:
        snf.status="OnlyEndsBlink" 

    
def set_waiting_time(raw_request):
    get_string=str(raw_request)
    start_index = get_string.find("wait=") + len("wait=")
    end_index = len(get_string)-1
    if start_index!= end_index: 
        wait_time = int(float(get_string[start_index:end_index]))
    else:
        wait_time=60
    print (f"time has set to {wait_time}")
    return wait_time
    
def findrgbs(string):
    # Extract the color code from the string
    string=str(string)
    color_code = string.split('=')[1].strip()

    # Convert the color code to RGB tuple
    r = int(color_code[3:5], 16)
    g = int(color_code[5:7], 16)
    b = int(color_code[7:9], 16)
#     print (color_code[3:5],color_code[5:7],color_code[7:9])

    return (r, g, b)   