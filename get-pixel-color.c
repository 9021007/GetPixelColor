#include <stdio.h>
#include <stdlib.h>
#include <ApplicationServices/ApplicationServices.h>


int main(int argc, char* argv[]) {

    // Check if the user provided the x and y coordinates of the pixel
    if (argc != 3) {
        fprintf(stderr, "Usage: %s x y\n", argv[0]);
        return 1;
    }

    // Parse the x and y coordinates from the command line arguments
    int x = atoi(argv[1]);
    int y = atoi(argv[2]);

    // Get the main display
    CGDirectDisplayID mainDisplay = CGMainDisplayID();

    // Get the screen size
    CGRect screenRect = CGDisplayBounds(mainDisplay);

    // Check if the provided coordinates are within the screen bounds
    if (x < 0 || x >= screenRect.size.width || y < 0 || y >= screenRect.size.height) {
        fprintf(stderr, "Error: The coordinates (%d, %d) are outside of the screen bounds.\n", x, y);
        return 1;
    }

    // Get the color of the pixel at the given coordinates
    CGImageRef image = CGDisplayCreateImageForRect(mainDisplay, CGRectMake(x, y, 1, 1));
    if (image == NULL) {
        fprintf(stderr, "Error: Failed to get the color of the pixel at (%d, %d).\n", x, y);
        return 1;
    }
    CFDataRef pixelData = CGDataProviderCopyData(CGImageGetDataProvider(image));
    const UInt8* pixelBytes = CFDataGetBytePtr(pixelData);
    size_t bitsPerPixel = CGImageGetBitsPerPixel(image);
    size_t bytesPerPixel = bitsPerPixel / 8;
    size_t channelCount = bitsPerPixel / 8;
    UInt8 red = 0, green = 0, blue = 0, alpha = 0;
    if (channelCount == 4) {
        blue = pixelBytes[0];
        green = pixelBytes[1];
        red = pixelBytes[2];
        alpha = pixelBytes[3];
    } else if (channelCount == 3) {
        red = pixelBytes[0];
        green = pixelBytes[1];
        blue = pixelBytes[2];
    }
    printf("(%d, %d, %d, %d)\n",red, green, blue, alpha);

    // Clean up
    CFRelease(pixelData);
    CGImageRelease(image);
    //return string of red green and blue
    char *rgb = malloc(3);
    rgb[0] = red;
    rgb[1] = green;
    rgb[2] = blue;
    return rgb;
}