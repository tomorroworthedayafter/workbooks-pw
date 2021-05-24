//1.1
#include<iostream>
using namespace std;


void main()
{
	setlocale(LC_ALL, "Russian");

	int Var1;
	cout << "Введите число: ";
	cin >> Var1;

	char Var2;
	cout << "Введите букву: ";
	cin >> Var2;

	float Var3;
	cout << "Введите нецелое число: ";
	cin >> Var3;

	double Var4;
	cout << "Введите нецелое число№2: ";
	cin >> Var4;

	cout << "Число = " << Var1 << endl << "Буква = " << Var2 << endl << "Нецелое число = " << Var3 << endl << "Нецелое число №2 = " << Var4 << endl;
}
	//1.2
#include<iostream>
		using namespace std;


	void main()
	{
		setlocale(LC_ALL, "Russian");

		char Var1, Var2, Var3, Var4, Var5;

		cout << "Введите слово из 5 букв: ";

		cin >> Var1 >> Var2 >> Var3 >> Var4 >> Var5;

		cout << Var1 << Var2 << Var3 << Var4 << Var5;
	}
	//1.3
#include<iostream>
		using namespace std;


	void main()
	{
		setlocale(LC_ALL, "Russian");

		int Var1;
		cout << "Введите число №1: ";
		cin >> Var1;

		int Var2;
		cout << "Введите число №2: ";
		cin >> Var2;

		cout << "Сумма = " << Var1 + Var2 << endl << "Разница = " << Var1 - Var2 << endl << "Произведение = " << Var1 * Var2 << endl;
	}
	//1.4
#include<iostream>
		using namespace std;


	void main()
	{
		setlocale(LC_ALL, "Russian");

		int n; // Клетки
		int m; // Зайцы

		cout << "Введите количество зайцев: ";
		cin >> m;
		cout << "Введите количество клеток: ";
		cin >> n;
		cout << "Максимальное количество зайцев, которое гарантированно окажется в 1 клетке = " << (m + n - 1) / n << endl;
	}
	//1.5
#include<iostream>
		using namespace std;


	void main()
	{
		setlocale(LC_ALL, "Russian");

		int a; // сторона квадрата

		cout << "Введите сторону квадрата: ";
		cin >> a;
		cout << "Периметр квадрата = " << a * 4 << endl << "Площадь квадрата = " << a * a << endl;
	}
	//1.6
#include<iostream>
#include<cmath>
		using namespace std;


		void main()
		{
			setlocale(LC_ALL, "Russian");

			int a; // 1й катет
			int b; // 2й катет

			cout << "Введите 1й катет: ";
			cin >> a;
			cout << "Введите 2й катет: ";
			cin >> b;

			cout << "Гипотенуза = " << sqrt((a * a) + (b * b)) << endl;
		}
		//1.7
#include<iostream>
#include<cmath>
			using namespace std;


			void main()
			{
				setlocale(LC_ALL, "Russian");

				int N; // Кол-во школьников
				int K; // Кол-во яблок

				cout << "Введите кол-во школьников: ";
				cin >> N;
				cout << "Введите кол-во яблок: ";
				cin >> K;

				cout << "Каждому школьнику достанется яблок  " << K / N << endl;
			}
			//1.8
#include<iostream>
#include<cmath>
				using namespace std;


			void main()
			{
				setlocale(LC_ALL, "Russian");

				float x;


				cout << "Введите x: ";
				cin >> x;

				cout << "Значение функции = " << x * x + 3 * x - 100 << endl;
			}
			//1.9
#include<iostream>
				using namespace std;


			void main()
			{
				setlocale(LC_ALL, "Russian");

				cout << "Захаров Александр БФБО-01-20";
			}
			//1.10
				//Программа для решения квадратного уравнения
#include<iostream>
#include<cmath>
				using namespace std;


			void main()
			{
				setlocale(LC_ALL, "Russian");

				float a, b, c, D;

				cout << "Введите коэф-ты a, b, c ";
				cin >> a;
				cin >> b;
				cin >> c;
				D = b * b - 4 * a * c; // Определяем дискриминант

				cout << "D = " << b * b - 4 * a * c << endl << "x1 = " << -b + sqrt(D) << endl << "x2 = " << -b - sqrt(D);
			}
			//1.11
#include<iostream>
#include<cmath>
				using namespace std;


			void main()
			{
				setlocale(LC_ALL, "Russian");
				int ch = 10000; // Чашки
				int bl = ch; // Блюдца
				int l = ch; // Ложки
				cout << "Чашки = " << ch << endl << "Блюдца = " << bl << endl << "Ложки = " << l << endl;


			}
			//1.12
#include<iostream>
using namespace std;
			void main()
				{
					setlocale(LC_ALL, "Russian");
					int a, b;
					cin >> a >> b;
					swap(a, b);
					cout << a << endl << b << endl;
				}
