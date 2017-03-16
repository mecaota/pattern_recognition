import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;

import gab.opencv.*;

PImage img;
OpenCV opencv;


void setup() {
  img = loadImage("test.png");
  opencv = new OpenCV(this, "test.png");
}

void draw() {
  changeWindowSize(img.width+opencv.width, opencv.height);
  opencv.gray();
  
  
  
  
  
  
  
  
  
  
  output();
}
void output() {
  image(img, 0, 0);
  image(opencv.getOutput(), opencv.width, 0);
}

void changeWindowSize(int w, int h) {
  frame.setSize( w + frame.getInsets().left + frame.getInsets().right, h + frame.getInsets().top + frame.getInsets().bottom );
  size(w, h);
}