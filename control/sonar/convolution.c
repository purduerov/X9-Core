#include <stddef.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>
//Assumption: Lengths and pointers won't be 0. SignalLen + KernelLen - 1 <= size_t -1
//Signal is the real signal you will get
//Kernel is the ideal signal

void convolve(const float Signal[/* SignalLen */], size_t SignalLen, 
              const float Kernel[/* KernelLen */], size_t KernelLen,
              float Result[/* SignalLen + KernelLen - 1 */])
{
  size_t n;

  for (n = 0; n < SignalLen + KernelLen - 1; n++)
  {
    size_t kmin, kmax, k;

    Result[n] = 0;

    kmin = (n >= KernelLen - 1) ? n - (KernelLen - 1) : 0;
    kmax = (n < SignalLen - 1) ? n : SignalLen - 1;

    for (k = kmin; k <= kmax; k++)
    {
      Result[n] += Signal[k] * Kernel[n - k];
    }
  }
}

void printSignal(const char* Name,
                 float Signal[/* SignalLen */], size_t SignalLen)
{
  size_t i;

  for (i = 0; i < SignalLen; i++)
  {
    printf("%s[%zu] = %f\n", Name, i, Signal[i]);
  }
  printf("\n");
}

float angle(float time1, float time2, float d, float v) {
	float angle;
	angle = acos(((time1 + time2)*(time2 - time1) * v + pow(d, 2))/ (2 * time2 * d)) * 180 * 7 / 22;
	return angle;
}

#define ELEMENT_COUNT(X) (sizeof(X) / sizeof((X)[0]))
#define DISTANCE 0.5
#define VELOCITY 50.45

int main(void)
{
  float signal1[] = { 1, 1, 1, 1, 1 };
  float signal2[] = { 0, 1, 1, 1, 0 };
  float signal3[] = { 1, 1, 1, 1, 1 };
  float signal4[] = { 1, 1, 1, 1, 1 };
  float kernel[] = { 1, 1, 1, 1, 1 };
  bool SignalReceive = true;
  float t = 0;
  while (t >= 0 && t <= 2) {
  if (SignalReceive) {
  	float result1[ELEMENT_COUNT(signal1) + ELEMENT_COUNT(kernel) - 1];
  	float result2[ELEMENT_COUNT(signal2) + ELEMENT_COUNT(kernel) - 1];
  	float result3[ELEMENT_COUNT(signal3) + ELEMENT_COUNT(kernel) - 1];
  	float result4[ELEMENT_COUNT(signal4) + ELEMENT_COUNT(kernel) - 1];

	  convolve(signal1, ELEMENT_COUNT(signal1),
		   kernel, ELEMENT_COUNT(kernel),
		   result1);

	  convolve(signal2, ELEMENT_COUNT(signal2),
		   kernel, ELEMENT_COUNT(kernel),
		   result2);
	  convolve(signal3, ELEMENT_COUNT(signal3),
		   kernel, ELEMENT_COUNT(kernel),
		   result3);
	  convolve(signal4, ELEMENT_COUNT(signal4),
		   kernel, ELEMENT_COUNT(kernel),
		   result4);
	  // printSignal("signal", signal, ELEMENT_COUNT(signal));
	  // printSignal("kernel", kernel, ELEMENT_COUNT(kernel));
	  //Print out the convolution result
	  printSignal("result1", result1, ELEMENT_COUNT(result1));
	  printSignal("result2", result2, ELEMENT_COUNT(result2));
	  printSignal("result3", result3, ELEMENT_COUNT(result3));
	  printSignal("result4", result4, ELEMENT_COUNT(result4));

	//Define time:
	  float t1 = 0.0;
	  float t2 = 0.12;
	  float t3 = 0.083;
	  float t4 = 0.02;

	  float delta_t2 = t2 - t1;
	  float delta_t3 = t3 - t1;
	  float delta_t4 = t4 - t1;

	  float angleY = angle(delta_t3, delta_t4, DISTANCE, VELOCITY);
	  float angleX = angle(delta_t2, delta_t3, DISTANCE, VELOCITY);
	  printf ("%f\n", angleX);
	  printf ("%f\n", angleY);
	}

	t = t + 0.1;
}
  return 0;
}
