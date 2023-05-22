// #include <LiquidCrystal.h>
#include "LiquidCrystal.h"

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

int counter = 0;

void setup() {
  // set up the LCD's number of columns and rows:
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Waiting...");
  delay(1000);
}

void loop() {
  if (Serial.available()) {
    // Read the incoming data
    char data = Serial.read();
    Serial.print("data:\t");
    Serial.print(data);
    Serial.print("\n");
    if (data == '\n') {
      // Clear the LCD
      lcd.clear();
    } else {
      // Print the received character on the LCD
      lcd.print(data);
      if () lcd.scrollDisplayLeft();
    }
    counter ++;
  } else {
    Serial.print("Serial not available");
  }
}
