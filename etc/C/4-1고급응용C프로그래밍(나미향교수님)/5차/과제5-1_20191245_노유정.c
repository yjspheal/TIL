#include <stdio.h>

int main(void) {
	char veh_type;
	int hour; int min; int min_sum;

	printf("���� ���� : ");
	scanf("%c", &veh_type);
	printf("�ð� : ");
	scanf("%d", &hour);
	printf("�� : ");
	scanf("%d", &min);
	min_sum = (hour * 60 + min) / 10;

	if ((veh_type == 'C') || (veh_type == 'c')) {
		printf("������� : %d��\n", min_sum * 2000);
	}

	if ((veh_type == 'B') || (veh_type == 'b')) {
		printf("������� : %d��\n", min_sum * 3000);
	}

	if ((veh_type == 'T') || (veh_type == 't')) {
		printf("������� : %d��\n", min_sum * 5000);
	}
}

