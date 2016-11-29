/**********************************************************************************/
/*  Pin 0,1,2,3 are for 4 channels analog input
 *  When  pin 4 is high, program start doing the sonar things
 *  When the Arduino restart with digital pin 6 High, after 1s delay, 
 *Arduino start reading standard signal from analog pin 5 for a specified length
 *
 *  It's better to print out array "StandardSignal", remove the nonsignal part, 
 *and then hardcode back. (make calculation more efficient)

 * Units being used are celcius, microseconds and meters
 *  Thanks for Sofia's raw code
 *
 *  Richard Shen 2016/11/17
 ****************************************************/
#define SignalSetupLength 2000              //(number of samples in the standard signal) need to be determined
#define SignalReadLength 2000              //(number of samples in the reading signal) need to be determined. The length to read real signal.
#define TEMP 20                             //temperature of water, to be determined
#define sampleTime 6000						//How long we will need to sample the water for in microseconds
#define sampleRate 160000					//How many samples per second we will need


int TIMEGAP1 = 5;						     //sampling time gap between channels in microseconds?  need to be determined
int TIMEGAP2 = 5;                            //sampling time gap in the same channel (4*TIMEGAP1 + time of 'for loop') need to be determined
float DPiezo = 0.6666;                       //distance between piezos, in meters
float numSamples = (sampleTime/1000/1000)*sampleRate;

int StandardSignal[SignalSetupLength] = {127.0,135.0,142.0,150.0,158.0,166.0,173.0,181.0,188.0,195.0,201.0,208.0,214.0,219.0,225.0,230.0,234.0,238.0,242.0,245.0,248.0,250.0,252.0,253.0,254.0,254.0,254.0,253.0,252.0,250.0,248.0,245.0,242.0,238.0,234.0,230.0,225.0,219.0,214.0,208.0,201.0,195.0,188.0,181.0,173.0,166.0,158.0,150.0,142.0,135.0,127.0,118.0,111.0,103.0,95.0,87.0,80.0,72.0,65.0,58.0,52.0,45.0,39.0,34.0,28.0,23.0,19.0,15.0,11.0,8.0,5.0,3.0,1.0,0.0,-1.0,-1.0,-1.0,0.0,1.0,3.0,5.0,8.0,11.0,15.0,19.0,23.0,28.0,34.0,39.0,45.0,52.0,58.0,65.0,72.0,80.0,87.0,95.0,103.0,111.0,118.0,126.0,135.0,142.0,150.0,158.0,166.0,173.0,181.0,188.0,195.0,201.0,208.0,214.0,219.0,225.0,230.0,234.0,238.0,242.0,245.0,248.0,250.0,252.0,253.0,254.0,254.0,254.0,253.0,252.0,250.0,248.0,245.0,242.0,238.0,234.0,230.0,225.0,219.0,214.0,208.0,201.0,195.0,188.0,181.0,173.0,166.0,158.0,150.0,142.0,135.0,127.0,118.0,111.0,103.0,95.0,87.0,80.0,72.0,65.0,58.0,52.0,45.0,39.0,34.0,28.0,23.0,19.0,15.0,11.0,8.0,5.0,3.0,1.0,0.0,-1.0,-1.0,-1.0,0.0,1.0,3.0,5.0,8.0,11.0,15.0,19.0,23.0,28.0,34.0,39.0,45.0,52.0,58.0,65.0,72.0,80.0,87.0,95.0,103.0,111.0,118.0,126.0,135.0,142.0,150.0,158.0,166.0,173.0,181.0,188.0,195.0,201.0,208.0,214.0,219.0,225.0,230.0,234.0,238.0,242.0,245.0,248.0,250.0,252.0,253.0,254.0,254.0,254.0,253.0,252.0,250.0,248.0,245.0,242.0,238.0,234.0,230.0,225.0,219.0,214.0,208.0,201.0,195.0,188.0,181.0,173.0,166.0,158.0,150.0,142.0,135.0,127.0,118.0,111.0,103.0,95.0,87.0,80.0,72.0,65.0,58.0,52.0,45.0,39.0,34.0,28.0,23.0,19.0,15.0,11.0,8.0,5.0,3.0,1.0,0.0,-1.0,-1.0,-1.0,0.0,1.0,3.0,5.0,8.0,11.0,15.0,19.0,23.0,28.0,34.0,39.0,45.0,52.0,58.0,65.0,72.0,80.0,87.0,95.0,103.0,111.0,118.0,126.0,135.0,142.0,150.0,158.0,166.0,173.0,181.0,188.0,195.0,201.0,208.0,214.0,219.0,225.0,230.0,234.0,238.0,242.0,245.0,248.0,250.0,252.0,253.0,254.0,254.0,254.0,253.0,252.0,250.0,248.0,245.0,242.0,238.0,234.0,230.0,225.0,219.0,214.0,208.0,201.0,195.0,188.0,181.0,173.0,166.0,158.0,150.0,142.0,135.0,127.0,118.0,111.0,103.0,95.0,87.0,80.0,72.0,65.0,58.0,52.0,45.0,39.0,34.0,28.0,23.0,19.0,15.0,11.0,8.0,5.0,3.0,1.0,0.0,-1.0,-1.0,-1.0,0.0,1.0,3.0,5.0,8.0,11.0,15.0,19.0,23.0,28.0,34.0,39.0,45.0,52.0,58.0,65.0,72.0,80.0,87.0,95.0,103.0,111.0,118.0,126.0,135.0,142.0,150.0,158.0,166.0,173.0,181.0,188.0,195.0,201.0,208.0,214.0,219.0,225.0,230.0,234.0,238.0,242.0,245.0,248.0,250.0,252.0,253.0,254.0,254.0,254.0,253.0,252.0,250.0,248.0,245.0,242.0,238.0,234.0,230.0,225.0,219.0,214.0,208.0,201.0,195.0,188.0,181.0,173.0,166.0,158.0,150.0,142.0,135.0,127.0,118.0,111.0,103.0,95.0,87.0,80.0,72.0,65.0,58.0,52.0,45.0,39.0,34.0,28.0,23.0,19.0,15.0,11.0,8.0,5.0,3.0,1.0,0.0,-1.0,-1.0,-1.0,0.0,1.0,3.0,5.0,8.0,11.0,15.0,19.0,23.0,28.0,34.0,39.0,45.0,52.0,58.0,65.0,72.0,80.0,87.0,95.0,103.0,111.0,118.0,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127};
int Signal0[SignalReadLength];
int Signal1[SignalReadLength];
int Signal2[SignalReadLength];
int Signal3[SignalReadLength];
int SetupPin = 6; //a pin tells arduino to setup Standard Signal
int StandardInputPin = 5;
int sigSent = 0;//when true, signal was sent from ROV
//from the top right corner, piezos are labeled as 0, 1, 2, 3 clock-wisely
//Pin to enable the write signal
int serialWen = 7;
//need pins to get temperature data

