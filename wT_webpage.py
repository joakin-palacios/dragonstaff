
def webpage(selection):
    global html_CCtrl, html_MCtrl, html_PSets, html_Xprt
    style='''<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <script>
            window.onload = function () {
                var menu = document.querySelector(".menu");
                var content = document.querySelector(".content");
                content.style.paddingTop = menu.offsetHeight + "px";
            };
        </script>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                text-align: center;
                color: white;
                text-shadow: 1px 1px 2px black;

                font-size: 1em; /* Set the default font size for the entire page */
                background: content-box linear-gradient(magenta, green);
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
                padding: 12px 10px;
                text-decoration: none;
                color: white;
            }
            .spokeColor,
            .colorSide,
            .brightnessRange{
                display: flex;
                justify-content: space-evenly;
            }
            .spokeColor div {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-right: 20px; /* Adjust the margin as needed */
            }
               .preMadeSets button {
                align-items: center;
                width: 25%;
                font-size: 1.2em;
                padding: 1em 0 0.4em;
                margin: 0.4em;
            }
            
           
            .colorSide div {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-right: 20px; /* Adjust the margin as needed */
            }

            .brightnessRange div {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-right: 20px; /* Adjust the margin as needed */
            }
            .formText {
                font-size: 1.2em;
                padding: 0.8em 0 0.4em;
            }
            .preMadeColors {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-evenly;
            }
            .preMadeColors label:not(.customRGB_Input) {
                border: solid;
            }
            .customRGB_Inputdiv {
                text-align: right;
            }
            .preMadeColors div {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 20%;

                margin: 20px; /* Adjust the margin as needed */
            }
            .movements div {
            padding: 0.5em 0;
            }

            #forred {
                color: red;
                background-color: #fff0f0; /* Light pink background for red text */
                padding: 5% 40%;
                width: 20%;
            }

            #forblue {
                color: blue;
                background-color: #e0f0ff; /* Light blue background for blue text */
                padding: 5% 40%;
                width: 20%;
            }

            #forgreen {
                color: green;
                background-color: #e0ffe0; /* Light green background for green text */
                padding: 5% 35%;
                width: 30%;
            }

            #foryellow {
                color: yellow;
                background-color: #333; /* Dark gray background for yellow text */
                padding: 5% 35%;
                width: 30%;
            }

            #fororange {
                color: orange;
                background-color: #fff5e6; /* Light peach background for orange text */
                padding: 5% 33%;
                width: 34%;
            }

            #forpurple {
                color: purple;
                background-color: #f5e6ff; /* Light lavender background for purple text */
                padding: 5% 35%;
                width: 30%;
            }
            #forpink {
                color: #ff69b4; /* Pink text color */
                background-color: #ffe6f0; /* Light pink background */
                padding: 5% 35%;
                width: 30%;
            }

            #forbrown {
                color: #8b4513; /* Brown text color */
                background-color: #ffdab9; /* Light brown background */
                padding: 5% 35%;
                width: 30%;
            }

            #forblack {
                color: #000000; /* Black text color */
                background-color: #d3d3d3; /* Light gray background for black text */
                padding: 5% 35%;
                width: 30%;
            }

            #forwhite {
                color: #ffffff; /* White text color */
                background-color: #808080; /* Dark gray background for white text */
                padding: 5% 35%;
                width: 30%;
            }

            #forcyan {
                color: #00ffff; /* Cyan text color */
                background-color: #e0ffff; /* Light cyan background */
                padding: 5% 35%;
                width: 30%;
            }

            #formagenta {
                color: #ff00ff; /* Magenta text color */
                background-color: #ffe4e1; /* MistyRose background for magenta text */
                padding: 5% 30%;
                width: 40%;
            }

            #forrandom {
                /* Define styles for the "Random" color option */
                /* You can customize this as needed */
                padding: 5% 30%;
                width: 40%;
            }

            /* Additional styles for radio buttons */
            input[type="radio"] {
                margin-right: 5px; /* Add some spacing between radio buttons and labels */
            }

            #forcustom {
                color: red;
                background-color: #fff0f0; /* Light pink background for custom text */
                padding: 0% 30%;
                width: 40%;
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
            <a href="/MovementControl">Movement Control</a>
            <a href="/PreSets">Premade Sets</a>
        </div>
        <div class="content">
            <h1>Welcome to the Color Control Center</h1>
        </div>

        <form>
            <div class="formText"><label>Select a color:</label><br /></div>

            <div class="spokeColor">
                <div><input type="radio" id="primary" name="spokeColor" value="primary" /> <label for="primary">Primary Color</label></div>
                <div><input type="radio" id="secondary" name="spokeColor" value="secondary" /> <label for="secondary">Secondary Color</label></div>
                <div><input type="radio" id="tertiary" name="spokeColor" value="tertiary" /> <label for="tertiary">Tertiary Color</label></div>
            </div>
            <div class="formText"><label>Choose a side:</label><br /></div>

            <div class="colorSide">
                <div><input type="radio" id="thisSide" name="colorSide" value="thisSide" /> <label for="thisSide">This side</label></div>
                <div><input type="radio" checked id="bothSides" name="colorSide" value="bothSides" /> <label for="bothSides">Both sides</label></div>
                <div><input type="radio" id="otherSide" name="colorSide" value="otherSide" /> <label for="otherSide">Other side</label></div>
            </div>
            <div class="preMadeColors">
                <div><input type="radio" id="red" name="color" value="red" /> <label id="forred" for="red">Red</label></div>

                <div><input type="radio" id="blue" name="color" value="blue" /> <label id="forblue" for="blue">Blue</label></div>

                <div><input type="radio" id="green" name="color" value="green" /> <label id="forgreen" for="green">Green</label></div>

                <div><input type="radio" id="yellow" name="color" value="yellow" /> <label id="foryellow" for="yellow">Yellow</label></div>

                <div><input type="radio" id="orange" name="color" value="orange" /> <label id="fororange" for="orange">Orange</label></div>

                <div><input type="radio" id="purple" name="color" value="purple" /> <label id="forpurple" for="purple">Purple</label></div>

                <div><input type="radio" id="pink" name="color" value="pink" /> <label id="forpink" for="pink">Pink</label></div>
                <div><input type="radio" id="brown" name="color" value="brown" /> <label id="forbrown" for="brown">Brown</label></div>
                <div><input type="radio" id="black" name="color" value="black" /> <label id="forblack" for="black">Black</label></div>
                <div><input type="radio" id="white" name="color" value="white" /> <label id="forwhite" for="white">White</label></div>
                <div><input type="radio" id="cyan" name="color" value="cyan" /> <label id="forcyan" for="cyan">Cyan</label></div>
                <div><input type="radio" id="magenta" name="color" value="magenta" /> <label id="formagenta" for="magenta">Magenta</label></div>
                <div><input type="radio" id="random" name="color" value="random" /> <label id="forrandom" for="random">Random</label></div>

                <div><input type="radio" id="custom" name="color" value="custom" /> <label id="forcustom" for="custom">Custom (RGB)</label></div>

                <div class="customRGB_Inputdiv" id="rgbInput" style="display: none;">
                    <label class="customRGB_Input" for="redValue">Red:</label>
                    <input type="number" id="redValue" name="red" min="0" max="255" /><br />

                    <label class="customRGB_Input" for="greenValue">Green:</label>
                    <input type="number" id="greenValue" name="green" min="0" max="255" /><br />

                    <label class="customRGB_Input" for="blueValue">Blue:</label>
                    <input type="number" id="blueValue" name="blue" min="0" max="255" /><br />
                </div>
            </div>
            <br />
            <br />
            <div class="brightnessRange">
                <div>
                    <label for="brightnessRange">Brightness:</label>
                    <input type="range" id="brightnessRange" name="brightness" min="0" max="100" value="100" />
                    <output for="brightnessRange" id="brightnessValue">100 </output><br />
                </div>
            </div>
            <input type="submit" value="Lets go!" />
        </form>

        <script>
            const rangeInput = document.getElementById("brightnessRange");
            const rangeOutput = document.getElementById("brightnessValue");
            const customColor = document.getElementById("custom");
            const rgbInput = document.getElementById("rgbInput");

            customColor.addEventListener("change", function () {
                if (customColor.checked) {
                    rgbInput.style.display = "block";
                } else {
                    rgbInput.style.display = "none";
                }
            });

            rangeInput.addEventListener("input", function () {
                rangeOutput.value = rangeInput.value;
            });
            const colorRadio = document.querySelectorAll('input[name="color"]');
            colorRadio.forEach(function (radio) {
                radio.addEventListener("change", function () {
                    if (radio.value !== "custom") {
                        rgbInput.style.display = "none";
                    }
                });
            });
        </script>
        <br />
    </body>
</html>
"""


    html_MCtrl=style+"""
    <title>Movement Control</title>
    </head>
    <body>
        <div class="menu">
            <a href="/ColorControl">Color Control</a>
            <a href="/MovementControl">Movement Control</a>
            <a href="/PreSets">Premade Sets</a>
        </div>
        <div class="content">
            <h1>Welcome to the Movement Control Center</h1>
        </div>

        <form>
          

           
            <div class="formText"><label>Choose a side:</label><br /></div>

            <div class="colorSide">
                <div><input type="radio" id="thisSide" name="colorSide" value="thisSide" /> <label for="thisSide">This side</label></div>
                <div><input type="radio" checked id="bothSides" name="colorSide" value="bothSides" /> <label for="bothSides">Both sides</label></div>
                <div><input type="radio" id="otherSide" name="colorSide" value="otherSide" /> <label for="otherSide">Other side</label></div>
            </div><br />
              <div class="formText"><label>Choose something !</label><br /></div>
            <div class="movements">
                <div><input type="radio" id="goingOut" name="movementCtrl" value="goingOut" /> <label id="forgoingOut" for="goingOut">Going Out</label></div>

<div><input type="radio" id="goingIn" name="movementCtrl" value="goingIn" /> <label id="forgoingIn" for="goingIn">Going In</label></div>

<div><input type="radio" id="toBounce" name="movementCtrl" value="toBounce" /> <label id="fortoBounce" for="toBounce">Bounce baby bounce!</label></div>

<div><input type="radio" id="doubleBounce" name="movementCtrl" value="doubleBounce" /> <label id="fordoubleBounce" for="doubleBounce">Double bounce!</label></div>

<div><input type="radio" id="clockRotate" name="movementCtrl" value="clockRotate" /> <label id="forclockRotate" for="clockRotate">Rotate</label></div>

<div><input type="radio" id="antiRotate" name="movementCtrl" value="antiRotate" /> <label id="forantiRotate" for="antiRotate">Rotate the other way</label></div>

<div><input type="radio" id="spiral" name="movementCtrl" value="spiral" /> <label id="forspiral" for="spiral">Spiral</label></div>

<div><input type="radio" id="oneRandomMovement" name="movementCtrl" value="oneRandomMovement" /> <label id="foroneRandomMovement" for="oneRandomMovement">One of the above, at random</label></div>

<div><label for="wait">Waiting time in ms:</label>
            <input type="number" id="wait" name="wait" max="1000" value="40" min="0">
           
</div><br />

  
                          </div>
            <br />
            <br />
   
            <input type="submit" value="Lets go!" />
        </form>

       
        <br /><br /><br /><br /><br /><br />
    </body>
</html>
"""



    
    html_PSets=style+""" <title>Premade Sets</title>
    </head>
    <body>
        <div class="menu">
            <a href="/ColorControl">Color Control</a>
            <a href="/MovementControl">Movement Control</a>
            <a href="/PreSets">Premade Sets</a>
        </div>
        <div class="content">
            <h1>Welcome to the Premade Sets Selector</h1>
        </div>

      <div class="preMadeSets">
            <div><form action="/monochromePreMade">
                <button type="submit">Monochrome</button>
            </form></div>
            <div><form action="/blinkPreMade">
                <button type="submit">Blink</button>
            </form></div>
            <div><form action="/interpolatePreMade">
                <button type="submit">Interpolate</button>
            </form></div>
            <div><form action="/rainbowPremade">
                <button type="submit">Rainbow</button>
            </form></div>
                <div><form action="/firePreMade">
                <button type="submit">Fire!</button>
            </form></div>
                <div><form action="/randomPreMade">
                <button type="submit">Random</button>
            </form></div>
        </div>
        <br /><br /><br /><br /><br /><br />
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
        
