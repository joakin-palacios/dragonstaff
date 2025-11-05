import setupnfunctions as snf

async def webpage(color, state):
    #Template HTML
    def hex_string (rgb):
        return '%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])
    html = """<!DOCTYPE html>
<html>

<head>
    <title>Choose the color goddammnit</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #4b8b3b;

        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background-color: #f2f2f2;
        }

        h2 {
            text-align: center;
            font-size: 32px;
        }

        button {
            padding: 12px 24px;
            margin: 8px;
            border-radius: 4px;
            border: none;
            color: black;
            font-size: 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }



        form {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin: 16px 0;
        }

        form label {
            display: block;
            margin-right: 8px;
            font-size: 18px;
        }

        form input[type="color"] {
            margin-right: 8px;
            height: 36px;
            width: 100px;
            padding: 4px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        form input[type="number"] {
            margin-right: 8px;
            height: 36px;
            width: 100px;
            padding: 4px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        form input[type="submit"] {
            padding: 12px 24px;
            border-radius: 4px;
            border: none;
            color: black;
            font-size: 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        p {
            text-align: center;
        }
    </style>
</head>

<body>
    <div>
        <h2>J's Dragonstafff controls</h2>
        <p> Enjoy</p>
        <div>
            <form action="/monochrome">
                <button type="submit">Monochrome</button>
            </form>
            <form action="/blink">
                <button type="submit">Blink</button>
            </form>
            <form action="/only_ends">
                <button type="submit">Only Ends</button>
            </form>
            <form action="/only_blink">
                <button type="submit">Only Ends Blink</button>
            </form>
            <form action="/add_random">
                <button type="submit">One at a time</button>
            </form>
            <form action="/cycle">
                <button type="submit">Cycle</button>
            </form>
            <form action="/bycle">
                <button type="submit">Bycle</button>
            </form>            
            <form action="/bounce">
                <button type="submit">Bounce</button>
            </form>
            <form action="/rainbow">
                <button type="submit">Rainbow</button>
            </form>
            <form action="/firework">
                <button type="submit">Firework</button>
            </form>
            <form action="/random_xD">
                <button type="submit">Random!</button>
            </form>
            <form action="/water_waves">
                <button type="submit">Waves</button>
            </form>
            <form action="/trigonometric_fade">
                <button type="submit">Fade</button>
            </form>
            <form action="/side_b">
                <button type="submit">Side B</button>
            </form>
            <form action="/side_a">
                <button type="submit">Side A</button>
            </form>
            <form action="/both_sides">
                <button type="submit">Both Sides</button>
            </form>
        </div>
        <p> mode: %s <br> waiting time : %d ms <br> Main and secondary colors : <span style="display: inline-block;
  width: 25px; height: 25px; background-color: #%s; vertical-align: middle; margin-left: 5px;   border: 2px solid black;
"></span><span style="display: inline-block;
  width: 25px; height: 25px; background-color: #%s; vertical-align: middle; margin-left: 5px;   border: 2px solid black;
"></span></p>

        <form>
            <label for="main_color">Main:</label>
            <input type="color" id="main_color" name="main_color" value="#%s">
            <input type="submit" value="color me!">
        </form>
          <form>
            <label for="co_color">Secondary:</label>
            <input type="color" id="co_color" name="co_color" value="#%s">
            <input type="submit" value="color me!">
        </form>
        <form action="/main_color=%%23000000">
                <button type="submit">Black on 1</button>
            </form>
            <form action="/co_color=%%23000000">
                <button type="submit">Black on 2</button>
            </form>
        <form>
            <label for="wait">Waiting time in ms:</label>
            <input type="number" id="wait" name="wait" max="1000" min="0">
            <input type="submit" value="set wait">
        </form>
    </div>
</body>

</html> """ % (snf.this_side.status, snf.this_side.wait, hex_string(snf.this_side.color), hex_string(snf.this_side.co_color), hex_string(snf.this_side.color), hex_string(snf.this_side.co_color))
    return bytes(html, 'utf-8')