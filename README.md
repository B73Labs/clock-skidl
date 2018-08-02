# Skidl + KiCad + Freerouting Clock Example

## Components

- WS2813 LEDs

## Programs
- Skidl 0.0.22
- KiCad
- Freerouting/LayoutEditor
- PyCharm Community

## Clock Generation

- Generate clock.net

`./clock.py`

- Load netlist into pcbnew
  - Open pcbnew
  - Tools > Load Netlist
  - Load clock.net
  - Select Re-associate footprints by reference (if required)
  - Update PCB
  - Close
  - Save pcb
  - Close pcbnew

- Generate layout
`./clock_place_leds.py`

- Export DSN for Freerouting
  - Open pcbnew
  - Export > Spectra DSN - `clock.dsn`
  
- Auto routing
  - Open freerouting
  - Open Your Own Design - `clock.dsn`
  - click Autorouter
  - get a coffee
  - File > Export Specctra Session File
  - File > Save and Exit  
  - Open pcbnew
  - File > Import > Specctra Session `clock.ses`
  
## References

- [KiCad Scripting Reference](https://github.com/KiCad/kicad-doc/blob/master/src/pcbnew/pcbnew_python_scripting.adoc)
- [Arranging components in a circle with KiCad](http://kevincuzner.com/tag/pcbnew/)
- [Skidl docs](https://xesscorp.github.io/skidl/docs/_site/index.html)
- [Python Scripting Example: Studio Clock](https://forum.kicad.info/t/python-scripting-example-studio-clock/5387)
- Studio Clock source - [KiCadStudioClock.zip](https://kicad-info.s3-us-west-2.amazonaws.com/original/2X/4/49e167315a677e95bbfc2e08c05e37a0b8d94dea.zip)
- Skidl: Blinkenface - [Others use it, too!](https://xesscorp.github.io/skidl/docs/_site/blog/others-use-it-too)
- Miles McCoo [KiCad Scripting blog](https://kicad.mmccoo.com/)
- Skidl: Studio Clock - [Two Easy Pieces](https://xesscorp.github.io/skidl/docs/_site/blog/two-easy-pieces)
- [LayoutEditor](http://www.layouteditor.net/)
