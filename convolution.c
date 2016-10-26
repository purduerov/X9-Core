#include <stddef.h>
#include <stdio.h>
#include <math.h>

//Assumption: Lengths and pointers won't be 0. SignalLen + KernelLen - 1 <= size_t -1
//Signal is the real signal you will get
//Kernel is the ideal signal

void convolve(const double Signal[/* SignalLen */], size_t SignalLen, 
              const double Kernel[/* KernelLen */], size_t KernelLen,
              double Result[/* SignalLen + KernelLen - 1 */])
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
                 double Signal[/* SignalLen */], size_t SignalLen)
{
  size_t i;

  for (i = 0; i < SignalLen; i++)
  {
    printf("%s[%zu] = %f\n", Name, i, Signal[i]);
  }
  printf("\n");
}

double angle(double time1, double time2, double d, double v) {
	double angle;
	angle = acos(((time1 + time2)*(time2 - time1) * v + pow(d, 2))/ (2 * time1 * d)) * 180 * 7 / 22;
	return angle;
}

#define ELEMENT_COUNT(X) (sizeof(X) / sizeof((X)[0]))
#define DISTANCE 0.5
#define VELOCITY 50.45

int main(void)
{
  double signal1[] = { 1, 1, 1, 1, 1 };
  double signal2[] = { 0, 1, 1, 1, 0 };
  double signal3[] = { 1, 1, 1, 1, 1 };
  double signal4[] = { 1, 1, 1, 1, 1 };
  double kernel[] = { 1, 1, 1, 1, 1 };
  double result1[ELEMENT_COUNT(signal1) + ELEMENT_COUNT(kernel) - 1];
  double result2[ELEMENT_COUNT(signal2) + ELEMENT_COUNT(kernel) - 1];
  double result3[ELEMENT_COUNT(signal3) + ELEMENT_COUNT(kernel) - 1];
  double result4[ELEMENT_COUNT(signal4) + ELEMENT_COUNT(kernel) - 1];

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
  printSignal("result1", result1, ELEMENT_COUNT(result1));
  printSignal("result2", result2, ELEMENT_COUNT(result2));
  printSignal("result3", result3, ELEMENT_COUNT(result3));
  printSignal("result4", result4, ELEMENT_COUNT(result4));

  double t1 = 0.0;
  double t2 = 0.04;
  double t3 = 0.083;
  double t4 = 0.02;

  double delta_t2 = t2 - t1;
  double delta_t3 = t3 - t1;
  double delta_t4 = t4 - t1;

  double angleX = angle(delta_t3, delta_t4, DISTANCE, VELOCITY);
  printf ("%f\n", angleX);
  return 0;
}
