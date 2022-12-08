#!/bin/bash
gcc -o get-pixel-colorarm get-pixel-color.c -framework ApplicationServices -target arm64-apple-macos11 #arm64
gcc -o get-pixel-color86 get-pixel-color.c -framework ApplicationServices -target x86_64-apple-macos10.12 #x86_64
lipo -create -output get-pixel-color get-pixel-color86 get-pixel-colorarm   #create universal binary
rm get-pixel-color86 get-pixel-colorarm  #remove the old binaries
chmod +x get-pixel-color #make it executable
mv get-pixel-color static/ #move it to the static folder