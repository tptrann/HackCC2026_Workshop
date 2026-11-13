#define ECHO_PIN 27
#define TRIG_PIN 25
#define TIME_THRESHOLD 30000  //microsecond
#define MAX_DISTANCE 50 //cm
bool previousDetection = false;
bool currentDetection = false;

void setup() {
  Serial.begin(115200);

  pinMode(ECHO_PIN , INPUT);
  pinMode(TRIG_PIN, OUTPUT);

  delay(2000);
}

void loop() {
  // Read from ultrasound
  
  // Set trig pin to low
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  unsigned long time = pulseIn(ECHO_PIN, HIGH, TIME_THRESHOLD);
  // return 0 when timeout with no detecting
  currentDetection = (time > 0) && (time / 58) < MAX_DISTANCE;

  if (currentDetection && currentDetection != previousDetection) {
      Serial.println("DATA: Object detected");
      delay(500);
  }
  previousDetection = currentDetection;
  delay(50);
}
