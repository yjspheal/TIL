#include <stdio.h>
void Celsius(void);
void Fahrenheit(void);
int main(void)
{
	Celsius();
	printf("\n");
	Fahrenheit();
}
float Get_Celsius(void);
float Celsius_to_Fahrenheit(float celsi);
void Print_Fahrenheit(float fahre);
void Celsius(void) {
	float cel, fah;
	cel = Get_Celsius();
	fah = Celsius_to_Fahrenheit(cel);
	Print_Fahrenheit(fah);
}
float Get_Celsius(void) {
	float c;
	printf("���� �µ��� �Է��Ͻÿ� : ");
	scanf("%f", &c);
	return c;
}
float Celsius_to_Fahrenheit(float celsi) {
	return celsi * 180. / 100 + 32;
}
void Print_Fahrenheit(float fahre) {
	printf("ȭ�� �µ��� %.2f �Դϴ�\n", fahre);
}
float Get_Fahrenheit(void);
float Fahrenheit_to_Celsius(float fahre);
void Print_Celsius(float celsi);
void Fahrenheit(void) {
	float cel, fah;
	fah = Get_Fahrenheit();
	cel = Fahrenheit_to_Celsius(fah);
	Print_Celsius(cel);
}
float Get_Fahrenheit(void) {
	float f;
	printf("ȭ�� �µ��� �Է��Ͻÿ� : ");
	scanf("%f", &f);
	return f;
}
float Fahrenheit_to_Celsius(float fahre) {
	return 100./180 * (fahre - 32);
}
void Print_Celsius(float celsi) {
	printf("���� �µ��� %.2f �Դϴ�\n", celsi);
}
