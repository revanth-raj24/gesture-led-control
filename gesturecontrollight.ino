int ledPin = 9;
String data = "";
int brightness = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    data = Serial.readStringUntil('\n');
    brightness = data.toInt();
    brightness = constrain(brightness, 0, 255);

    analogWrite(ledPin, brightness);
  }
}
