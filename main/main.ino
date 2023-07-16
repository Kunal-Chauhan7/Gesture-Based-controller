#include "Wire.h"       
#include "I2Cdev.h"     
#include "MPU6050.h"    

const int buttonPin_right = 7;
const int buttonPin_left = 8;
int buttonState_right = 0;
int buttonState_left = 0;

MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;

struct MyData {
  byte X;
  byte Y;
};

MyData data;

void setup()
{
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  pinMode(buttonPin_right, INPUT);
  pinMode(buttonPin_left, INPUT);
}

void loop()
{
  delay(500);
  buttonState_right = digitalRead(buttonPin_right);
  buttonState_left = digitalRead(buttonPin_left);
  if(buttonState_left == 1){
    Serial.println("leftClick"); 
  }
  if(buttonState_right == 1){
    Serial.println("rightClick");
  }
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  data.X = map(ax, -17000, 17000, 0, 255 );
  data.Y = map(ay, -17000, 17000, 0, 255);
   if (data.Y < 80) { //gesture : down 
    Serial.println("up");
    }
 if (data.Y > 145) {//gesture : up
  Serial.println("down");
    }
 if (data.X > 155) {//gesture : left
  Serial.println("left");
    }
 if (data.X < 80) {//gesture : right
  Serial.println("right");
    }
}
