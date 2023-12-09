# GetPixelColor

## A cross-platform python library for getting the color of a given pixel on screen.

![img](https://github.com/Bobrobot1/GetPixelColor/actions/workflows/tests.yml/badge.svg) [![Downloads](https://static.pepy.tech/badge/getpixelcolor)](https://pepy.tech/project/getpixelcolor) [![Downloads](https://static.pepy.tech/badge/getpixelcolor/month)](https://pepy.tech/project/getpixelcolor)


 - Compatible with MacOS, Windows, and Linux.
 - Transparency data only available on some platforms.
   
__Examples:__

Make sure you first `import getpixelcolor`

Get color of a specific pixel: `getpixelcolor.pixel(x, y)`

> (R, G, B, (A))

Get average color of an area: `getpixelcolor.average(x, y, width, height)`

> (R, G, B, (A))

Get all color values of an area: `getpixelcolor.area(x, y, width, height)`

> [[[R, G, B, (A)]]]

https://pypi.org/project/GetPixelColor/
