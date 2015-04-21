void light(char n){
 for(char i =0;i<4;++i)
   digitalWrite(i+9,LOW);
 for(char i=0;i<n;++i)
   digitalWrite(i+9,HIGH);
}

void setup() {                
  // initialize the digital pin as an output.
  pinMode(9, OUTPUT); 
  pinMode(10, OUTPUT); 
  pinMode(11, OUTPUT); 
  pinMode(12, OUTPUT);   
  Serial.begin(9600);
  Serial.write("HI!");
}

// the loop routine runs over and over again forever:
void loop() {
  char n;
  if(Serial.available()>1){
      n = Serial.parseInt();
      light(n);
      Serial.println(n,DEC);
    }
}
