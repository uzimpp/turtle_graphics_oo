# OO code using turtle graphics

A Python program that generates various geometric art patterns using object-oriented programming principles and the turtle graphics library.

## Implementation Details
The program consists of three main classes:
- `PolygonArt`: Main controller class that manages the art generation
- `Polygon`: Base class for creating single polygons with random attributes
- `EmbeddedPolygon`: Derived class that creates nested polygon patterns

### Key Features
- Object-oriented design with inheritance and encapsulation
- Random generation of:
  - Polygon sizes (50-150 units)
  - Colors (RGB values)
  - Locations on screen (-300 to 300 x, -200 to 200 y)
  - Border sizes (1-10 units)
- Nine different art patterns (selected via user input)
- Embedded polygons with configurable depth (for patterns 5-9)

### Art Pattern Types
1. Basic triangles
2. Squares only
3. Pentagons only
4. Random 3-5 sided polygons
5. Embedded triangles
6. Embedded squares
7. Embedded pentagons
8. Random embedded 3-5 sided polygons
9. Random embedded 3-5 sided polygons with varying depths

## How to Use
1. Run the program
2. Enter a number between 1-9 to generate different art patterns
3. Enter 0 to exit the program

## Dependencies
- Python 3.x
- turtle module (built-in)

## Author
Worakrit Kullanatpokin