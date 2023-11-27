
def webpage(selection):
    global html_CCtrl, html_MCtrl, html_PSets, html_Xprt
    style='''<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .menu {
            text-align: center;
            background-color: #333;
            position: fixed;
            width: 100%;
            top: 0;
        }

        .menu a {
            display: inline-block;
            padding: 12px 0;
            text-decoration: none;
            color: white;
        }

        /* Responsive styling for phone screens */
        @media (max-width: 480px) {
            .menu a {
                display: block;
                padding: 10px 0;
                font-size: 18px;
            }
        }
    </style>'''
    
    
    
    
    html_CCtrl=style+"""
    <title>Color Control</title>
</head>
<body>
   
<div class="menu">
    <a href="/ColorControl">Color Control</a>
    <a href="/MovementControl">Movement Controll</a>
    <a href="/PreSets">Premade Sets</a>

</div>
    <div class="content">
        <h1>Welcome to the Color Control (CCtrl)</h1>
        <p>Click on the menu to navigate.</p>
    </div>
    
     <form>
        <label>Select a color:</label><br>
        <input type="radio" id="primary" name="colors" value="primary">
        <label for="primary">Primary Color</label><br>
        <input type="radio" id="secondary" name="colors" value="secondary">
        <label for="secondary">Secondary Color</label><br>
        <input type="radio" id="tertiary" name="colors" value="tertiary">
        <label for="tertiary">Tertiary Color</label><br>
      
        <input type="radio" id="red" name="color" value="red">
        <label for="red">Red</label><br>
        
        <input type="radio" id="blue" name="color" value="blue">
        <label for="blue">Blue</label><br>
        
        <input type="radio" id="green" name="color" value="green">
        <label for="green">Green</label><br>
        
        <input type="radio" id="yellow" name="color" value="yellow">
        <label for="yellow">Yellow</label><br>
        
        <input type="radio" id="orange" name="color" value="orange">
        <label for="orange">Orange</label><br>
        
        <input type="radio" id="purple" name="color" value="purple">
        <label for="purple">Purple</label><br>
          
        <input type="radio" id="custom" name="color" value="custom">
        <label for="custom">Custom (RGB)</label><br>
         
        <div id="rgbInput" style="display: none;">
            <label for="redValue">Red:</label>
            <input type="number" id="redValue" name="red" min="0" max="255"><br>
            
            <label for="greenValue">Green:</label>
            <input type="number" id="greenValue" name="green" min="0" max="255"><br>
            
            <label for="blueValue">Blue:</label>
            <input type="number" id="blueValue" name="blue" min="0" max="255"><br>
        </div>
        <!-- Include other color options -->
        
        <br><br>
        <label for="brightnessRange">Adjust brightness:</label>
        <input type="range" id="brightnessRange" name="brightness" min="0" max="100" value="50">
        <output for="brightnessRange" id="brightnessValue">50</output><br>
        
        <input type="submit" value="Submit">
    </form>

    <script>
        const rangeInput = document.getElementById('brightnessRange');
        const rangeOutput = document.getElementById('brightnessValue');
        const customColor = document.getElementById('custom');
        const rgbInput = document.getElementById('rgbInput');

        customColor.addEventListener('change', function() {
            if (customColor.checked) {
                rgbInput.style.display = 'block';
            } else {
                rgbInput.style.display = 'none';
            }
        });

        rangeInput.addEventListener('input', function() {
            rangeOutput.value = rangeInput.value;
        });
         const colorRadio = document.querySelectorAll('input[name="color"]');
        colorRadio.forEach(function(radio) {
            radio.addEventListener('change', function() {
                if (radio.value !== 'custom') {
                    rgbInput.style.display = 'none';
                }
            });
        });
    </script><br>
</body>

</html> """


    html_MCtrl=style+"""
    <title>Movement Control</title>
</head>
<body>
    
<div class="menu">
    <a href="/ColorControl">Color Control</a>
    <a href="/MovementControl">Movement Controll</a>
    <a href="/PreSets">Premade Sets</a>
</div>
    <div class="content">
        <h1>Page 1</h1>
        <p>This is content for Movement Control</p>
    </div>
</body>
</html>"""

    html_PSets=style+"""
    <title>Pre Sets</title>
</head>
<body>
    
<div class="menu">
    <a href="/ColorControl">Color Control</a>
    <a href="/MovementControl">Movement Controll</a>
    <a href="/PreSets">Premade Sets</a>
</div>
    <div class="content">
        <h1>Page 2</h1>
        <p>This is content for Pre Sets.</p>
    </div>
</body>
</html>"""
    html_Xprt=style+"""
    <title>Erweiterte Einstellungen</title>
</head>
<body>
   
<div class="menu">
    <a href="/ColorControl">Color Control</a>
    <a href="/MovementControl">Movement Controll</a>
    <a href="/PreSets">Premade Sets</a>
</div>
    <div class="content">
        <h1>Page 3</h1>
        <p>Sike bitch, nothing here</p>
    </div>
</body>
</html>"""
    html="html"
    chosen="_".join([html,str(selection)])

    return bytes(globals()[chosen],'utf-8')

def web_request_parser(raw_request):
    if "ColorControl" in raw_request:
        return "CCtrl"
    elif "MovementControl" in raw_request:
        return "MCtrl"
    elif "PreSets" in raw_request:
        return "PSets"
    else:
        return "CCtrl"
        