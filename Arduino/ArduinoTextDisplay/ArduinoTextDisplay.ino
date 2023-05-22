#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

const String INITIAL_DISPLAY = "Waiting...      ";
const int BAUDRATE = 9600;
const int SCROLL_LIMIT = 8;
int counter = 0;

void setup() {
  // set up the LCD's number of columns and rows:
  Serial.begin(BAUDRATE);
  lcd.begin(16, 1);
  lcd.setCursor(0, 0);
  lcd.print(INITIAL_DISPLAY);
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
      counter ++;
      if (counter >= SCROLL_LIMIT) {
        for (int i = 0; i < counter; i ++) {
          lcd.scrollDisplayLeft();
        }
        counter = 0;
        delay(1000);
      }
    }
  } else {
    Serial.print("Serial not available");
  }
}
