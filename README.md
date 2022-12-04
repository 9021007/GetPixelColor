# GetPixelColor

## A cross-platform python library for getting the color of a given pixel on screen.

 - Compatible with MacOS, Windows, and Linux.
 - Transparency data only be available on some platforms.

__Examples:__

Get color of a specific pixel: `getpixelcolor.pixel(x, y)`

> (R, G, B, (A))

Get average color of an area: `getpixelcolor.average(x, y, width, height)`

> (R, G, B, (A))

Get all color values of an area: `getpixelcolor.area(x, y, width, height)`

> [[[R, G, B, (A)]]]