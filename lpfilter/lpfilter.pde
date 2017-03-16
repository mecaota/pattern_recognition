import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;

import processing.awt.PSurfaceAWT;

import gab.opencv.*;

import drop.*;

SDrop drop;
PImage img;
OpenCV opencv;
int textsize=20;
int imgfrag=0;
float zoom =  1.0;

void setup() {
  size(400, 400);
  frameRate(60);
  drop = new SDrop(this);
}

void draw() {
  background(255);
  textAlign(CENTER);
  textSize(textsize);
  if (img != null) {
    changeWindowSize(img.width, img.height);
    lpfillter();
    image(img, 0, 0);
  } else if (imgfrag == -1) {
    changeWindowSize(400, 400);
    fill(0);
    rect(0, height/2-textsize*2, width, 50);
    fill(255);
    text("This File is incompatible file.", width/2, height/2-textsize);
    text("Please drag & drop an image file.", width/2, height/2);
  } else {
    fill(0);
    rect(0, height/2-textsize, width, 30);
    fill(255);
    text("Please drag & drop an image file.", width/2, height/2);
  }
}

void dropEvent(DropEvent theDropEvent) {
  if (theDropEvent.isImage()) {
    println("### loading image ...");
    img = theDropEvent.loadImage();
    imgfrag=1;
  } else {
    imgfrag=-1;
  }
}

void changeWindowSize(int w, int h) {
  frame.setSize( w + frame.getInsets().left + frame.getInsets().right, h + frame.getInsets().top + frame.getInsets().bottom );
  size(w, h);
}

void lpfillter() {
  opencv = new OpenCV(this, img);
  opencv.gray();
  img = opencv.getOutput();
}