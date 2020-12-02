#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

volatile unsigned int ValPot;

//---------------------------------
// Analogue port read
// Lecture dde l'ADC 2 sur la pin 4
//---------------------------------
void analogRead() {
  ADMUX = _BV(ADLAR) | _BV(MUX1);     // left shift result and use ADC2 for pot
  ADCSRA |= _BV(ADEN);                // Analog-Digital enable bit
  ADCSRA |= _BV(ADSC);                // Discard first conversion
  while (ADCSRA & _BV(ADSC)) {};      // Wait until conversion is done
  ADCSRA |= _BV(ADSC);                // Start single conversion
  while (ADCSRA & _BV(ADSC)) {};      // Wait until conversion is done
  ADCSRA &= ~_BV(ADEN);               // Shut down ADC
  ValPot=ADCH*8;          
  if (ValPot>2000)            // Shaping ADC reading
    ValPot=2000;
}

//-----------------------------
// interruption mode CTC a 50hz
//-----------------------------
ISR(TIM0_COMPA_vect) {
  PORTB |= (1<<PB0);            // Pin 0 high
  _delay_loop_2(ValPot+2000);       // Waiting 
  PORTB &= ~(1<<PB0);           // Pin 0 Low
} 

//--------------------
// Programme principal
//--------------------
int main (void) {
  sei();                      // Enable global interrupts
  DDRB |= (1<<PB0) | (1<<PB1);          // PB0 and PB1 as outputs
  TCCR0A |= (1<<WGM01);             // Configure timer 0 for CTC mode
  TIMSK |= (1<<OCIE0A);               // Enable CTC interrupt
  TCCR0B |= (1<<CS02) | (1<<CS00) ;         // Prescaler clk/1024
  OCR0A = 156;                  // Set CTC pour execution 50hz
  ADCSRA |= _BV(ADEN) | _BV(ADPS1) | _BV(ADPS0);  // ADC Enable and Div 8 prescaler
  ValPot=0;                   // RAZ variable lecture potentiometre
  while(1) {
    analogRead();               // read pot value and refresh ValPot
  }
}