float getTemp();
void convolution(const int Signal[], int SignalLen,
	const int Standard[], int StandardLen,
	int Result[]);
float angle(float time1, float time2, float d, float v);
void maxIndex(int array[], int LengthX, int* MaxValue, int* Index);
int serialListen();
bool serialSend(float angle1, float angle2);

int serialListen(){
//waits for line to send command, either pingHappened or return angles
}

bool serialSend(float angle1, float angle2){
//sends the angle data down the RS485 line
}

float getTemp()
{
	float Temp=21;
  //temperature in celcius
	//put codes to get temperature
	return Temp;
}

void convolution(const int Signal[], int SignalLen,
	const int Standard[], int StandardLen,
	int Result[])
{
	for (int n=0; n<SignalReadLength+SignalSetupLength-1; n++)
	{
		int kmin, kmax;
		Result[n] = 0;

		kmin = (n >= StandardLen - 1) ? n - (StandardLen - 1) : 0;
		kmax = (n < SignalLen - 1) ? n : SignalLen - 1;

		for (int k = kmin; k <= kmax; k++)
		{
			Result[n] += Signal[k] * Standard[n - k];
		}
	}
}


float angle(float time1, float time2, float d, float v) {
	float Angle;
	Angle = acos(((time1 + time2)*(time2 - time1) * v + pow(d, 2))/ (2 * time2 * d)) * 180 * 7 / 22;
	return Angle;
}


void maxIndex(int array[], int LengthX, int* MaxValue, int* Index)
{
	for(int i=0; i<= LengthX; i++)
	{
		if (*MaxValue < array[i])
		{
			*MaxValue = array[i];
			*Index = i;
		}
	}
}


