/**********************************************************************************/
/*  Pin 0,1,2,3 are for 4 channels analog input
 *  When digital pin 4 is high, program start doing the sonar things
 *  When the Arduino restart with digital pin 6 High, after 1s delay, 
 *Arduino start reading standard signal from analog pin 5 for a specified length
 *
 *  It's better to print out array "StandardSignal", remove the nonsignal part, 
 *and then hardcode back. (make calculation more efficient)
 *
 *  Thanks for Sofia's raw code
 *
 *  Richard Shen 2016/11/17
****************************************************/
#define SignalSetupLength 5000              //(number of samples in the standard signal) need to be determined
#define SignalReadLength 5000               //(number of samples in the reading signal) need to be determined. The length to read real signal.
#define TEMP 20                             //temperature of water, to be determined
// read signal from 4 sonar reciever, convolute with standard signal
int TIMEGAP1 = 1;                            //sampling time gap between channels in microseconds?  need to be determined
int TIMEGAP2 = 5;                            //sampling time gap in the same channel (4*TIMEGAP1 + time of 'for loop') need to be determined
float DPiezo = 0.5;                          //distance between piezos, in meters
int StandardSignal[SignalSetupLength];// = {/*need Standard Signal*/};

int SetupPin = 6; //a pin tells arduino to setup Standard Signal
int StandardInputPin = 5;
int SignalFlagPin = 4;//when it is high start reading signals from 4 channels
//from the top right corner, piezos are labeled as 0, 1, 2, 3 clock-wisely
int SignalInput0 = 0;
int SignalInput1 = 1;
int SignalInput2 = 2;
int SignalInput3 = 3;
//need pins to get temperature data

float getTemp();
void convolution(const int Signal[], int SignalLen,
                 const int Standard[], int StandardLen,
                 int Result[]);
float angle(float time1, float time2, float d, float v);
void maxIndex(int array[], int LengthX, int* MaxValue, int* Index);



float getTemp()
{
  float Temp=TEMP;  
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
  pinMode(SetupPin, INPUT);
  pinMode(StandardInputPin, INPUT);
  pinMode(SignalInput0, INPUT);
  pinMode(SignalInput1, INPUT);
  pinMode(SignalInput2, INPUT);
  pinMode(SignalInput3, INPUT);
  pinMode(SignalFlagPin, INPUT);

  if(digitalRead(SetupPin) == HIGH)//
  {
    delay(1000);//delay 1s then start reading the standard signal
    //better use a LED as a signal to start reading
    for(int i=0; i<SignalSetupLength; i++)
    {
      //read 4 times to mimic sampling rate of real signal
      StandardSignal[i] = analogRead(StandardInputPin);
      StandardSignal[i] = analogRead(StandardInputPin);
      StandardSignal[i] = analogRead(StandardInputPin);
      StandardSignal[i] = analogRead(StandardInputPin);
      //it is better to print out the standard signal after that remove non signal part and manualy put into this array
    } 
  }
}


void loop() 
{
  int Signal0[SignalReadLength];
  int Signal1[SignalReadLength];
  int Signal2[SignalReadLength];
  int Signal3[SignalReadLength];
  float Volocity;
  
  
  int Temp = getTemp;
  Volocity=1.402385*1000 + 5.038813*Temp - 5.799136/100*Temp*Temp + 3.287156/10000*Temp*Temp*Temp; //sound speed in water under atm pressure

  
  
  if (digitalRead(SignalFlagPin) == HIGH) //is the SetupPin 'HIGH' cover the whole signal or just mark the start point?
  {

    for(int i=0; i<SignalReadLength; i++) //sampling rate need to be measured
    {
      Signal0[i] = analogRead(SignalInput0);
      Signal1[i] = analogRead(SignalInput1);
      Signal2[i] = analogRead(SignalInput2);
      Signal3[i] = analogRead(SignalInput3);
    }

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
    float Angle0Y = angle(Time1, Time0, DPiezo, Volocity);
    float Angle0X = angle(Time0, Time3, DPiezo, Volocity);  
  }
}
