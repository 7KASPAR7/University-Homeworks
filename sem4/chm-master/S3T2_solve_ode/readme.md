Методичка: http://www.apmath.spbu.ru/ru/staff/eremin/files/task8_2016.pdf

Во вложении тесты для ваших численных решений задачи Коши.

* `py/`
	* `test_fix_step.py` - набор тестов для интегрирования с постоянным шагом:
		* `test_one_step()` - проверит одношаговые методы
		* `test_multi_step()` - проверит многошаговые методы

	* `test_adap_step.py` - набор тестов для интегрирования с выбором шага:
		* `test_adaptive()` - проверит алгоритмы автоматического выбора шага
		* `test_adaptive_order()` - проверит сходимость методов (их порядок)
		* `test_arenstorf()` - продемонстрирует работу на орбите Аренсторфа

	* `test_stiff.py` - набор тестов с жёсткими задачами:
		* `test_stiff()` - проверит явный и неявный методы Эйлера и метод Розенброка

	* `one_step_methods.py` - тут должны быть ваши одношаговые методы. Каждый метод - это объект класса, умеющего делать `step()`
		* `ExplicitEulerMethod` - явный метод Эйлера (уже реализован)
		* `ImplicitEulerMethod` - неявный метод Эйлера
		* `RungeKuttaMethod()` - метод Рунге-Кутты. Нужно переписать `step()` без использования стороннего кода
		* `EmbeddedRungeKuttaMethod()` - вложенный метод Рунге-Кутты. Он должен уметь делать `embedded_step()`, возвращая как приближение (`y1`), так и разность двух приближений (`y2-y1`) 
		* `EmbeddedRosenbrockMethod()` - вложенный метод Розенброка. Он также должен уметь делать `embedded_step()`

	* `multistep_methods.py` - тут должны быть ваши многошаговые методы:
		* `adams()` - метод Адамса (порядок метода зависит от длины списка коэффициентов, который приходит как параметр)

	* `solve_ode.py` - тут собственно алгоритмы интегрирования (верхний уровень):
		* `fix_step_integration()` - с постоянным шагом. Получает всю сетку времени как параметр (уже реализован)
		* `adaptive_step_integration()` - с автоматическим выбором шага. Для контроля локальной погрешности должен использовать параметры `atol` и `rtol`. Тип выбора шага (правило Рунге или вложенные методы) задаётся параметром `adapt_type`