void setup() 
{

	int bit_mask = 0x7F;
	ADC1_SC1A = ((ADC1_SC1A&(~bit_mask))|0b1000000);
	bit_mask = 0xFF;
	ADC1_CFG1 = ((ADC1_CFG1&(~bit_mask))|0b00001100);
	bit_mask = 0x17;
	ADC1_CFG2 = ((ADC1_CFG2&(~bit_mask))|0b10111);
	bit_mask = 0x7F;
	ADC1_SC2 = ((ADC1_SC2&(~bit_mask))|0b0000100);
	bit_mask = 0x8F;
	ADC1_SC3 = ((ADC1_SC3&(~bit_mask))|0b10001100);
	bit_mask = 0xFF;
	ADC1_OFS = ((ADC1_OFS&(~bit_mask))|0b00000000);

  bit_mask = 0x7F;
  ADC0_SC1A = ((ADC1_SC1A&(~bit_mask))|0b1000000);
  bit_mask = 0xFF;
  ADC0_CFG1 = ((ADC1_CFG1&(~bit_mask))|0b00001100);
  bit_mask = 0x17;
  ADC0_CFG2 = ((ADC1_CFG2&(~bit_mask))|0b10111);
  bit_mask = 0x7F;
  ADC0_SC2 = ((ADC1_SC2&(~bit_mask))|0b0000100);
  bit_mask = 0x8F;
  ADC0_SC3 = ((ADC1_SC3&(~bit_mask))|0b10001100);
  bit_mask = 0xFF;
  ADC0_OFS = ((ADC1_OFS&(~bit_mask))|0b00000000);
  
	pinMode(SetupPin, INPUT);
	pinMode(StandardInputPin, INPUT);

	pinMode(serialWen,OUTPUT);
	Serial.begin(9600);
}


void loop() 
{
	float Volocity;
	float Angle0Y;
	float Angle0X;
	sigSent = serialListen();
	int bit_mask =0x7F;
	int analogVal;
  // adc_read();
	unsigned long t;
	sigSent=1;
	if (sigSent == 1) //is the SetupPin 'HIGH' cover the whole signal or just mark the start point?
	{

		float Temp = getTemp();
		Volocity=1.402385*1000 + 5.038813*Temp - 5.799136/100*Temp*Temp + 3.287156/10000*Temp*Temp*Temp; //sound speed in water under atm pressure
		t = micros();
		for(int i=0; i<SignalReadLength; i++) //sampling rate need to be measured
		{
			ADC1_SC1A = ((ADC1_SC1A&(~bit_mask))|0b1000000);
			Signal0[i] = ADC1_RA&0xFF;
			ADC0_SC1A = ((ADC0_SC1A&(~bit_mask))|0b1000000);
			Signal1[i] = ADC0_RA&0xFF;
			ADC1_SC1A = ((ADC1_SC1A&(~bit_mask))|0b1000001);
			Signal2[i] = ADC1_RA&0xFF;
			ADC0_SC1A = ((ADC0_SC1A&(~bit_mask))|0b1000001);
			Signal3[i] = ADC0_RA&0xFF;
		}
		t = micros() - t;
		Serial.println(t);
		int Result0[SignalReadLength+SignalSetupLength-1];
		int Result1[SignalReadLength+SignalSetupLength-1];
		int Result2[SignalReadLength+SignalSetupLength-1];
		int Result3[SignalReadLength+SignalSetupLength-1];

		convolution( Signal0, SignalReadLength,
			StandardSignal, SignalSetupLength,
			Result0);

		convolution( Signal1, SignalReadLength,
			StandardSignal, SignalSetupLength,
			Result1);

		convolution( Signal2, SignalReadLength,
			StandardSignal, SignalSetupLength,
			Result2);

		convolution( Signal3, SignalReadLength,
			StandardSignal, SignalSetupLength,
			Result3);

		float Time0, Time1, Time2, Time3;
		int MaxValue0, MaxValue1, MaxValue2, MaxValue3;
		int Index0, Index1, Index2, Index3;

		maxIndex(Result0, SignalReadLength, &MaxValue0, &Index0);
		maxIndex(Result1, SignalReadLength, &MaxValue1, &Index1);
		maxIndex(Result2, SignalReadLength, &MaxValue2, &Index2);
		maxIndex(Result3, SignalReadLength, &MaxValue3, &Index3);
		/*   
		     Index0 = Index0 - SignalSetupLength;
		     Index1 = Index1 - SignalSetupLength;
		     Index2 = Index2 - SignalSetupLength;
		     Index3 = Index3 - SignalSetupLength;
		 */   
		Time0 = Index0 * TIMEGAP2;
		Time1 = Index1 * TIMEGAP2 + TIMEGAP1;
		Time2 = Index2 * TIMEGAP2 + 2 * TIMEGAP1;
		Time3 = Index3 * TIMEGAP2 + 3 * TIMEGAP1;

		//the original point is piezo2
		float Angle2Y = angle(Time2, Time3, DPiezo, Volocity);
		//the original point is piezo2
		float Angle2X = angle(Time1, Time2, DPiezo, Volocity);
		//we also need angle base on piezo0
		Angle0Y = angle(Time1, Time0, DPiezo, Volocity);
		Angle0X = angle(Time0, Time3, DPiezo, Volocity);  
	}


	if(sigSent == 2){
		serialSend(Angle0X,Angle0Y);
	}
}
