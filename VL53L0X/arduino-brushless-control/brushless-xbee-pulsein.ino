const uint8_t VescOutputPin = 0;
int pulseInPin = 2;
unsigned long duration;

void setup() {
  //Commence by holding pin low to activate our brushless driver
  OCR0A = 156;
  pinMode(VescOutputPin, OUTPUT);
  digitalWrite(VescOutputPin, HIGH);
  delay(1000);
  pinMode(pulseInPin, INPUT);
}

void loop() 
{
  duration = pulseIn(pulseInPin, HIGH);
  duration = constrain(duration, 10, 62);
  //result from XBee PWM is 0-65
  int result = map(duration, 10, 62, 0, 255);
  result = constrain(result, 0, 255);
  analogWrite(VescOutputPin, result);

}
