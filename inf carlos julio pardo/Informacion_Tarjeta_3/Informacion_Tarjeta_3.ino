

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

//--------------------------------- VARIABLES
// Sectores y bloques para leer: SECTOR_1 / BLOQUES 

String tagID = "";
byte readCard[4];

//--------------------------------- FUNCION LECTURA
//-----------------------------------
// 1. Lectura de ID 
//-----------------------------------
uint8_t Lectura() {
   
  // Getting ready for Reading PICCs
  if ( ! mfrc522.PICC_IsNewCardPresent()) { //If a new PICC placed to RFID reader continue
    return 0;
  }
  if ( ! mfrc522.PICC_ReadCardSerial()) {   //Since a PICC placed get Serial and continue
    return 0;
  }
  tagID = "";
  for ( uint8_t i = 0; i < 4; i++) {  // El UID de la tarjeta MIFARE PICCs de 1K tiene 4 bytes
    readCard[i] = mfrc522.uid.uidByte[i];
    tagID.concat(String(mfrc522.uid.uidByte[i], HEX)); // Concatenar los 4 bytes en una variable string
  }
  tagID.toUpperCase();
  Serial.print(F("UID:"));
  Serial.println(tagID);
  
 

//-----------------------------------
// 1. Lectura INFORMACION USUARIO
//-----------------------------------

  MFRC522::StatusCode status;
  MFRC522::MIFARE_Key key;
  for(byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF; // asignacion a los 6 bytes de KEY_A
  
  byte buffer1[64];
  byte block = 1;
  byte len = 18;
 

  //-------------------- LECTURA DE BLOQUE 1 - NOMBRE

  // - AUTENTICACION
  
  Serial.print(F("Name:"));
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid)); //line 834 of MFRC522.cpp file
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("Authentication failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  // - LECTURA DE BLOQUE 1

  status = mfrc522.MIFARE_Read(block, buffer1, &len);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("Reading failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  for (uint8_t i = 0; i < 16; i++) {
    Serial.write(buffer1[i] );
  }
  
 Serial.print(F("\n "));
 mfrc522.PICC_HaltA(); // Stop reading
 mfrc522.PCD_StopCrypto1();


}

void setup() {
  Serial.begin(9600);   // Initialize serial communications with the PC
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init();   // Init MFRC522
  //mfrc522.PCD_DumpVersionToSerial();  // Show details of PCD - MFRC522 Card Reader details
  //Serial.println(F("Scan PICC to see UID, SAK, type, and data blocks..."));
}

void loop() {
    
    Lectura();
    
  
   
 
  //-----------------------------------------------------------------------
}
